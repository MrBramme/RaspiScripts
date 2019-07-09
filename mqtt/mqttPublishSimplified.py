# Simple script to send a message to an mqtt topic once there's internet
# required page.mqtt to be installed (use a venv: 'python3 -m venv venv')
# add this to crontab: '@reboot echo 'source /location/venv/bin/activate; python /location/main.py' | /bin/bash'
# this script will run on each reboot sending a message to a topic whenever there's internet.

import socket
import time
import paho.mqtt.publish as publish

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def main():
    while not is_connected():
        print("not yet online")
        time.sleep(1)
    username = "user"
    password = "pass"
    host = "host"
    topic = "devices/devicename/ip"
    clientid = "myclient"

    ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

    message = "%s : My ip is " % time.ctime()
    message = message + ip
    publish.single(topic, message, hostname=host, retain=True, port=1883, client_id=clientid, keepalive=60, auth={'username':username , 'password':password})

if __name__ == "__main__":
    main()
