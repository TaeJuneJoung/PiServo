#!/usr/bin/env python
#
#  Pi Servo Control
#
#  E-mail: jtj0525@gmail.com
#  Blog: taejunejoung.github.io

import RPi.GPIO as GPIO
import time
import decimal
import sys

global servo_pin, servo_angle
servo_pin = 0
servo_angle = 0

if(len(sys.argv) > 2):
    servo_pin = int(sys.argv[1])
    servo_angle = decimal.Decimal(sys.argv[2])

def argv_set_angle(start_duty=7.5):
    global servo_pin, servo_angle
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(start_duty)
    duty_cycle = servo_angle / 18 + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)
    pwm.stop()


class Servo:
    def set_pin(self, pin_num, pwm_num=50, start_duty=7.5):
        self.pin_num = pin_num
        GPIO.setup(pin_num, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(pin_num, pwm_num)
        self.servo_pwm.start(start_duty)
    
    def set_angle(self, servo_angle):
        self.duty_cycle = servo_angle / 18 + 2
        self.servo_pwm.ChangeDutyCycle(self.duty_cycle)
        time.sleep(0.3)

    def servo_stop(self):
        self.servo_pwm.stop()

    def cleanup(self):
        GPIO.cleanup()

if __name__ == '__main__':
    if(servo_pin and servo_angle):
        GPIO.setup(servo_pin, GPIO.OUT)
        argv_set_angle()
        GPIO.cleanup()