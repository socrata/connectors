---
layout: listing
title: Salesforce to Socrata
type: template-r

icon: fa-cloud

description: Reads data from Salesforce instance via API, load data into R as a data.frame, then write to Socrata using RSocrata

github_url: https://github.com/hiratake55/RForcecom
download_url: https://cran.r-project.org/web/packages/RForcecom/index.html
bugs_url: https://github.com/hiratake55/RForcecom/issues
---

This walkthrough goes through the steps of taking data from Salesforce and then loads that into an existing Socrata table using write. Rforcecom Example from [Takekatsu Hiramura](https://hiratake55.wordpress.com/2013/03/28/rforcecom/)

## Step 1: Install Required Dependencies

{% highlight r %}
install.packages("RForcecom")
library(RForcecom)
{% endhighlight %}

## Step 2: Log into Salesforce

To sign in to the Salesforce.com, use `rforcecom.login()` function

{% highlight r %}
username <- "yourname@yourcompany.com"
password <- "YourPasswordSECURITY_TOKEN"
instanceURL <- "https://na14.salesforce.com/"
apiVersion <- "26.0"
(session <- rforcecom.login(username, password, instanceURL, apiVersion))
{% endhighlight %}

## Step 3: Query Salesforce

Make a query using Salesforce Query language (SOQL), not to be confused with the Socrata Query Language (SoQL)..

{% highlight r %}
soqlQuery <- "SELECT Id, Name, Phone FROM Account WHERE AnnualRevenue > 50000 LIMIT 5"
rforcecom.query(session, soqlQuery)
{% endhighlight %}

## Step 4: Identify Destination Dataset

Ensure that you have a Socrata dataset with proper fields and proper datatypes to write to.  Capture the 4x4 ID for the dataset you want to publish to.  

## Step 5: Write to Your Dataset

{% highlight r %}
socrataEmail <- Sys.getenv("SOCRATA_EMAIL", "XXX@socrata.com")
socrataPassword <- Sys.getenv("SOCRATA_PASSWORD", "XXXXXXX")
datasetToAddToUrl <- "https://opendata.socrata.com/resource/evnp-32vr.json" 
write.socrata(table, datasetToAddToUrl, "UPSERT", socrataEmail, socrataPassword)
{% endhighlight %}

For full documentation on Rforcecom please see <http://rforcecom.plavox.info/>.

