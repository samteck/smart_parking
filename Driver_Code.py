import RPi.GPIO as IO
import time
from RPLCD import CharLCD
import requests
import json

IO.setwarnings(False)
IO.setmode(IO.BCM)

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])

url = 'https://webhook.site/0acfa087-ffda-4424-9b9c-994c54ac218d'
#url = 'http://smartparkingbackend.us-west-2.elasticbeanstalk.com:8281/saveSlotStatus'

print("Started")

ir0 = 21
ir1 = 3
ir2 = 2
ir3 = 12
ir4 = 7

green0 = 16
green1 = 14
green2 = 18
green3 = 27
green4 = 23
red0   = 20
red1   = 4
red2   = 15
red3   = 17
red4   = 22

IO.setup(ir0,IO.IN)
IO.setup(ir1,IO.IN)
IO.setup(ir2,IO.IN)
IO.setup(ir3,IO.IN)
IO.setup(ir4,IO.IN)

IO.setup(green0,IO.OUT)
IO.setup(green1,IO.OUT)
IO.setup(green2,IO.OUT)
IO.setup(green3,IO.OUT)
IO.setup(green4,IO.OUT)
IO.setup(red0,IO.OUT)
IO.setup(red1,IO.OUT)
IO.setup(red2,IO.OUT)
IO.setup(red3,IO.OUT)
IO.setup(red4,IO.OUT)

lcd.clear()
lcd.write_string("Welcome to POC  ")
for i in range(16):
    lcd.write_string("#")
    time.sleep(0.2)
lcd.clear()


while 1 :
    
    occupiedSlot= []
    unoccupiedSlot = []
    
    print ("ir0 : " + str(IO.input(ir0)) + " ir1 : " + str(IO.input(ir1)) + " ir2 : " + str(IO.input(ir2)) + " ir3 : " + str(IO.input(ir3)) + " ir4 : " + str(IO.input(ir4)))
    
    #print(type(IO.input(ir0)))
    if (IO.input(ir0) == 0):
        IO.output(green0,IO.LOW)
        IO.output(red0,IO.HIGH)
        occupiedSlot.append(1001)
        #count -= 1
    if (IO.input(ir1) == 0):
        IO.output(green1,IO.LOW)
        IO.output(red1,IO.HIGH)
        occupiedSlot.append(1002)
        #count -= 1
    if (IO.input(ir2) == 0):
        IO.output(green2,IO.LOW)
        IO.output(red2,IO.HIGH)
        occupiedSlot.append(1003)
        #count -= 1
    if (IO.input(ir3) == 0):
        IO.output(green3,IO.LOW)
        IO.output(red3,IO.HIGH)
        occupiedSlot.append(1004)
        #count -= 1
    if (IO.input(ir4) == 0):
        IO.output(green4,IO.LOW)
        IO.output(red4,IO.HIGH)
        occupiedSlot.append(1005)
        #count -= 1
        
    count = 0
    
    if (IO.input(ir0) == 1):
        IO.output(green0,IO.HIGH)
        IO.output(red0,IO.LOW)
        count += 1
        unoccupiedSlot.append(1001)
    if (IO.input(ir1) == 1):
        IO.output(green1,IO.HIGH)
        IO.output(red1,IO.LOW)
        count += 1
        unoccupiedSlot.append(1002)
    if (IO.input(ir2) == 1):
        IO.output(green2,IO.HIGH)
        IO.output(red2,IO.LOW)
        count += 1
        unoccupiedSlot.append(1003)
    if (IO.input(ir3) == 1):
        IO.output(green3,IO.HIGH)
        IO.output(red3,IO.LOW)
        count += 1
        unoccupiedSlot.append(1004)
    if (IO.input(ir4) == 1):
        IO.output(green4,IO.HIGH)
        IO.output(red4,IO.LOW)
        count += 1
        unoccupiedSlot.append(1005)
        
    #print(count)
    #print("occupied : ", occupiedSlot)
    #print("unoccupied : ", unoccupiedSlot)

# dynamically Generated Json slot status
#    data = '{"occupiedSlot": [1001,1002],"unoccupiedSlot": [1003,1004,1005]}'
    json = '{\"occupiedSlot\":'+str(occupiedSlot)+',\"unoccupiedSlot\":'+str(unoccupiedSlot)+'}'
    print (json)
    
# printing values on the LCD    
    lcd.clear()
    string = "Empty Slots : "+ str(count)    
    lcd.write_string(string)
    
# sending the HTTP post request to the server
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json, headers=headers)
    print('Response Code : ' + str(response.status_code))
        
    time.sleep(1)
        
    
    