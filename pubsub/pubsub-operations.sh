#create pubsub topic
gcloud pubsub topics create myTopic

#create another topic
gcloud pubsub topics create Test1

#list the topics
gcloud pubsub topics list

#delete topic
gcloud pubsub topics delete Test1

#============================================

#create a subscription
gcloud  pubsub subscriptions create --topic myTopic mySubscription

#you can also create more subscriptions
#gcloud  pubsub subscriptions create --topic myTopic mysub2
#gcloud  pubsub subscriptions create --topic myTopic mysub3

#list subscriptions
gcloud pubsub topics list-subscriptions myTopic


#publish message to the mytopic 
#mesg-1
gcloud pubsub topics publish myTopic --message "1. Hello pk"

#mesg-2
gcloud pubsub topics publish myTopic --message "2. customer wants to order a pizza"

#below command gets one message ie consumes one message out at a time
gcloud pubsub subscriptions pull mySubscription --auto-ack --limit=1

#mesg-3
gcloud pubsub topics publish myTopic --message "2. customer wants to order a pizza"
gcloud pubsub topics publish myTopic --message "3. order placed"
gcloud pubsub topics publish myTopic --message "4. order delivered"
gcloud pubsub topics publish myTopic --message "5. customer gave thumbs up"

#below command outputs 3 messages at a time, ie consumes 3 messages at a time
gcloud pubsub subscriptions pull mySubscription --auto-ack --limit=3


# cleanup
#delete subscription
gcloud pubsub subscriptions delete mySubscription

#delete topic
gcloud pubsub topics delete myTopic




