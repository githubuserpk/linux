#===================
# S E T U P
#===================
#install the python pubsub module

# step-1: upgrade and install pubsub module

pip install --upgrade google-cloud-pubsub
#now set the environment variable for project id
export GLOBAL_CLOUD_PROJECT=intense-cortex-278011

#step-2 list and see if there are any topics created
python publisher.py $GLOBAL_CLOUD_PROJECT list

#step-3: export project id
export GLOBAL_CLOUD_PROJECT=intense-cortex-278011


# =========================
# P U B L I S H E R - T O P I C 
# =========================
#step-4: create topic
python publisher.py $GLOBAL_CLOUD_PROJECT create p-MyTopic

#step-6: list topics
python publisher.py $GLOBAL_CLOUD_PROJECT list

# output:

# =========================
# S U B S C R I P T I O N
# =========================
#step-7: create subscription
python subscriber.py $GLOBAL_CLOUD_PROJECT create MyTopic p-MySub


#step-8
# ================================
# P U B L I S H   M E S S A G E S
# ================================

gcloud pubsub topics publish p-MyTopic --message "Hello"
gcloud pubsub topics publish p-MyTopic --message "Publisher's name is pk"
gcloud pubsub topics publish p-MyTopic --message "Publisher likes to eat pizza"

#step-9 receive messages
python subscriber.py $GLOBAL_CLOUD_PROJECT receive p-MySub

