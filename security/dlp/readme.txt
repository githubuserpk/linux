1. create project id variable
>
export PROJECT_ID=[YOUR_PROJECT_ID]

2. create a owner service account
>
gcloud iam service-accounts create owner-sa \
  --display-name "Owner Service Account"

3. assign the role of owner to the owner-sa service account
>
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
--member serviceAccount:owner-sa@${PROJECT_ID}.iam.gserviceaccount.com \
--role roles/owner

4. create the json key file
> 
--create service account key 
gcloud iam service-accounts keys create ~/owner-sa.json \
--iam-account owner-sa@${PROJECT_ID}.iam.gserviceaccount.com

5. activate the service account
gcloud auth activate-service-account --key-file=key.json

6. get the ACCESS_TOKEN value 
> 
gcloud auth print-access-token

7. create a file called deid.json


8. invoke the dlp api, replace ACCESS_TOKEN with the token obtained in above step
> 
curl -s \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  https://dlp.googleapis.com/v2/projects/$PROJECT_ID/content:inspect \
  -d @deid.json

#9. run the script to re-identify the data, replace the access token value 
#Note: in reid.json replace the value of phone number you got when you ran the de-identify step
#For eg: in deid.json if your phone no is 12345 and the deidentified value is 56789, then use the value 56789 in reid.json to get decoded properly

curl -s \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  https://dlp.googleapis.com/v2/projects/$PROJECT_ID/content:inspect \
  -d @reid.json

