import time
import machine
import esp32

from machine import Timer

hs_pin = machine.Pin(5, machine.Pin.In, machine.Pin.PULL_UP)
prev_time = time.ticks_ms()
prev_count = 0
rpm = 0
while True:
    hall_state = hs_pin.value()

    if hall_state == 1:
        curr_time = time.ticks_ms()
    revTime = curr_time - prev_time
    rpm = 60000 / revTime
    prev_time = curr_time
    iph = rpm * 39.9 - .1*rpm
    mph = iph / 63360
    time.sleep_ms(25)
