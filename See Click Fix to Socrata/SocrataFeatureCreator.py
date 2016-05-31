import urllib2
import base64
import json
import csv
import fme
import fmeobjects


logger = fmeobjects.FMELogFile()

# CONFIGURATION

org_csv = fme.macroValues['SourceDataset_CSV']

#character limit in See Click Fix is larger than Socrata, if the description is too long it will break workflow
if fme.macroValues['max_descripton_length']:
    MAX_DESCRIPTION_LENGTH = fme.macroValues['max_descripton_length']
else:
    MAX_DESCRIPTION_LENGTH = 1000
logger.logMessageString("Maximum issue description length set to " + str(MAX_DESCRIPTION_LENGTH) + " chars")


scf_open_endpoint = 'seeclickfix.com/open311/v2'

if fme.macroValues['replace_dataset'] != 'Yes':
    fme.macroValues['replace_dataset'] = 'No'

logger.logMessageString("Using SeeClickFix endpoint: " + scf_open_endpoint)

# CONSTANTS

scf_issues_endpoint_suffix = 'requests.json'

logger = fmeobjects.FMELogFile()

# Template Class Interface:
class SCFIssueFeatureCreator(object):

    def input(self,feature):
        pass
    def close(self):
        total_issues = 0
        all_orgs = get_all_scf_orgs()
        
        for name, org_id in all_orgs.iteritems():
            curr_page = 1
            
            has_more_left = True
            while has_more_left:

                page_url = 'https://' + scf_open_endpoint + '/' + str(org_id) + '/' + scf_issues_endpoint_suffix + '?page=' + str(curr_page)
                logger.logMessageString("Paging through result page: " + page_url)

                req = urllib2.Request(page_url)
                response = urllib2.build_opener().open(req).read()
                cur_issues = json.loads(response)

                cur_issues_formatted = get_socrata_formatted_issues(cur_issues, get_org_name_without_state(name))

                logger.logMessageString("Exporting SCF issues as Features.")
                for row in cur_issues_formatted:
                    feature = fmeobjects.FMEFeature()
                    for key in row.keys():
                        if not row[key] is None:
                            feature.setAttribute(key, row[key])
                    self.pyoutput(feature)

                if len(cur_issues) > 0:
                    curr_page += 1
                    total_issues += len(cur_issues)
                else:
                    has_more_left = False
                    logger.logMessageString("No more pages left.")
        
        logger.logMessageString("Processed a total of %d issues in %d organizations." % (total_issues, len(all_orgs)))


def get_all_scf_orgs(limit = 100):
    with open(org_csv, mode='r') as infile:
        #get data from org csv
        data = [row for row in csv.reader(infile.read().splitlines())]
        #customer = dict((rows[0])  for rows in data)
        #logger.logMessageString(customer)
        orgs = dict((rows[0],rows[1]) for rows in data)
    return orgs

# Given a list of issues in SCF format (map),
# Returns a list of issues such that each issue is ready for publication to Socrata dataset (ServiceConnect app schema)
def get_socrata_formatted_issues(issues, city_name):
    socrata_issues = []
    for issue in issues:
        issue_description = issue['description'] if issue['description'] is not None else ''
        
        if len(issue_description) > MAX_DESCRIPTION_LENGTH:
            logger.logMessageString("Issue description exceeded max length of %s chars, and was shortened from %s chars" % (MAX_DESCRIPTION_LENGTH, len(issue_description)))
            issue_description = issue_description[:MAX_DESCRIPTION_LENGTH] + '...'
        if issue['status'] == 'closed':
            closed_date_time = issue['updated_datetime']
        else:
            closed_date_time = None
        #closed_date_time = issue['updated_datetime'] if issue['status'] is 'closed' else None

        formatted_issue = {
            'ticket_id': issue['service_request_id'],
            'ticket_status': issue['status'],
            'issue_description': issue_description,
            'lat': issue['lat'],
            'lng': issue['long'],
            'location': "(%s,%s)" % (issue['lat'], issue['long']),
            'address': issue['address'],
            'issue_type': issue['service_name'],
            'city': city_name,
            'ticket_closed_date_time': format_date(closed_date_time),
            'ticket_created_date_time': format_date(issue['requested_datetime']),
            'ticket_last_updated_date_time': format_date(issue['updated_datetime']),
            'image': issue['media_url']
        }

        socrata_issues.append(formatted_issue)
    return socrata_issues

def get_org_name_without_state(org_name):
	#data cleaning incorrect orgnames with nulls: org_name.replace(old, new)
    return org_name.replace(', MA', '').replace(' MA', '')

def format_date(date_str):
    if date_str is None:
        return None
    
    parts = date_str.split('-')
    return "%s-%s-%s" % (parts[0], parts[1], parts[2])


