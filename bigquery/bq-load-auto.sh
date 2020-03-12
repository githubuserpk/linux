Create a dataset called source_data and directly run below command to create a table called events and load data into it
bq load --autodetect $DEVSHELL_PROJ:source_data.events gs://cloud-training/gcpsec/labs/bq-authviews-source.csv
