from ckan_extract import Extract
from ckan_transform import Transform
from ckan_load import Load

class Crawler(object):
    def __init__(self,ckan_domain, socrata_domain,username, password, app_token):
        self.base_url = ckan_domain
        self.socrata_url = socrata_domain
        self.config = {}
        self.config['username'] = username
        self.config['password'] = password
        self.config['app_token'] = app_token
        return

    def run(self):
        print("Running Extraction for %s" % self.base_url)
        extraction = Extract(self.base_url)
        raw_data = extraction.run()
        print("Success\n\n")

        print("Running Transformation of metadata")
        transformation = Transform(raw_data, self.base_url)
        cleaned_data = transformation.run()
        print("Success\n\n")

        print("Loading datasets to %s" % self.socrata_url)
        load = Load(cleaned_data,self.socrata_url, self.config)
        response = load.run()
        return response
        
    def test(self):
        print("Running Extraction for %s" % self.base_url)
        extraction = Extract(self.base_url)
        raw_data = extraction.test()
        print("Success\n\n")

        print("Running Transformation of metadata")
        transformation = Transform(raw_data, self.base_url)
        cleaned_data = transformation.test()
        print("Success\n\n")

        print("Loading datasets to %s" % self.socrata_url)
        load = Load(cleaned_data,self.socrata_url, self.config)
        response = load.test()
        return response