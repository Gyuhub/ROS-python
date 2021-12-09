# ROS-python
BARAM ROS seminar KwangWoon University BARAM 2021 winter seminar Using python to adopt rospy

## Requirements
-----------
All you need is just ROS1(related packages which are installed automatically when installing ros-melodic-desktop-full such as rospy, roscpp, std_msgs ...)

## Contents
-----------
├─scripts
│   | client.py   
|   | listener.py   
|   | server.py   
|   └─talker.py   
├─srv   
|   | PythonTest.srv   
| CMakeLists.txt   
| README.md   
└─package.xml   

## Descriptions
### Codes in scripts/
1. client.py

'''
    When we use rospy to create service, the "client.py" takes a role of "client". So, it can request the service to server and receive the response.
    
    In this example, the "client" requests two integer numbers to server and waits for the sum of the two numbers. It will terminate automatically After receive   
    
    response.
'''

2. listener.py

'''
    When we use rospy to communicate with other nodes, the "listener.py" takes a role of "subscriber". In this example, the "subscriber" subscribes    
    
    the topic which
    
    has a name of "chatter", and calls back the string message to terminal like "I heard Something".
'''

3. server.py

'''
    When we use rospy to create service, the "server.py" takes a role of "server". So, it can reply the service from client.
  
    In this example, the "server" replies the sum of two numbers which is requested by the "client". It will not terminate while the user enter terminate signal   
  
    like "Ctrl+c"
'''

4. talker.py

'''
    When we use rospy to communicate with other nodes, the "talker.py" takes a role of "publisher". In this example, the "publisher" publishes the topic which   
  
    has a name of "chatter". the message of topic is "Hello world" + "server time".
'''
