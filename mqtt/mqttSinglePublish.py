#!/usr/bin/python

## Publishes a single mqtt message
# example: python <PATH TO SCRIPT>/mqttSinglePublish.py -h <host> -u <user> -P <password> -t <topic> -m "I'm your content"

import sys
import getopt
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def on_publish(mqttc, userdata, mid):
    print("Message sent to topic")

def print_usage():
    print("mqttSinglePublish.py [-d] [-h hostname] [-i clientid] [-p port] [-u username [-P password]] [-r retain] [-t topic] -m message")

def main(argv):
    debug = False
    host = "localhost"
    client_id = None
    port = 1883
    password = None
    topic = None
    message = None
    username = None
    verbose = False
    retain = True

    try:
        opts, args = getopt.getopt(argv, "dh:i:p:u:P:r:t:m:", ["debug", "host", "id", "port", "username", "password", "retain", "topic", "message"])
    except getopt.GetoptError as s:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d", "--debug"):
            debug = True
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-i", "--id"):
            client_id = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-P", "--password"):
            password = arg
        elif opt in ("-r", "--retain"):
            retain = arg
        elif opt in ("-t", "--topic"):
            topic = arg
            if debug:
                print("received topic arg:")
                print(topic)
        elif opt in ("-m", "--message"):
            message = arg
            if debug:
                print("received message arg:")
                print(message)
        elif opt in ("-u", "--username"):
            username = arg

    if topic == None:
        print("You must provide a topic.\n")
        print_usage()
        sys.exit(2)
    if message == None:
        print("You must provide a message.")
        print_usage()
        sys.exit(2)
    if debug:
        print("Sending a single message to\nTopic:")
        print(topic)
    publish.single(topic, message, hostname=host, retain=retain, port=port, client_id=client_id, keepalive=60, auth={'username':username , 'password':password})

if __name__ == "__main__":
    main(sys.argv[1:])
