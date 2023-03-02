from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio
radio.config(group=69)
radio.on()
initialize()
clear_oled()
while True:
    message = radio.receive()
    if message == 'someone detected':
        add_text(0, 1, "there is someone")
        sleep(2000)
        clear_oled()
    elif message == 'nothing':
        add_text(0, 0, "nothing")
        sleep(2000)
        clear_oled()