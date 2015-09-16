---
layout: listing
title: XLS to LIVES schema CSV
type: template-kettle

icon: fa-file-o

description: Reads data from 2 excel (XLS) files of Restaurant and Violation data and transforms the data to meet the LIVES schema into a csv file.

github_url: https://github.com/socrata/connectors/tree/master/XLS%20to%20LIVES%20Schema%20CSV
download_url: https://github.com/socrata/connectors/tree/master/XLS%20to%20LIVES%20Schema%20CSV/inspection_violations.zip
bugs_url: https://github.com/socrata/connectors/issues?labels=xls-to-lives-schema-csv&state=open
---

This workflow reads from 2 excel files in order to transform the data into a single a CSV file that is compliant to the LIVES Standard.[^1]

It uses the following transformations:

* [Excel Input](http://wiki.pentaho.com/display/EAI/Excel+Input+(XLS,+XLSX)+including+OpenOffice+Workbooks+(ODS))
* [String Operations](http://wiki.pentaho.com/display/EAI/String+operations) (Trim on key fields)
* [Sorter](http://wiki.pentaho.com/display/EAI/Sort+rows) for key fields (required before merge join)
* [Merge Join](http://wiki.pentaho.com/display/EAI/Merge+Join) (Left outer since a business may have no violation)
* [Concat Fields](http://wiki.pentaho.com/display/EAI/Concat+Fields) (Street # with Street Name)
* [Select Values](http://wiki.pentaho.com/display/EAI/Select+Values) (renames to schema, selects fields to write to output file)
* [Text Output](http://wiki.pentaho.com/display/EAI/Text+File+Output) (force quote enclosure, comma separator, [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) date format and trims all fields)

### Quickstart

Follow these steps to get the example workflow working.

1. Download the workflow and associated files using the Download link above and open it from Spoon. **NOTE:** You may have to right-click > Save Link As... to get it to download. 
2. Update the Paths to the Raw Inspection and Violation files so they point to the correct directory.[^2]
3. Update the path for the Text file output.
4. Run the workflow and ensure that the file transformed_data.csv was created in the directory with current timestamp.

### Notes
[^1]: The current [LIVE Standard](http://www.yelp.com/healthscores) is out of date.
[^2]: Be sure to add the new path after browsing to the file to ensure the workflow reads correct path.