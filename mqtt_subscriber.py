import paho.mqtt.client as mqtt
import time

##### Publisher #####
# Creating client
client = mqtt.Client()

# Connecting to Broker
client.connect('139.59.4.199', 1883)

# Looping Forever
packet_count = 0

# while True:
#     packet_count += 1
#     print('Sending message', packet_count)
#     client.publish('/test', 'ON')
#     time.sleep(1)

##### Subscriber #####

def on_message(client, userdata, message):
    raw_message = str(message.payload.decode("utf-8"))
    topic = message.topic

    print(int(time.time()), 'Received', topic, raw_message)


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribe Succeed")


def on_connect(client, userdata, flags, rc):
    print("Broker is connected")
    client.subscribe('/test')


# Configuring Callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe


client.loop_forever()
