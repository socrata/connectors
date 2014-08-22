# ArcGIS Server to Socrata

This example workflow extracts data from ArcGIS Server and pushes it to Socrata.

## Steps to get your JSON URL

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

Then copy the URL fro your browser's URL bar
