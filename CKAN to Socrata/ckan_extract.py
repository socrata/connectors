import requests

class Extract(object):
    def __init__(self, base_url):
        self.all_packages_url = 'http://' + base_url.replace('http://','') + '/api/3/action/package_list'
        self.package_metadata_url = 'http://' + base_url.replace('http://','') + '/api/3/action/package_show?id='
        return

    def run(self):
        packages = self.get_packages()
        metadata = self.get_metadata(packages)
        return metadata

    def test(self):
        packages = self.get_packages()
        metadata = self.get_metadata(packages)
        return metadata[0]

    def get_packages(self):
        r = requests.get(self.all_packages_url)
        packages = r.json()['result']
        return packages

    def get_metadata(self, packages):
        metadata = []
        for package in packages:
            url = self.package_metadata_url+package
            print("Getting Metadata for %s" % url)
            r = requests.get(url)
            package_metadata = r.json()['result']
            metadata.append(package_metadata)

        return metadata
