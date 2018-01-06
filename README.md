SDSU Rocket Project DAQ Client
=================================
Software Repository for SDSU Rocket Project Avionics. DAQ software package is responsible for data acquisition and command/control of the vehicle. 
## Software Structure
### Test Stand Configuration
* Sensor Array/MQTT Broker
* Data Visualization Client
* Command Client
### Flight Configuration
* Sensor Array
* MQTT Broker
* Data Visualization Client
* Command Client
(see below for descriptions...)
## Sensor Array
* Pressure Transducers
* Igniter State
* Valve State
* GPS/IMU Data
* Load Cell Data
* Thermocouple Data
* TVC Position Feedback

## MQTT Broker
* Mosquitto MQTT Broker <https://github.com/eclipse/mosquitto>
* Pipline for DataACQ -> Broker -> Data Visualization Client
* Pipeline for Command Client -> Broker -> Rocket/TestStand
### Broker Topics
Topic Name | Topic Description
---------- | -----------
1 | Valve States
2 | Valve Command
3 | Transducer Data/Thermocouple Data
4 | Load Cell/GPS/IMU/TVC Position Feedback
5 | Safe/Alert/Panic/Launch
## Data Visualization Client
* Receives sensor data from broker
* Relay Panel
* Pressure/Temperature Panel
* TVC/Load Cell Panel
* GPS Panel
* Panic Button
## Command Client
* Igniter Control
* Valve Control
* Abort Control
* Panic Button