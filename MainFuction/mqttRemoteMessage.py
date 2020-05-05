import paho.mqtt.client as mqtt
import time 

def onConnect(client_name, host_name):
    """try to connect a broker and return a mqtt.client objection"""
    client = mqtt.Client(client_name)
    client.connect(host_name, 1883) 
    print('try to connect ',host_name)
    try:
        client.connect(host_name, 1883)
        print('connect successfully your client_name is ', client_name)
    except:
        print('wrong connection')
        return False
    return client

def toPublish(client, topic, message):
    """try to publish a message in a topiv"""
    print('try to publish message:', message, 'in ', topic)
    try:
        client.publish(topic, message)
        print('successfully publish a message')
    except:
        print('wrong publishment')

def toSubscribe(client, topic):
    try:
        client.subscribe(topic)
        print('successfully subscrive from ', topic)
    except:
        print('Wrong subscribtion')

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

        
if __name__ == "__main__":
    client_connection = onConnect('test_connect', 'test.mosquitto.org')
    client_subsribtion = onConnect('test_subscribton', 'test.mosquitto.org')
    client_connection.on_message = on_message   #attach function to callback
    client_subsribtion.on_message = on_message  #attach functon to callback
    client_connection.loop_start()
    client_subsribtion.loop_start()


    if client_subsribtion:
        toSubscribe(client_subsribtion, 'house/light')
    if client_connection:
        toPublish(client_connection, 'house/light', 'Hello World')
    time.sleep(4)
    client_connection.loop_stop()
    client_subsribtion.loop_stop()
    