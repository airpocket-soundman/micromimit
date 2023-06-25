# Imports go at the top
from microbit import *
import radio
microphone.set_threshold(SoundEvent.LOUD, 1)
mic = 0
radio.config(group=0)
radio.on()
number = 0
display.show(number)

# Code in a 'while True:' loop repeats forever
while True:
   if button_a.was_pressed():
       number -= 1
       if number < 0:
           number = 0
       display.show(number)
   if button_b.was_pressed():
       number += 1
       if number > 2:
           number = 2
       display.show(number) 
   if pin_logo.is_touched():
       mic = 0
   if microphone.current_event() == SoundEvent.LOUD:
       mic = 1
       radio.send(str(number))
   if mic == 1:
       display.clear()
       sleep(500)
       display.show(number)
       sleep(500)