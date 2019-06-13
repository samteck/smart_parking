import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

print("Started")

ir0 = 21
ir1 = 3
ir2 = 2
ir3 = 12
ir4 = 7


IO.setup(ir0,IO.IN)
IO.setup(ir1,IO.IN)
IO.setup(ir2,IO.IN)
IO.setup(ir3,IO.IN)
IO.setup(ir4,IO.IN)



while 1 :
    
    print ("ir0 : " + str(IO.input(ir0)) + " ir1 : " + str(IO.input(ir1)) + " ir2 : " + str(IO.input(ir2)) + " ir3 : " + str(IO.input(ir3)) + " ir4 : " + str(IO.input(ir4)))
        
    time.sleep(1)
        
    
    