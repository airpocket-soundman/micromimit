# Imports go at the top
from microbit import *
import radio
radio.config(group=0)
radio.on()
mode = pin0.read_digital()
timerflag = 0
mode = 0
timer = 0
display.show(Image.HAPPY)

# Code in a 'while True:' loop repeats forever
while True:
   message = radio.receive()
   if message:
       if mode == 0:
           if message == '0':
               display.show(Image('00900:'
                                  '00000:'
                                  '00000:'
                                  '00000:'
                                  '00000:'))
           if message == '1':
               display.show(Image('00090:'
                                  '00000:'
                                  '00000:'
                                  '00000:'
                                  '00000:'))
           if message == '2':
               display.show(Image('00009:'
                                  '00000:'
                                  '00000:'
                                  '00000:'
                                  '00000:'))
           if message == 'A':
               display.show(Image('90000:'
                                  '00000:'
                                  '00000:'
                                  '00000:'
                                  '00000:'))
           if message == 'B':
               display.show(Image('00000:'
                                  '00000:'
                                  '00000:'
                                  '00009:'
                                  '00000:'))
            
   if button_a.was_pressed():
       timer -= 1 
       if timer < 0:
           timer = 0
       display.show(timer)
   if button_b.was_pressed():
       timer += 1
       if timer > 9:
           timer = 9
       display.show(timer)
   mode = pin0.read_digital() 
   if mode == 0:
       timerflag = 1
   if mode == 1:
       if timerflag == 1:
           timerflag = 0
           sleep(timer * 1000)
           pin1.write_digital(1)
           display.show(Image('09990:'
                              '90009:'
                              '90009:'
                              '90009:'
                              '09990:'))
           sleep(1000)
           display.show(Image.HAPPY)
   if pin2.is_touched():
       pin1.write_digital(0)
   if pin_logo.is_touched():
       display.show(Image.HAPPY)
               