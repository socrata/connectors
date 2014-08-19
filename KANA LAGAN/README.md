These notes are rough but they're a start

## Goal

        Ticket ID (string)
        Category/type (string)
        Description (string)
        Location: Address (string)
        Location: City (string)
        Location: State (list)
        Location: Zip (int)
        neighborhood_district: 
        Ticket created (date/time)
        Ticket last updated (date/time)
        Ticket closed (date/time)
        Status (string)
        Image (URL)

## Mapping

        Ticket ID (string) - FLODS_CASE_ENQUIRY_D00.CASE_REFERENCE
        Category/type (string) - LGNEF_EFORMINSTANCEVERSION.FORMNAME
        Description (string) - FLODS_CASE_ENQUIRY_D00.OTHER_DESCRIPTION or TITLE
        Location: Address (string) - FLODS_CASE_ENQUIRY_D00.OBJECT_DESCRIPTION (parsed)
        Location: City (string) - FLODS_CASE_ENQUIRY_D00.OBJECT_DESCRIPTION (parsed)
        Location: State (list) - FLODS_CASE_ENQUIRY_D00.OBJECT_DESCRIPTION (parsed)
        Location: Zip (int) - FLODS_CASE_ENQUIRY_D00.OBJECT_DESCRIPTION (parsed)
        Location: Latitude (double) - FLODS_CASE_ENQUIRY_D00.Y_COORD (Will need to be reprojected)
        Location: Longitude (double) - FLODS_CASE_ENQUIRY_D00.X_COORD (Will need to be reprojected)
        Location: Neighborhood (string) - 
        Ticket created (date/time) - FLODS_CASE_ENQUIRY_D00.CREATED_DT
        Ticket last updated (date/time) - FLODS_CASE_ENQUIRY_D00.LAST_MODIFIED_DT
        Ticket closed (date/time) - FLODS_CASE_ENQUIRY_D00.CLOSED_DT
        Status (string) - FLODS_CASE_ENQUIRY_D00.STATUS
        Image (URL)

## Sample Query

        SELECT TOP 100
          FCED.CASE_REFERENCE AS ticket_id,
          LEFIV.FORMNAME AS category,
          FCED.OTHER_DESCRIPTION AS description,
          FCED.OBJECT_DESCRIPTION AS object,  
          FCED.X_COORD AS x_coord,
          FCED.Y_COORD AS y_coord,
          FCED.CREATED_DT AS created_at,
          FCED.LAST_MODIFIED_DT AS last_modified_at,
          FCED.CLOSED_DT AS closed_at,
          FCED.STATUS AS status
        FROM 
          FLODS_CASE_ENQUIRY_D00 FCED,
          LGNEF_EFORMINSTANCEVERSION LEFIV
        WHERE
          LEFIV.CASEID = FCED.LGNCC_ID 
          
        ORDER BY CREATED_DT DESC;
                  

