steps to setup docker desktop with airflow
==========================================

step-1: download docker desktop
downloaded the latest version of docker desktop for windows 11 
start -> open docker desktop [ it start the app ]

step-2: create materials folder
create a folder called materials under documents as below:
C:\Users\Pradeep\Documents\materials

step-3: visual studio
C:\Users\Pradeep\Documents\materials> code .

step-4: docker compose step
download the docker-compose yaml file from the website here 
https://airflow.apache.org/docs/apache-airflow/2.4.2/docker-compose.yaml into C:\Users\Pradeep\Documents\materials
see Fig-1 in the document

step-5: .env file
create a .env file and put below contentes 

AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
AIRFLOW_UID=50000

see Fig-2


step-6: run the below cmd in vs studio 
docker-compose up -d  [ to run in detatched mode ie background mode ]
see Fig-3 for output

step-7: run the command to see the containers running
docker-compose ps 

for output see Fig-4


step-8: launch airflow ui
go to browser and launch airflow ui localhost:8080

for output see Fig-5




