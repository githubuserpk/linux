PROJECT_ID=pkdeltaai-06

gcloud config set project ${PROJECT_ID

curl  --http1.1 --header "Authorization: Bearer ${ACCESS_TOKEN}" https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/services
