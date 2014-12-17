---
layout: listing
title: ArcGIS Server
type: template

icon: fa-globe

description: Extracts data from an ArcGIS Server endpoint (Esri-JSON) and publishes it to Socrata.

github_url: https://github.com/socrata/connectors/tree/master/ArcGIS%20Server
download_url: https://github.com/socrata/connectors/raw/master/ArcGIS%20Server/ArcGIS%20Server2Socrata.fmwt
bugs_url: https://github.com/socrata/connectors/issues?labels=arcgis-server&state=open
---

# ArcGIS Server to Socrata

This FME workflow extracts data from an ArcGIS Server endpoint (Esri-JSON) and publishes it to Socrata.

[View preview of workflow](https://github.com/socrata/connectors/blob/master/ArcGIS%20Server/arcgis_server_preview.png)


## Obtain your ArcGIS Esri-JSON URL

1. Determine what ArcGIS layer you want to export
  - It must be a Feature Layer with the REST service enabled
  - Currently it must be point data. The Socrata writer will coerce all the incoming features down to points by default.
  If you want more control over the placement of points you must summarize it down to centroids or something similar 
  with a CenterOfGravityReplacer or an InsidePointReplacer.
2. Click on "Query" at the bottom of the layer's entry in the ArcGIS Services Directory. Ex. https://gisrevprxy.seattle.gov/ArcGIS/rest/services/ext/WM_CityGISLayers/MapServer/33
3. Under "Where" enter "1=1" (or whatever more specific query you want for your export)
4. Under "Format" select "JSON"
5. If you want all the feature service attributes be sure to add '*' to the Output Fields. The Esri Json reader will pick these up
automatically
6. Click the "Query (GET)" button
7. Then copy the URL from your browser's URL bar


## Update workflow to point to your Esri-JSON URL

Follow the steps below to get the example workflow working to create a new dataset on your data portal.

1. [Download the workflow](https://github.com/socrata/connectors/raw/master/ArcGIS%20Server/ArcGIS%20Server2Socrata.fmwt) and open it in FME Desktop.

2. Input the URL obtained using the steps above by editing the 'Esri-JSON File or URL' under `query?where1=...` in the Navigator panel in the upper left of FME workbench.

3. Update your Socrata credentials for the Socrata Writer by editing the following under the Socrata writer (look for `soda.demo.socrata.com [Socrata]`) in the Navigator panel:
    - Host (e.g. data.seattle.gov)
    - User
    - Password

4. Run the workflow and ensure a new dataset was created on your domain.
