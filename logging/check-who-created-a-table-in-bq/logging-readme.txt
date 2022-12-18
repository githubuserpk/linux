Steps:
Problem statement: 
I created a table called bqlogtable in bigquery and I want to find out who created it and when

In logging explorer, use the below filters and you can see the details in the log

resource.type="bigquery_dataset"
resource.labels.dataset_id="bqml"
logName="projects/kp-devops/logs/cloudaudit.googleapis.com%2Factivity"
protoPayload.resourceName="projects/kp-devops/datasets/bqml/tables/bqlogtable"
protoPayload.methodName: "google.cloud.bigquery.v2.TableService.InsertTable"
