import RPi.GPIO as GPIO
from piservo import Servo
import decimal

servo_pin = int(input('Enter Servo Motor Pin Number'))

def check_angle(angle):
    if angle < 0 and angle > 180:
        print('Possible Servo Motor Angle range 0 <= Angle <= 180')
        raise Exception

GPIO.setmode(GPIO.BOARD)
# warning error visible/unvisible
#GPIO.setwarnings(False)

servo = Servo()
servo.set_pin(servo_pin)

# Testing 3 times
for _ in range(3):
    servo_angle = decimal.Decimal(input('Enter Servo Motor Angle]\n Angle >= 0 and Angle <= 180\n'))
    check_angle(servo_angle)
    servo.set_angle(servo_angle)

servo.servo_stop()
servo.cleanup()