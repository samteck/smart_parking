# smart_parking
A smart parking solution which tracks individual parking spot.
At each parking spot there are 2 LED's (Red and Green) which tell the availibity of the spot to the user who is searching for a spot and an IR sensor which will record the status of the spot for further processing. Every second the status of all the parking spot are send to a web server as a HTTP POST request in JSON format, which can be further consumed by our web app. 

![alt text](https://github.com/samteck/smart_parking/blob/master/Smart_Parking_DFD.jpg)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to have a raspberry Pi with Raspbian installed. We will be using Python3 for this project

### Installing

You need to install following libraries 

```
sudo pip3 install RPLCD     #to interface LCD (Hitachi HD44780)
sudo pip3 install requests  #to make http request
```


## Hardware Requirements

In this project we choose 5 parking spots for the initial phase and there will be one LCD display at the entrance to show number of free spots
Here is the list of Hardwares used

* Raspberry Pi with internet connection (Ethernet or Wifi)
* HD44780 LCD Diplay
* 5 IR sensors
* 5 Green LED's
* 5 Red LED's
* Breaboard
* 1K Potentiometer (for LCD contrast)
* Breadboard
* Plenty of Jumper Wires

### Interfacing the Hardware

Refer to below image to 

For Pin Numbers refer to the file /Config/GPIO_pins_config.txt

```
Image to be uploaded
```

### Testing the Hardwares

In the config folder use the files to check if hardware components are correctly interfaced

## Deployment

After all the hardware components are correctly working, you can check the internet connection by

```
ping www.google.com
```

and then proceed to run the main Driver_Code.py program to start the Edge application.

## Check the JSON requests 

This app will be integrated with a cloud platform to consume the JSON data. Meanwhile you can verify that your data is being send to the cloud by using the below url

```
https://webhook.site/
```

## Further Scope

We can use LDR sensors in place of IR sensor to reduce the cost.


