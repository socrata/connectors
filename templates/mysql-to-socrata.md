---
layout: listing
title: mySql to Socrata
type: template-fme

icon: fa-icon

description: Reads data from mysql database and loads into an R data.frame. Then uses RSocrata and write.Socrata to load. 

github_url: https://github.com/rstats-db/rmysql
download_url: https://github.com/rstats-db/rmysql
bugs_url: https://github.com/rstats-db/rmysql/issues
---

This is courtesy of the Rstats-db project on github. These are the constants that you will need in order to connect to the MySql database. 

```con <- dbConnect(MySQL(),
    user = 'RDSUser',
    password = 'YourPass',
    host = 'RDS Host',
    dbname='YourDB')
```
dbReadTable takes the constants that you just fed it and then a name of the table to load the table in as a dataframe 

```testDataFrame <- dbReadTable(conn = con,name = 'Test'), title = "9 variables from Thurstone")```

![Mysql table](/images/mysqldb.png)

Then use write.Socrata from Rsocrata to load the data.frame into A Socrata table. 
```# Store user email and password
socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "XXX@socrata.com")
socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "XXXXXXX")

datasetToAddToUrl <- "https://opendata.socrata.com/resource/evnp-32vr.json" # dataset

write.socrata(testDataFrame,datasetToAddToUrl,"UPSERT",socrataEmail,socrataPassword)```


