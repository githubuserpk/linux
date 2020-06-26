In this lab, we use the GCS as the storage layer for Hadoop cluster
truly separating the 
STORAGE 
and
COMPUTE 

This is an example of using Ephemeral Cluster 
Once the job is completed, the cluster will be deleted.

Steps:
=====
1. create a hadoop cluster 
2. copy a sample file to GCS cloud storage.
3. run Spark job by using the file on cloud storage.
4. spark job writes output to the /output folder in the bucket
5. delete cluster and bucket sub-folders.

