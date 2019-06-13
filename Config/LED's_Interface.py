#importing the requests package
import requests
import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

#public URL of the App
url = 'https://webhook.site/f061197e-2c23-4c15-89f5-e7341154f3f8'

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
#ir1    = xx
#ir2    = xx
#ir3    = xx
#ir4    = xx
#ir5    = xx

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

IO.output(green0,IO.HIGH)
IO.output(green1,IO.HIGH)
IO.output(green2,IO.HIGH)
IO.output(green3,IO.HIGH)
IO.output(green4,IO.HIGH)
IO.output(red0,IO.HIGH)
IO.output(red1,IO.HIGH)
IO.output(red2,IO.HIGH)
IO.output(red3,IO.HIGH)
IO.output(red4,IO.HIGH)

time.sleep(10)

#IO.cleanup() 


#for x in range(5):
#	a = 'green'+str(x)
#	print (a)
#	g = int(a,10)
#	print(type(g))
#	b = red+x
#	c = ir+x
#	IO.setup(g,IO.OUT)
#	IO.setup(b,IO.OUT)
#	IO.setup(c,IO.OUT)
#        IO.output(a,IO.HIGH)
	


#while 1:	

	#JSON string to be send
	#data = '{"occupiedSlot":[1001,1002],"unoccupiedSlot":[1003,1004]}'

	#making the POST request to the URL
	#response = requests.post(url, data=data)
