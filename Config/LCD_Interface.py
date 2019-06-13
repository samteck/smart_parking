from RPLCD import CharLCD
import RPi.GPIO
import time
RPi.GPIO.setwarnings(False)

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])

while True:
    lcd.clear()
    lcd.write_string("Welcome to POC  ")
    for i in range(16):
        lcd.write_string("#")
        time.sleep(0.2)
    lcd.clear()
    lcd.write_string("This is my POC")
    time.sleep(10)