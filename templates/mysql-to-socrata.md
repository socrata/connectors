---
layout: listing
title: MySQL to Socrata
type: template-r

icon: fa-database

description: Reads data from a MySQL database, load data into R as a data.frame, then write to Socrata using RSocrata

github_url: https://github.com/rstats-db/rmysql
download_url: https://cran.r-project.org/web/packages/RMySQL/index.html
bugs_url: https://github.com/rstats-db/rmysql/issues
---

This walkthrough goes through the steps of taking data from a MySQL database using RMySQL and loading it into an existing Socrata table using `write.Socrata` from RSocrata

![View preview of workflow](/connectors/images/mysql.png)

This walkthrough assumes that you already have an instance of MySQL running on your machine.  If that is not the case please stop and install that before continuing.  

## Step 1: Install Packages

{% highlight r %}
install.packages('RMySQL')
install.packages('RSocrata')
{% endhighlight %}

## Step 2: Connect to MySQL instance

Create constants so that R can access MySQL instance 

{% highlight r %}
con <- dbConnect(MySQL(),
    user = 'mysql',
    password = 'YourPass',
    host = 'RDS Host',
    dbname='YourDB')
{% endhighlight %}

## Step 3: Write to Data Frame

Use `con` to write to data.frame 

{% highlight r %}
table <- dbWriteTable(conn = con, name = 'Test')
{% endhighlight %}

## Step 4: Identify Destination Dataset

Ensure that you have a Socrata dataset with proper fields and proper datatypes to write to.  Capture the 4x4 ID for the dataset you want to publish to.  

## Step 5: Publish to Your Dataset

{% highlight r %}
socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "XXX@socrata.com")
socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "XXXXXXX")
datasetToAddToUrl <- "https://opendata.socrata.com/resource/evnp-32vr.json" 
write.socrata(table,datasetToAddToUrl,"UPSERT",socrataEmail,socrataPassword)
{% endhighlight %}

## Step 6: Done!

Enjoy your new dataset!

