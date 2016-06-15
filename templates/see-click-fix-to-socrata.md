---
layout: listing
title: See Click Fix to Socrata
type: template-fme

icon: fa-file-o

description: Pulls data from the See Click Fix API and publishes to Socrata dataset

github_url: https://github.com/socrata/connectors/tree/master/See%20Click%20Fix%20to%20Socrata
download_url: https://github.com/socrata/connectors/blob/master/See%20Click%20Fix%20to%20Socrata/SCF2Socrata.zip
bugs_url: https://github.com/socrata/connectors/issues
---

Pulls data from the See Click Fix API and publishes to Socrata dataset.

It relies heavily on a custom python script which does the following:

* Loop through the org id of each city
* Paginate through the data on [See Click Fix API](http://dev.seeclickfix.com/): [https://seeclickfix.com/api/v2/<orgid>](http://dev.seeclickfix.com/#url-format)
* Transform the data from json to FME Feature Attributes
* Publish to Socrata using the [Socrata Writer](https://dev.socrata.com/blog/2014/10/09/fme-socrata-writer.html)

### Quickstart

Follow these steps to get the example workflow working.

1. Download the workflow and associated files using the Download link above and open in FME Workbench.
2. Contact dev@seeclickfix.com to obtain account IDs for the customer's account on SeeClickFix. For example if you are an open data administrator for a state level agency you should obtain the city ids for all pertinent cities and list them 1 per row.
3. Fill out the org_id file with the above information, save changes.
4. Configure the FME Published Parameters.
5. For 1st run dataset creation: Change Socrata Writer dataset title to desired dataset title.
6. Run the workflow.
7. Search the logs for "dataset id" and change the Socrata Writer to this 4-4
8. Run the workflow again.
9. Schedule this workflow on a regular cadence, for example with [Windows Task Scheduler](https://support.socrata.com/hc/en-us/articles/215760118-Scheduling-a-DataSync-Update-Job-Using-Windows-Task-Scheduler)

### Troubleshooting
To test the See Click Fix API and your org id, [make a "GET" request to](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=gmail) https://seeclickfix.com/api/v2/<org_id>.

If FME log shows errors with specific parameters, make sure all published parameters are filled out correctly.



