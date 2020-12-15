gcloud functions deploy env_vars --runtime python37 --set-env-vars FOO=bar --trigger-http

#note the below will not work as they are not setting GCP_PROJECT env variable in python38
#gcloud functions deploy env_vars --runtime python38 --set-env-vars FOO=bar --trigger-http
