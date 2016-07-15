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

## Step 1: Install Required Packages

{% highlight r %}
install.packages('RODBC')
install.packages('RSocrata')
{% endhighlight %}

## Step 2: Connect to ODBC Database

Create constants so that R can access your database instance.

{% highlight r %}
ch <- odbcConnect("some dsn", uid = "user", pwd = "****")
{% endhighlight %}

## Step 3: Write to Your Data Frame

Use con to write to data.frame:

{% highlight r %}
res <- sqlFetch(ch, "table name")
{% endhighlight %}

## Step 4: Identify Destination Dataset

Ensure that you have a Socrata dataset with proper fields and proper datatypes to write to.  Capture the 4x4 ID for the dataset you want to publish to.  


## Step 5: Write Your Dataset

{% highlight r %}
socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "XXX@socrata.com")
socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "XXXXXXX")
datasetToAddToUrl <- "https://opendata.socrata.com/resource/evnp-32vr.json" 
write.socrata(table, datasetToAddToUrl, "UPSERT", socrataEmail, socrataPassword)
{% endhighlight %}

For full documentation on RODBC please see <https://cran.r-project.org/web/packages/RODBC/vignettes/RODBC.pdf>

