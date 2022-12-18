url: qwiklabs url is here: https://www.cloudskillsboost.google/focuses/6100?parent=catalog


create a dataset called bq_logs 

in sql workspace run below query: 
> SELECT current_date

In logs explorer -> search for Bigquery -> look of "jobcompleted"
right click and click "show matching results"

Sink:
=====
create a new sink 
sink service: select Bigquery
select dataset name: bq_logs 
click: create sink

create the view v_querylogs and visualize the data in bigquery

viewname: v_querylogs
see file: v_query_logs_view.txt


