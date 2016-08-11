import requests
import json

class Load(object):
    def __init__(self, cleaned_data, socrata_url, config):
        self.socrata_url = socrata_url
        self.upload_url = 'https://'+socrata_url+'/api/views.json'
        self.publish_url = 'https://'+socrata_url+'/api/views/'
        self.metadata = cleaned_data
        self.username = config['username']
        self.password = config['password']
        self.app_token = config['app_token']

        return
    def run(self):
        for dataset in self.metadata:
            print("Uploading dataset %s" % dataset['name'])
            print(self.createExternalDataset(dataset))
        return "Success"

    def test(self):
        print("Uploading dataset %s" % self.metadata['name'])
        print(self.createExternalDataset(self.metadata))
        return "Success"  

    def createExternalDataset(self, dataset):
        headers = {"X-App-Token":self.app_token}

        response = requests.post(
            self.upload_url,
            data=json.dumps(dataset),
            headers=headers,
            auth=(self.username, self.password)
            )
        if response.status_code == 200:
            r = self.publishExternalDataset(response.json()['id'])
            if r:
                return_response = "Successfully created at https://"+self.socrata_url+"/d/"+response.json()['id']
                return return_response
            else:
                return "Failed"
        else:
            return "Failed to create %s, %s" % (dataset['name'], response.text)
    def publishExternalDataset(self, id):
        print("Publishing %s" % id)
        url = self.publish_url+id+'/publication.json'
        empty = {}
        headers = {"X-App-Token":self.app_token}
        publish_response = requests.post(
            url,
            data=json.dumps(empty),
            headers=headers,
            auth=(self.username,self.password)
            )
        if publish_response.status_code == 200:
            return True
        else:
            print("Failed to publish %s, %s" % (id, publish_response.text))
            return False