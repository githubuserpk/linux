In this sample, we are going to encrypt a cloud storage file with CMEK keys.
High level steps:
=================
1. enable kms api from gcloud
2. create a key ring
3. create a key and add it to the key ring
4. use the key to encrypt a sample file
5. upload to cloud storage
6. download the file and decrypt using the key
