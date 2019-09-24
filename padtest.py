from pad4pi import rpi_gpio
from time import sleep
import RPi.GPIO as GPIO
#from lcd_func import output_to_lcd
from RPLCD import CharLCD

#******************************************#
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]


COL_PINS = [4, 22, 27, 17] # BCM numbering
ROW_PINS = [20,16,12,25] # BCM numbering


factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)



pn=""

def printKey(key):
    global pn
    pn += key
    #print(key)
    if len(pn)==8:
       
       print(pn);
       
       #lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
       #lcd.write_string("Hello "+pn)

       exec(open("ultrasonic.py").read())
       pn =""

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

while True:
	sleep(0.5)
