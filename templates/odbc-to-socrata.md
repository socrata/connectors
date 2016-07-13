---
layout: listing
title: ODBC to Socrata
type: template-r

icon: fa-database

description: Reads data over an ODBC connection, load data into R as a data.frame, then write to Socrata using RSocrata

github_url: https://cran.r-project.org/web/packages/RODBC/vignettes/RODBC.pdf
download_url: https://cran.r-project.org/web/packages/RODBC/vignettes/RODBC.pdf
bugs_url: 
---
This walkthrough goes through the steps of taking data from any system that uses ODBC and then loads that into an existing Socrata table using write.Socrata from RSocrata



  

##Step 1

```install.packages('RODBC')
   install.packages('RSocrata')```

##Step 2

create constants so that R can access mySQL instance 

```ch <- odbcConnect("some dsn", uid = "user", pwd = "****") ```

##Step 3 

use con to write to data.frame 
```res <- sqlFetch(ch, "table name")```

##Step 4 

ensure that you have a Socrata dataset with proper fields and proper datatypes to write to.  Capture the 4x4 for the dataset you want to publish to.  

##Step 5
```socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "XXX@socrata.com")
	socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "XXXXXXX")
	datasetToAddToUrl <- "https://opendata.socrata.com/resource/evnp-32vr.json" 
	write.socrata(table,datasetToAddToUrl,"UPSERT",socrataEmail,socrataPassword)
	```
For full documentation on RODBC please see https://cran.r-project.org/web/packages/RODBC/vignettes/RODBC.pdf

