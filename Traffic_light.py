import machine
import utime
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(13, machine.Pin.OUT)
led_G = machine.Pin(15, machine.Pin.OUT)
led_Y = machine.Pin(17, machine.Pin.OUT)
led_R = machine.Pin(16, machine.Pin.OUT)
Tend = True
i = 0
buzzer.value(0)
led_Y.value(0)
led_R.value(0)
while Tend:
    buttonPressed = 0
    led_G.value(1)
    if button.value() == 1 :
        if i<1:
            print("Button pressed!")
            i=1
        while i != 3:
            led_G.value(0)
            utime.sleep(1)
            led_G.value(1)
            utime.sleep(1)
            i=i+1
        led_G.value(0)
        led_Y.value(1)
        utime.sleep(2)
        led_Y.value(0)
        led_R.value(1)
        i=10
        while i!=0:
            print("Wait ",i," seconds")
            utime.sleep(0.8)
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            i=i-1
        buttonPressed = 1
        buzzer.value(0)
        print("STOP!")
    if buttonPressed == 1:
        led_G.value(1)
        led_Y.value(0)
        led_R.value(0)
        
