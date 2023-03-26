#!/usr/bin/env python3
"""
This script blinks an LED and shuts down the raspberry pi when a button is held.

The default button GPIO pin is 17. The default LED pin is 27.
The LED will blink 6 times before executing the shutdown subprocess.
"""
import subprocess
import sys
import time

import RPi.GPIO as GPIO

def main(button_pin: int = 17, led_pin: int = 27) -> int:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led_pin, GPIO.OUT)
    return watch_button(button_pin, led_pin)

def watch_button(button_pin: int, led_pin: int) -> int:
    GPIO.wait_for_edge(button_pin, GPIO.FALLING, bouncetime=200)
    counter: int = 0
    counter_max: int = 6
    pause_interval: float = 0.5
    while GPIO.input(button_pin) == GPIO.LOW:
        if counter > counter_max:
            message = "wall -n Manual shutdown initiated"
            subprocess.run(message.split(),
                stdout=subprocess.PIPE,
                universal_newlines=True)
            light_led(led_pin, 3)
            GPIO.cleanup()
            shut_down()
            return 0
        else:
            counter += 1
            light_led(led_pin, 0.1)
            time.sleep(pause_interval)
    watch_button(button_pin, led_pin)

def shut_down() -> None:
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

def light_led(led_pin: int, light_time: float = 1):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(light_time)
    GPIO.output(led_pin, GPIO.LOW)

if __name__ == '__main__':
    sys.exit(main())
