#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to perform basic operations on
subscriptions with the Cloud Pub/Sub API.

For more information, see the README.md under /pubsub and the documentation
at https://cloud.google.com/pubsub/docs.
"""

import argparse


def list_subscriptions_in_topic(project_id, topic_name):
    """Lists all subscriptions for a given topic."""
    # [START pubsub_list_topic_subscriptions]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # topic_name = "your-topic-id"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    for subscription in publisher.list_topic_subscriptions(topic_path):
        print(subscription)
    # [END pubsub_list_topic_subscriptions]


def list_subscriptions_in_project(project_id):
    """Lists all subscriptions in the current project."""
    # [START pubsub_list_subscriptions]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"

    subscriber = pubsub_v1.SubscriberClient()
    project_path = subscriber.project_path(project_id)

    for subscription in subscriber.list_subscriptions(project_path):
        print(subscription.name)

    subscriber.close()
    # [END pubsub_list_subscriptions]


def create_subscription(project_id, topic_name, subscription_name):
    """Create a new pull subscription on the given topic."""
    # [START pubsub_create_pull_subscription]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # topic_name = "your-topic-id"
    # subscription_name = "your-subscription-id"

    subscriber = pubsub_v1.SubscriberClient()
    topic_path = subscriber.topic_path(project_id, topic_name)
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    subscription = subscriber.create_subscription(subscription_path, topic_path)

    print("Subscription created: {}".format(subscription))

    subscriber.close()
    # [END pubsub_create_pull_subscription]


def create_subscription_with_dead_letter_topic(
    project_id, topic_name, subscription_name, dead_letter_topic_name
):
    """Create a subscription with dead letter policy."""

def create_push_subscription(project_id, topic_name, subscription_name, endpoint):
    """Create a new push subscription on the given topic."""

def delete_subscription(project_id, subscription_name):
    """Deletes an existing Pub/Sub topic."""
    # [START pubsub_delete_subscription]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_name = "your-subscription-id"

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    subscriber.delete_subscription(subscription_path)

    print("Subscription deleted: {}".format(subscription_path))

    subscriber.close()
    # [END pubsub_delete_subscription]


def update_push_subscription(project_id, topic_name, subscription_name, endpoint):
    """
    Updates an existing Pub/Sub subscription's push endpoint URL.
    Note that certain properties of a subscription, such as
    its topic, are not modifiable.
    """

def update_subscription_with_dead_letter_policy(
    project_id, topic_name, subscription_name, dead_letter_topic_name
):
    """Update a subscription's dead letter policy."""


def remove_dead_letter_policy(project_id, topic_name, subscription_name):
    """Remove dead letter policy from a subscription."""

def receive_messages(project_id, subscription_name, timeout=None):
    """Receives messages from a pull subscription."""
    # [START pubsub_subscriber_async_pull]
    # [START pubsub_quickstart_subscriber]
    from concurrent.futures import TimeoutError
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_name = "your-subscription-id"
    # Number of seconds the subscriber should listen for messages
    # timeout = 5.0

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        print("Received message: {}".format(message))
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print("Listening for messages on {}..\n".format(subscription_path))

    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()
    # [END pubsub_subscriber_async_pull]
    # [END pubsub_quickstart_subscriber]


def receive_messages_with_custom_attributes(
    project_id, subscription_name, timeout=None
):
    """Receives messages from a pull subscription."""


def receive_messages_with_flow_control(project_id, subscription_name, timeout=None):
    """Receives messages from a pull subscription with flow control."""


def synchronous_pull(project_id, subscription_name):
    """Pulling messages synchronously."""

def synchronous_pull_with_lease_management(project_id, subscription_name):
    """blank implementation"""

def listen_for_errors(project_id, subscription_name, timeout=None):


