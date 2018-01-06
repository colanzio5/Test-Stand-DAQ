import time
import random
import math
import datetime
import paho.mqtt.client as mqtt


def packmessage():
    ret = str("{ \"time\": \"" + gettime() + "\", \"d1\": " + getd1() + ", \"d2\": " + getd2() + ", \"d3\": " + getd3() + ", \"v1\": \"" + getv1() + "\", \"v2\": \"" + getv2() + "\" }").encode()
    return ret

def mqtt_init():
    print("attempting new mqtt init...")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(host, 1883, 60)
    client.subscribe(valve_command_topic)
    client.subscribe(safe_abort_topic)
    print('client connected')
    return client

def echo_data():
    seed_data = time.time()
    random.seed(seed_data)
    
    #create fake valve states (randomly open small percentage of time)
    # layout -> [v0, v1, v2...v7]
    relays = 8 * [1]
    for relay in relays:
        relay = random.random() >= 0.80
    print(relays)

    #create fake pressure transducer and thermocouple data
    # layout -> [p0, p1, p2, p3, t0, t1, t2, t3...t9]
    sensors = 14 * [1]
    increment = 0
    for sensor in sensors:
        sensor = sin(increment + seed_data)
        increment += 0.25
    print(sensors)

    alerts = 

        

    



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    return rc

def on_disconnect(client, userdata,rc=0):
    print("Connection Lost. Attempting to reconnect...")
    client.loop_stop()
    client = mqtt_init()

def on_message(client, userdata, msg):
	parse_message(str(msg.payload))

def parse_message(message):
    print(message)

# OBJECTS #
# Topic Name | Topic Description
# 1 | Valve States  (publish)
# 2 | Valve Command (subscribe)
# 3 | Transducer Data/Thermocouple Data (publish)
# 4 | Load Cell/GPS/IMU/TVC Position Feedback (publish)
# 5 | Safe/Alert/Panic/Launch (publish/subscribe)
#       ...(0 - Safe, 1 - Alert, 2 - Panic, 3 - Abort, 4 - Launch)

SAFE_ALERT_PANIC_ABORT_LAUNCH = 0 
host = "192.168.1.132"	
valve_states_topic = "1"
valve_command_topic = "2"
data_sensors_topic = "3"
data_telemetry_topic = "4"
safe_abort_topic = "5"
client = mqtt_init()

# Begin Script
while True:




