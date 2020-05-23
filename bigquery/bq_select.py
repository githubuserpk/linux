#reference: https://pypi.org/project/google-cloud-bigquery/

import os
from google.cloud import bigquery

# Set this to the path to your credentials file
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = 'myapp-dev-owner-sa.json'


def main():
    # Instantiate a Google BigQuery client
    client = bigquery.Client()

    # Create a query job
    query_job = client.query("""
        SELECT 1 AS result""")

    # Run the query and retrieve results
    results = query_job.result()

    for row in results:
        print(row.result)


if __name__ == '__main__':
    main()
