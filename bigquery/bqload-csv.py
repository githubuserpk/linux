#===================================================================================================================
# script to load csv file to bigquery table
# the source csv file is copied from the google documentation given below
# https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#bigquery-load-table-gcs-csv-create-python
# the .csv file is available in global gcs location: gs://cloud-samples-data/bigquery/us-states/us-states.csv
# First 5 lines in the input file is

# name,post_abbr
# Alabama,AL
# Alaska,AK
# Arizona,AZ
# Arkansas,AR

#===================================================================================================================

from google.cloud import bigquery
client = bigquery.Client()
dataset_id = 'myapp_dev_datalake'

dataset_ref = client.dataset(dataset_id)
job_config = bigquery.LoadJobConfig()
job_config.schema = [
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("post_abbr", "STRING"),
]
job_config.skip_leading_rows = 1
# The source format defaults to CSV, so the line below is optional.
job_config.source_format = bigquery.SourceFormat.CSV
uri = "gs://myapp-dev-bucket-processed/us-states.csv"

load_job = client.load_table_from_uri(
    uri, dataset_ref.table("us_states"), job_config=job_config
)  # API request
print("Starting job {}".format(load_job.job_id))

load_job.result()  # Waits for table load to complete.
print("Job finished.")

destination_table = client.get_table(dataset_ref.table("us_states"))
print("Loaded {} rows.".format(destination_table.num_rows))