def receive_messages_with_delivery_attempts(
    project_id, subscription_name, timeout=None
):
    """blank """


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Your Google Cloud project ID")

    subparsers = parser.add_subparsers(dest="command")
    list_in_topic_parser = subparsers.add_parser(
        "list-in-topic", help=list_subscriptions_in_topic.__doc__
    )
    list_in_topic_parser.add_argument("topic_name")

    list_in_project_parser = subparsers.add_parser(
        "list-in-project", help=list_subscriptions_in_project.__doc__
    )

    create_parser = subparsers.add_parser("create", help=create_subscription.__doc__)
    create_parser.add_argument("topic_name")
    create_parser.add_argument("subscription_name")

    create_with_dead_letter_policy_parser = subparsers.add_parser(
        "create-with-dead-letter-policy",
        help=create_subscription_with_dead_letter_topic.__doc__,
    )
    create_with_dead_letter_policy_parser.add_argument("topic_name")
    create_with_dead_letter_policy_parser.add_argument("subscription_name")
    create_with_dead_letter_policy_parser.add_argument("dead_letter_topic_name")

    create_push_parser = subparsers.add_parser(
        "create-push", help=create_push_subscription.__doc__
    )
    create_push_parser.add_argument("topic_name")
    create_push_parser.add_argument("subscription_name")
    create_push_parser.add_argument("endpoint")

    delete_parser = subparsers.add_parser("delete", help=delete_subscription.__doc__)
    delete_parser.add_argument("subscription_name")

    update_push_parser = subparsers.add_parser(
        "update-push", help=update_push_subscription.__doc__
    )
    update_push_parser.add_argument("topic_name")
    update_push_parser.add_argument("subscription_name")
    update_push_parser.add_argument("endpoint")

    update_dead_letter_policy_parser = subparsers.add_parser(
        "update-dead-letter-policy",
        help=update_subscription_with_dead_letter_policy.__doc__,
    )
    update_dead_letter_policy_parser.add_argument("topic_name")
    update_dead_letter_policy_parser.add_argument("subscription_name")
    update_dead_letter_policy_parser.add_argument("dead_letter_topic_name")

    remove_dead_letter_policy_parser = subparsers.add_parser(
        "remove-dead-letter-policy", help=remove_dead_letter_policy.__doc__
    )
    remove_dead_letter_policy_parser.add_argument("topic_name")
    remove_dead_letter_policy_parser.add_argument("subscription_name")

    receive_parser = subparsers.add_parser("receive", help=receive_messages.__doc__)
    receive_parser.add_argument("subscription_name")
    receive_parser.add_argument("--timeout", default=None, type=float)

    receive_with_custom_attributes_parser = subparsers.add_parser(
        "receive-custom-attributes",
        help=receive_messages_with_custom_attributes.__doc__,
    )
    receive_with_custom_attributes_parser.add_argument("subscription_name")
    receive_with_custom_attributes_parser.add_argument(
        "--timeout", default=None, type=float
    )

    receive_with_flow_control_parser = subparsers.add_parser(
        "receive-flow-control", help=receive_messages_with_flow_control.__doc__
    )
    receive_with_flow_control_parser.add_argument("subscription_name")
    receive_with_flow_control_parser.add_argument("--timeout", default=None, type=float)

    synchronous_pull_parser = subparsers.add_parser(
        "receive-synchronously", help=synchronous_pull.__doc__
    )
    synchronous_pull_parser.add_argument("subscription_name")

    synchronous_pull_with_lease_management_parser = subparsers.add_parser(
        "receive-synchronously-with-lease",
        help=synchronous_pull_with_lease_management.__doc__,
    )
    synchronous_pull_with_lease_management_parser.add_argument("subscription_name")

    listen_for_errors_parser = subparsers.add_parser(
        "listen-for-errors", help=listen_for_errors.__doc__
    )
    listen_for_errors_parser.add_argument("subscription_name")
    listen_for_errors_parser.add_argument("--timeout", default=None, type=float)

    receive_messages_with_delivery_attempts_parser = subparsers.add_parser(
        "receive-messages-with-delivery-attempts",
        help=receive_messages_with_delivery_attempts.__doc__,
    )
    receive_messages_with_delivery_attempts_parser.add_argument("subscription_name")
    receive_messages_with_delivery_attempts_parser.add_argument(
        "--timeout", default=None, type=float
    )

    args = parser.parse_args()

    if args.command == "list-in-topic":
        list_subscriptions_in_topic(args.project_id, args.topic_name)
    elif args.command == "list-in-project":
        list_subscriptions_in_project(args.project_id)
    elif args.command == "create":
        create_subscription(args.project_id, args.topic_name, args.subscription_name)
    elif args.command == "create-with-dead-letter-policy":
        create_subscription_with_dead_letter_topic(
            args.project_id,
            args.topic_name,
            args.subscription_name,
            args.dead_letter_topic_name,
        )
    elif args.command == "create-push":
        create_push_subscription(
            args.project_id, args.topic_name, args.subscription_name, args.endpoint,
        )
    elif args.command == "delete":
        delete_subscription(args.project_id, args.subscription_name)
    elif args.command == "update-push":
        update_push_subscription(
            args.project_id, args.topic_name, args.subscription_name, args.endpoint,
        )
    elif args.command == "update-dead-letter-policy":
        update_subscription_with_dead_letter_policy(
            args.project_id,
            args.topic_name,
            args.subscription_name,
            args.dead_letter_topic_name,
        )
    elif args.command == "remove-dead-letter-policy":
        remove_dead_letter_policy(
            args.project_id, args.topic_name, args.subscription_name
        )
    elif args.command == "receive":
        receive_messages(args.project_id, args.subscription_name, args.timeout)
    elif args.command == "receive-custom-attributes":
        receive_messages_with_custom_attributes(
            args.project_id, args.subscription_name, args.timeout
        )
    elif args.command == "receive-flow-control":
        receive_messages_with_flow_control(
            args.project_id, args.subscription_name, args.timeout
        )
    elif args.command == "receive-synchronously":
        synchronous_pull(args.project_id, args.subscription_name)
    elif args.command == "receive-synchronously-with-lease":
        synchronous_pull_with_lease_management(args.project_id, args.subscription_name)
    elif args.command == "listen-for-errors":
        listen_for_errors(args.project_id, args.subscription_name, args.timeout)
    elif args.command == "receive-messages-with-delivery-attempts":
        receive_messages_with_delivery_attempts(
            args.project_id, args.subscription_name, args.timeout
        )
