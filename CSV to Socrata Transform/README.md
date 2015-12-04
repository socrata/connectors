# README #

Basic Kettle workflow documentation

### What is this workflow for? ###

* Demonstration of basic functionality of Kettle
*  CSV Input
*  Pivot Columns into flat rows
*  Rename
*  String Operations: Filter out unwanted characters, and unwanted values (ie "NA")
*  Change decimal to percent
*  Publish to Socrata

### How do I get set up? ###

* Download [Pentaho Kettle Community Edition](http://community.pentaho.com/)
* Download [DataSync](http://socrata.github.io/datasync/)
* Download the workflow and data
* Check out further [Kettle documentation](https://dev.socrata.com/connectors/pentaho-kettle.html) 

### The Transformation Workflow ###
* This workflow transforms the input file into a machine readable dataset ready to power your Socrata site
* On CSV File input browse to the path of the input file input.csv
* On the text file output browse to the path of output file location
* Open each step to understand how it was configured and what it achieves
* Open and compare the input file to the output. Output is ready for your Socrata site!


### The DataSync Runner Workflow ###
* This workflow runs the transformation workflow, then runs Datasync to publish to output file online
* You must first run the Transformation workflow and publish the output.csv to your site using DataSync
* Save the DataSync job, copy the command line prompt, run it in your command line
* Did it work? If not you might have to explicitly point to where your java instance is located or where your DataSync jar is located
* Once you have a command that executes the DataSync job paste the line into the step: DataSyncRunner in the workflow