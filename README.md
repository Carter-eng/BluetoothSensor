# BluetoothSensor

This is a testing system for the Adafruit nrf52840 Feather Sense Board.
The goal of this project is to create a system to recieve Bluetooth from the board,
specifically focusing on gyroscopic data, and publishing it to ROS.
There is an arduino handler made from an Arduino Uno Rev 3 and the Adafruit 
Bluefruit LE UART Friend. 

The code for these is adapted from the Adafruit examples for the libraries used. 
The Libraries and set up information are found here:
https://learn.adafruit.com/adafruit-feather-sense/overview
https://learn.adafruit.com/introducing-the-adafruit-bluefruit-le-uart-friend

Made for testing in the Boston University Robotics Lab
Wiring for the Arduino handler is shown below

![alt text](https://github.com/Carter-eng/BluetoothSensor/adafruit_products_UARTFriend_bb.png?raw=true)
