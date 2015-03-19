# Creating a LAGAN to Socrata Transformation Using FME

## *A Workflow for Delivering Data to the Socrata 311 Explorer*

# Introduction

The purpose of this document is to provide instructions to the New Orleans 311 team on how to access, use, and maintain FME, a data transformation app that is **currently installed on the SCRIPTS server**. The primary section of this report,  "Creating a SQL Server to Socrata Transformation"  provides instructions on how to pull 311 data from the LAGAN reporting server and push it to the New Orleans Socrata data portal at data.nola.gov in order to feed the data to the 311 Explorer application. The diagram below illustrates this workflow.

![Transformation workflow](image_0.jpg)

## Installation

The City of New Orlean's FME serial number is: ****-****-**** 

The latest production release of FME Desktop can be downloaded from: [http://downloads.safe.com/fme/fme_install.msi](http://downloads.safe.com/fme/fme_install.msi) 

Installation and licensing instruction can be viewed at: [http://docs.safe.com/fme/pdf/FMEInstallationLicensing.pdf](http://docs.safe.com/fme/pdf/FMEInstallationLicensing.pdf) (Chapter 3 for fixed licenses) 

**Important installation note: **In a windows environment, FME should be installed to the root directory of the C drive (C:\FME). If there are any spaces in the program’s file path, then FME’s "Socrata Writer" will not behave properly. 

## Support

Support contact: [codes@safe.com](mailto:codes@safe.com). 

# Creating a SQL Server to Socrata Transformation 

These instructions describe how to pull 311 data from the LAGAN reporting server and push it to the New Orleans Socrata data portal at data.nola.gov. 

## STEP 1: Create a SQL Server Reader

*A SQL Server "reader" extracts data from a SQL Server database in order to transform it to another format. In this case, we will create a reader to extract data from the 311 LaganPDM database.   *

1. Open FME Workbench.

2. Choose to start a new blank workspace.

3. Click the "Add Reader" button in the toolbar. ![Add Reader Button](image_1.png)

4. An "Add Reader" widget will appear. In the “Format” field, type “Microsoft SQL Server Non-spatial” and select it. 

5. Click the "Parameters" button and enter the appropriate SQL Server credentials.

1. In the "Server" field, enter “**SERVER**”.

2. In the "Database" field, enter “**LaganPDM**”.

3. Username: **USERNAME**

4. Password: **PASSWORD** 

5. Click the dialogue button next to the "Table List" field and select the table that you would like to write to Socrata. The table used in the first iteration of this transformation is “**nola_case_view_total**”.

6. Click OK.

## STEP 2: Create a Tester to Remove "Unknown" Values from XY Fields

*In order for the data to process correctly on Socrata, it is necessary to remove all records that contain the value "Unknown" in either their X or Y column. This section describes how to create a “Tester” that will evaluate all records and remove those that contain this attribute. *

1. Search the FME "Transformer Gallery" for “Tester”. Double click on the “Tester” entry in the gallery and it will appear in your workspace. 

2. In order to connect the reader to the transformer, click and hold the green arrow on the right side of the reader and drag it to the red arrow on the left side of the tester. Both arrows should become green with a black line connecting them. **This is how you will connect all the transformers in your workflow.  **

3. Double click the gear icon on the transformer to bring up its parameters.

4. Select "All Tests (AND)" from the “Pass Criteria” drop-down field. 

5. Click the first blank cell in the "Left Value" column beneath “Test Clauses”. A drop-down icon will appear. Click “Attribute Value…”, select ‘LOCATION_X” from the attribute list that appears, and click OK. 

6. Repeat step 4 in the next row, replacing ‘LOCATION_X’ with ‘LOCATION_Y’

## STEP 3: Create an Attribute Projector to Convert LAGAN Data to Lat/Long

*The data in LAGAN is stored in the Louisiana State Plane 1983 South projection system (LA83-SF-MOD). It must be converted to a lat/long coordinate system in order to Socrata to consume it. *

1. Search the FME "Transformer Gallery" for the “Attribute Reprojector”. Double click on the “Tester” entry in the gallery and it will appear in your workspace. Connect the tester to the attribute reprojector, as described in step 2 of the section above. 

2. Double click on the transformer widget inside of the main workbench window to bring up the parameters. Select "LOCATION_X" from the list of fields in the “X Attribute” drop-down menu and “LOCATION_Y” for the “Y Attribute” dropdown.

3. For "Source Coordinate System", click the ellipses button next to the drop down menu. Search for and select “LA83-SF-MOD”.

4. For "Destination Coordinate System", search for “EPSG:4326”.

## STEP 4: Create an AttributeValueMapper to Replace \<null\> Values with 0

*Many coordinate values in LAGAN are not populated, which defaults to a value of "\<null\>". Socrata requires a value in order to process the data. *

1. Search the FME "Transformer Gallery" for the “AttributeValueMapper”. Connect this transformer to the AttributeReprojector. 

2. Double click on the "AttributeValueMapper" entry in the gallery and it will appear in your workspace.

3. Double click on the transformer to bring up the parameters.     Select "LOCATION_X" from the “Source Attribute” drop-down menu. 

4. In the first entry of the "Source Value" column, type ”\<null\>”.

5. On the same row, in the "Destination Value" column, enter the number 0.

## STEP 5: Create a StringConcatenator to Concatenate the XY Values into a Single Field

*Socrata requires a single location column with the format (Long, Lat). This transformer will create this column.*

1. Search the FME "Transformer Gallery" for the “SringConcatenator”. Double click on the “StringConcatenator” entry in the gallery and it will appear in your workspace. Connect it to the AttributeValueMapper. 

2. Open the parameters window. In the "Destination Attribute" field, type “location”. This will be the name of the column that gets created. 

3. Navigate to the "String Parts" window. In the left column of the first row, under “String Type”, select “Constant”. Type an open parenthesis into the right column, below “String Value”.

4. In the following row, select "Attribute Value" for “String Type”. In the drop-down menu beneath “String Value”, select “LOCATION_Y”.

5. Create another constant beneath this and enter a comma as the string value.

6. Next, create another attribute value. Select "LOCATION_X" from the drop-down menu. 

7. Last, create a constant that contains a closing parenthesis. Click ok to complete this setup. 

## STEP 6: Create a Socrata Writer 

*The Socrata Writer will be used to push LaganPDM data to data.nola.gov. *

1. Click the "Writer" button, which is located to the right of the “Reader” button, and resembles the reader button except that the green arrow is to the left of the icon and the icon is a shade lighter. Connect the writer to the StringConcatenator. 

2. An "Add Writer" widget will appear. In the “Format” field, type “Socrata” and select the Socrata option when it appears/ 

3. In the "Dataset" field, type “data.nola.gov”.

4. Click "Parameters" and enter your data.nola.gov username and password.

5. After clicking ok, you will be given the option to add a new feature type to the writer. Click "Yes".  If you are creating a new dataset, then add a unique name for the dataset here. If you are modifying an existing dataset, then enter the 4x4 Socarata identifier of the dataset here. 

6. If you plan on overwriting an existing dataset, navigate to the "Format Parameters" in the Feature Type Properties. Next to the “Truncate Dataset” field, select “Yes”. Next to the “Writer Mode” field, select “UPSERT”. Click OK. 

## STEP 7: Customize Data Output

*At this stage, we will be customizing the data output to reflect the data structure that the Socrata 311 Explorer expects to receive. This will involve renaming, eliminating, and changing the datatype of the fields in the table.  *

1. Start by expanding all the fields for both the StringConcatenator and the Socrata Writer by clicking the right-facing arrow inside of the respective transformer icons. We will be mapping the fields in the concatenator to those in the writer. Mapping fields in FME is similar to connecting transformers. You must drag the red arrow heads from the source fields to the fields in the downstream transformer that you’d like to inherit the source attributes. 

2. Right click on the Socrata Writer and click "Copy Attributes from Transformer". In the window that pops up, choose “StringConcatenator” and click OK. This will cause the writer to inherit all attributes from the StringConcatenator. 

3. From here, edit the Socrata field list to resemble the one below. Remove any fields that are not mentioned in this list. This is especially important for sensitive data, such as contact information of those reporting an issue. To delete a field, right click on the field name, and choose delete; to rename it, choose rename.

4. Right click on the field list in the Socrata Writer. Click "Properties" and navigate to the “User Attributes” tab. Next to the “location” field, click on the “type” cell and choose “location”. For the “zip_code” field, choose “number”.

<table>
  <tr>
    <td>LAGAN FIELD NAME</td>
    <td>SOCRATA FIELD NAME</td>
    <td>NOTES</td>
  </tr>
  <tr>
    <td>CASE_REFERENCE</td>
    <td>ticket_id</td>
    <td>none</td>
  </tr>
  <tr>
    <td>TYPE</td>
    <td>issue_type</td>
    <td>none</td>
  </tr>
  <tr>
    <td>OPEN_DT</td>
    <td>ticket_created_date_time</td>
    <td>none</td>
  </tr>
  <tr>
    <td>CLOSED_DT</td>
    <td>ticket_closed_date_time</td>
    <td>none</td>
  </tr>
  <tr>
    <td>CASE_STATUS</td>
    <td>ticket_status</td>
    <td>none</td>
  </tr>
  <tr>
    <td>CASE_DESCRIPTION</td>
    <td>issue_description</td>
    <td>none</td>
  </tr>
  <tr>
    <td>OBJECT_DESCRIPTION</td>
    <td>street_address</td>
    <td>none</td>
  </tr>
  <tr>
    <td>LOCATION_DISTRICT</td>
    <td>neighborhood_district</td>
    <td>none</td>
  </tr>
  <tr>
    <td>LOCATION_CITY</td>
    <td>city</td>
    <td>none</td>
  </tr>
  <tr>
    <td>LOCATION_STATE</td>
    <td>state</td>
    <td>none</td>
  </tr>
  <tr>
    <td>LOCATION_ZIPCODE</td>
    <td>zip_code</td>
    <td>Change type to "number" in the Feature Type Properties “Type” field. </td>
  </tr>
  <tr>
    <td>location</td>
    <td>location</td>
    <td>This field was created in Step 5. Change type to “location” in the Feature Type Properties “Type” field. </td>
  </tr>
  <tr>
    <td><none></td>
    <td>second_issue_type</td>
    <td>This field does not exist in LAGAN and will be created</td>
  </tr>
  <tr>
    <td><none></td>
    <td>image</td>
    <td>This field does not exist in LAGAN and will be created</td>
  </tr>
</table>


## STEP 8: Run Transformation

*With all transformers in place, the transformation should be ready to run. Click the green "play" button in the top toolbar. You will see a stream of information in the “log” tab in the bottom of the application window. If all goes well, the console will produce the message “Transformation was successful”. Point your browser to data.nola.gov, login in using your Socrata credentials, and search for the data set that you’ve created based on the feature type name or identifier that you’ve given it in step 5.6. *

# Appendix

## APPENDIX I: The Final Product

![Transformation Complete](image_2.png)

