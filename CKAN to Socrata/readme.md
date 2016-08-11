# CKAN to Socrata Connector

## What It Does

This is a simply Python script (CLI in development) that crawls the package list of a target CKAN portal, extracts the metadata related to each package, transforms it into standard Socrata metadata, and then loads it into a new External Link dataset, which is visible on the Socrata catalog. Currently, it will return the top level of the package _without_ the additional resources associated with that package (if any).

Incuded in the metadata is:

- Title of the package
- Package author
- Tags associated with the package
- Link to the package landing page
- Description of the package

## Example Usage

 The main class is in ckan_crawler.py, though the ckan_extract, ckan_transform, and ckan_load files are required as well. 

 ```python
 from ckan_crawler import Crawler
import yaml

with open('.config.yml','r') as f:
	config = yaml.load(f)

ckan_domain = 'datosabiertos.bogota.gov.co'
socrata_domain = 'demo.socrata.com'

ckan_to_socrata = Crawler(
	ckan_domain = ckan_domain,
	socrata_domain = socrata_domain,
	username = config['username'],
	password = config['password'],
	app_token = config['app_token']
	)

#Testing on a single package to make sure everything is correct
ckan_to_socrata.test()

#Once testing is complete, you can run it on all the packages
ckan_to_socrata.run()
``` 
