---
layout: listing
title: CSV to Socrata Transform
type: template-kettle

icon: fa-file-o

description: Reads data from 1 csv, pivots columns to rows and other transformations then publishes to Socrata.

github_url: 
download_url: 
bugs_url: 
---

This workflow demonstrates the basic functionality of Pentaho Kettle Data Integration in order to clean a file, pivot columns to rows, and publish to Socrata.

To publish to Socrata using Pentaho is a two-step process. 1 workflow runs the transformations and the 2nd workflow runs datasync on the updated and transformed csv.

### The Transformations

#### tranformation.ktr workflow:

* [CSV Input](http://wiki.pentaho.com/display/EAI/CSV+File+Input)
* [Row Normaliser](http://wiki.pentaho.com/display/EAI/Row+Normaliser) in order to Pivot Columns into flat rows
* [Filter Rows](http://wiki.pentaho.com/display/EAI/Filter+Rows) to remove unwated "NA" characters
* [Select Values](http://wiki.pentaho.com/display/EAI/Select+Values) (renames to schema, selects fields to write to output file)in order to Rename Columns
* [Formula](http://wiki.pentaho.com/display/EAI/Formula) in order to change decimal rate to whole number and comply with Socrata Percent Data Type
* [Replace String](http://wiki.pentaho.com/display/EAI/Replace+in+String) in order to remove unwanted text from cells
* [Text Output](http://wiki.pentaho.com/display/EAI/Text+File+Output) (force quote enclosure, comma separator, [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) date format and trims all fields)

#### datasyncrunner.kjb:
* [Job Scheduling](http://wiki.pentaho.com/display/EAI/Job+Executor) to iniate workflow
* [Transformation](http://wiki.pentaho.com/display/EAI/Transformation+Executor) runs the transformation.ktr workflow
* [Execute Shell Script](http://wiki.pentaho.com/display/EAI/Shell) runs datasync

### Quickstart

Follow these steps to get the example workflow working.

1. Download [Pentaho Kettle Community Edition](http://community.pentaho.com/) and [Datasync](http://socrata.github.io/datasync/)
2. Download the workflow and associated files using the Download link above and open it from Spoon. **NOTE:** You may have to right-click > Save Link As... to get it to download. 
3. Update the Paths to the Raw Inspection and Violation files so they point to the correct directory.[^2]
4. Update the path for the Text file output.
5. Run the workflow and ensure that the file transformed_data.csv was created in the directory with current timestamp.