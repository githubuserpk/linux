# import statements
# This is a working sample the IAM roles assigned are:
# Data Catalog Admin
# Editor

import os
from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from google.cloud import datacatalog_v1


# Custom Python logic for derriving data value
yesterday = datetime.combine(datetime.today() - timedelta(1), datetime.min.time())

# Default arguments
default_args = {
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Python custom logic/function for python callables
def print_hello():
    print('Hey I am Python operator')



def create_taxonomy(
    # TODO(developer): Set project_id to the ID of the project the
    #  taxonomy will belong to.
    project_id: str = "kp-ccp",
    # TODO(developer): Specify the geographic location where the
    #  taxonomy should reside.
    location_id: str = "eu",
    # TODO(developer): Set the display name of the taxonomy.
    display_name: str = "pk-example-taxonomy-airflow",

):

    print("in create taxonomy")
    print("proj id: {}, location_id: {}, disp name: {}".format(project_id, location_id, display_name))

    # TODO(developer): Construct a Policy Tag Manager client object. To avoid
    # extra delays due to authentication, create a single client for your
    # program and share it across operations.
    client = datacatalog_v1.PolicyTagManagerClient()

    # Construct a full location path to be the parent of the taxonomy.
    parent = datacatalog_v1.PolicyTagManagerClient.common_location_path(
        project_id, location_id
    )

    # TODO(developer): Construct a full Taxonomy object to send to the API.
    taxonomy = datacatalog_v1.Taxonomy()
    taxonomy.display_name = display_name
    taxonomy.description = "This Taxonomy represents pk taxonomy for testing..."

    # Send the taxonomy to the API for creation.
    print("Creating taxonomy")
    taxonomy = client.create_taxonomy(parent=parent, taxonomy=taxonomy)
    print(f"Created taxonomy {taxonomy.name}")


    


# DAG definitions 
with DAG(dag_id='bq_catalog_airflow',
         catchup=False,
         schedule_interval=timedelta(days=1),
         default_args=default_args
         ) as dag:

    # Tasks starts here 



# Dummy strat task   
    start = DummyOperator(
        task_id='start',
        dag=dag,
    )

    # Python operator , task
    create_taxonomy = PythonOperator(
    task_id='create_taxonomy',
    python_callable=create_taxonomy,
    dag=dag)


# Dummy end task
end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Settting up task  dependency
start >> create_taxonomy >> end
