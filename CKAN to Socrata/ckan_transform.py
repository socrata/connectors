class Transform(object):
    def __init__(self, raw_data, base_url):
        self.data = raw_data
        self.base_url = base_url
        return
    def run(self):
        clean_data = []
        for package in self.data:
            cleaned = self.transform(package)
            clean_data.append(cleaned)
        return clean_data
    
    def test(self):
        clean_data = self.transform(self.data)
        return clean_data
        
    def transform(self, package):
        cleaned_package = dict()
        #Socrata Specific
        cleaned_package['viewType'] = 'href'
        cleaned_package['displayType'] = 'href'

        #Package name and attribution
        cleaned_package['name'] = package['title']
        cleaned_package['attribution'] = package['author']
        #cleaned_package['attributionLink'] = package['url']

        #Package Description
        cleaned_package['description'] = package['notes']
        #Package Tags
        if package['tags']:
            cleaned_package['tags'] = []
            for i in range(len(package['tags'])):
                cleaned_package['tags'].append(package['tags'][i]['display_name'])

        #METADATA :(
        cleaned_package['metadata'] = {}
        cleaned_package['metadata']['accessPoints'] = {
            'text/html':'http://'+self.base_url.replace('http://','')+'dataset/'+package['id']}

        return cleaned_package
