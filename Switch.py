import machine
import utime
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_extG = machine.Pin(15, machine.Pin.OUT)
while True:
    if button.value() == 1:
        if i<1:
            led_extG.toggle()
            print("Button pressed!")
        i=i+1
    else:
        i=0
