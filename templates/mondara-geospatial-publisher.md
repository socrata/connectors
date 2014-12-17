---
layout: listing
title: Mondara Geospatial Publisher
type: template

icon: fa-compass

description: Allows publishing geospatial data read into FME (in this example from a Shapefile containing points) to update an existing Socrata Mondara Geospatial Dataset.

github_url: https://github.com/socrata/connectors/tree/master/Mondara%20Geospatial%20Publisher
download_url: https://github.com/socrata/connectors/raw/master/Shapefile%20to%20Socrata/Shapefile%20to%20Socrata.fmwt
bugs_url: https://github.com/socrata/connectors/issues?labels=mondara-publisher&state=open
---

This workflow demonstrates publishing geospatial data read into FME (in this example from a Shapefile containing points) to update (by replacing) an existing Socrata Mondara Geospatial Dataset.

[View preview of workflow](https://github.com/socrata/connectors/blob/master/Mondara%20Geospatial%20Publisher/geospatial_publisher_preview.png)

### Quickstart

Follow these steps to get the example workflow working to update a dataset. Once you have it working you can swap out the FME Reader with a reader for the geospatial data you wish to publish.

1. [Download the workflow](https://github.com/socrata/connectors/raw/geospatial-publisher/Mondara%20Geospatial%20Publisher/socrata_geospatial_publisher.fmwt) and open it in FME Desktop.

2. Create a new Geospatial Dataset on your Socrata data portal. Refer to [this guide](https://support.socrata.com/hc/en-us/articles/202950488-Host-geospatial-files-using-Socrata-Mondara) for information on Geospatial datasets.

3. Copy the dataset ID of the Geospatial dataset you created in Step 1. To obtain the dataset ID, navigate to the dataset in your web browser. In the address bar the dataset ID is the code at the end of the URL in the form `xxxx-xxxx`. For example, for the dataset https://data.seattle.gov/Public-Safety/Fire-911/m985-ywaw, it’s identifier would be `m985-ywaw`.

4. Update the following User Parameters in the Navigator panel in the upper left of FME:
    - socrata_username  
    - socrata_password
    - socrata_dataset_uid (dataset ID obtained in Step 3)
    - socrata_domain (e.g. data.seattle.gov)

5. Run the workflow and refresh the page for the Geospatial Dataset to verify that it was updated to show a set of points in Austin, Texas (when you click on a point you should see the 7 attributes listed under the Writer called 'facilties' in the workflow template).  
**NOTE:** sometimes it takes a up to a minute or two for the changes to be reflected in the dataset. 


### Adapting the workflow for your geospatial data

To publish geospatial data from another source such as geospatial database or an ArcGIS server endpoint (ESRI-JSON) make the following changes:

1. Replace the 'faciltiies' reader with the appropriate Reader in FME (e.g. ESRI-JSON reader)

2. Update the Writer on the right (called 'facilties') to include the appropriate attributes you wish to publish. Double click on the Writer, click the Attribute Definition tab, and remove all the existing attributes. Re-add the attributes you wish to publish. You can add all attributes from a Reader by right-clicking the Writer and selecting 'Copy attributes from Feature Type'.  
**NOTE:** no attributes can be longer than 10 characters so you may need to use an [AttributeRenamer](http://docs.safe.com/fme/html/FME_Transformers/Default.htm#Transformers/attributerenamer.htm) transformer to rename attributes longer than 10 characters

3. If the geospatial data you are reading is not point data then you will need to double-click on the Writer and select the appropriate item from the 'Allowed Geometries' dropdown menu.

4. Run the workflow!
