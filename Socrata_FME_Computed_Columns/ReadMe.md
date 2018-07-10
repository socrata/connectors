## Writing to a Socrata Dataset with Computed Columns

When using the Socrata Writer to update an existing dataset that has computed columns, you may encounter a failure message that looks like this:

```Polling the job status: FAILURE: Processing TEMP.csv.sdiff.gz failed: Fields not in dataset: ":@computed_region_4b54_tmc4", ":@computed_region_p8tp_5dkv", ":@computed_region_4a3i_ccfj", ":@computed_region_kxmf_bzkv"```

Datasets that have location data that intersects a [Spatial Lens Boundary](https://support.socrata.com/hc/en-us/articles/212862177-Creating-Spatial-Lens-boundaries-for-region-mapping) will have computed columns. These columns are created and curated by the Socrata platform, not the user. They are used to perform the geographic join between the geocoded row and the underlying spatial lens polygon. The column names begin with the prefix `:@computed_region_`

These rows are hidden from default views of the dataset, so the Socrata user rarely interacts with them. However, when the Socrata Writer tries to write to a dataset with computed columns it tries to find them within the Socrata Writer’s payload, and they are not there.  

As a workaround, this FME workspace will use a [headless DataSync job](https://socrata.github.io/datasync/guides/setup-standard-job-headless.html) to update the existing dataset rather than the Socrata Writer. You will need to have DataSync [installed](https://github.com/socrata/datasync/releases) for this process. It can either be downloaded and installed, or you can use FME to find the version of DataSync you have installed within FME. To do so, run a different workspace with the Socrata Writer, and within the log, you will find the path to the .jar file. It will look something like `java -jar {path to datasync}/datasync.jar` This path can be used in the `DataSync_Path` published parameter.

Note: You will need to acquire the API field names for the columns in your dataset - you can access them by expanding the column descriptions on the dataset’s [Primer Page](https://support.socrata.com/hc/en-us/articles/221691947-Socrata-Primer-a-dataset-s-landing-page).
