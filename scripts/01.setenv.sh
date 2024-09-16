#create this file in your gcloud home directory ie ~ or do cd ~
export GOOGLE_PROJECT=$(gcloud config get-value project)
export GOOGLE_PROJECT=$(gcloud config get-value project)
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
export PROJECT_ID=$(gcloud config get-value project)
alias python=python3
alias pip=pip3

export GOOGLE_APPLICATION_CREDENTIALS=~/owner-sa.json

export USER_ACCOUNT=$(gcloud config get-value account)


#Add this file to .bashrc file 
vi ~/.bashrc and 

add below line in the end 
source ~/setenv.sh
