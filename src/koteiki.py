# Imports go at the top
from microbit import *
import radio

mic = 0
radio.config(group=0)
radio.on()
display.show('A')
microphone.set_threshold(SoundEvent.LOUD, 1)

# Code in a 'while True:' loop repeats forever
while True:
   if microphone.current_event() == SoundEvent.LOUD:
       mic = 1
       radio.send('A')
   if mic == 1:
       display.clear()
       sleep(500)
       display.show('A')
       sleep(500)
   if pin_logo.is_touched():
       mic = 0
       display.show('A')
       
        
    