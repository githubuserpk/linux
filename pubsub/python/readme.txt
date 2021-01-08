#===================
# S E T U P
#===================
#install the python pubsub module

# step-1: upgrade and install pubsub module
# This is done as part of setup scripts, ignore the step
pip install --upgrade google-cloud-pubsub

#better still do the below
pip3 install --upgrade google-cloud-pubsub

#now set the environment variable for project id
# This is done as part of setup scripts ignore the step
export GLOBAL_CLOUD_PROJECT=intense-cortex-278011

# =========================
# P U B L I S H E R - T O P I C 
# =========================
#step-2: create topic
we will use the previously created topic myTopic

# output:

# =========================
# S U B S C R I P T I O N
# =========================
#step-3: create subscription
we will use the previously created subscription mySubscription

#step-3 publish mesg
# ================================
# P U B L I S H   M E S S A G E S
# ================================

python publisher.py 

#step-4 receive mesg
# ================================
# R E C E I V E   M E S S A G E S
# ================================
python subscriber.py

