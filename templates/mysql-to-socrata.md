---
layout: listing
title: mySQL to Socrata
type: template-r

icon: fa-database

description: Reads data from a mySQL database, load data into R as a data.frame, then write to Socrata using RSocrata

github_url: https://github.com/rstats-db/rmysql
download_url: https://cran.r-project.org/web/packages/RMySQL/index.html
bugs_url: https://github.com/rstats-db/rmysql/issues
---
This walkthrough goes through the steps of taking data from a mySQL database using RmySQL and then loads that into an existing Socrata table using write.Socrata from RSocrata

![View preview of workflow](/connectors/images/mysql.png)

This walkthrough assumes that you already have an instance of MySql running on your machine.  If that is not the case please stop and install that before continuing.  

##Step 1

```install.packages('RMySQL')
   install.packages('RSocrata')```

##Step 2

create constants so that R can access mySQL instance 

```con <- dbConnect(MySQL(),
    user = 'mysql',
    password = 'YourPass',
    host = 'RDS Host',
    dbname='YourDB') ```

##Step 3 

use con to write to data.frame 
```table <- dbWriteTable(conn = con, name = 'Test')```

##Step 4 

ensure that you have a Socrata dataset with proper fields and proper datatypes to write to.  Capture the 4x4 for the dataset you want to publish to.  

##Step 5
```socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "XXX@socrata.com")
	socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "XXXXXXX")
	datasetToAddToUrl <- "https://opendata.socrata.com/resource/evnp-32vr.json" 
	write.socrata(table,datasetToAddToUrl,"UPSERT",socrataEmail,socrataPassword)
	```

##Step 6

Enjoy your new dataset.

