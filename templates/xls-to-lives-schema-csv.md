---
layout: listing
title: XLS to LIVES schema CSV
type: template

icon: fa-file-o

description: Reads data from 2 excel (XLS) files of Restaurant and Violation data and transforms the data to meet the LIVES schema into a csv file.

github_url: https://github.com/socrata/connectors/tree/master/XLS%20to%20LIVES%20Schema%20CSV
download_url: https://github.com/socrata/connectors/tree/master/XLS%20to%20LIVES%20Schema%20CSV/inspection_violations.zip
bugs_url: https://github.com/socrata/connectors/issues?labels=xls-to-lives-schema-csv&state=open
---

### Quickstart

Follow these steps to get the example workflow working.

1. Download the workflow and associated files using the Download link above and open it from Spoon. **NOTE:** You may have to right-click > Save Link As... to get it to download. 
2. Update the Paths to the Raw Inspection and Violation files so they point to the correct directory. Also update the path for the Text file output.
3. Run the workflow and ensure that the file transformed_data.csv was created in the directory with current timestamp.