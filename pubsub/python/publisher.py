# Reference url: https://cloud.google.com/pubsub/docs/quickstart-client-libraries
# In this example we publish 10 messages to an existing topic called myTopic
import os
from google.cloud import pubsub_v1

project_id =os.environ['PROJECT_ID']
print("project id: ", project_id)

# TODO(developer)
# project_id = "intense-cortex-278011"
topic_id = "myTopic"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 10):
    data = u"Message number {}".format(n)
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)
    print(future.result())

print("Published messages.")
