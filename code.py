# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""
import binascii
import board
import busio
import digitalio
import time

from dabble import Dabble #Imports the libariars we need

dabble = Dabble(board.GP4, board.GP5, debug=True)

import pwmio #imports libaries that are needed to run this code

from adafruit_motor import motor #imports a small section of adafruit_motor libary

left_motor_forward = board.GP12 #Initilizes the varibale left_motor_forward and attaches it to GP12
left_motor_backwards = board.GP13 #Initilizes the varibale left_motor_backwards and attaches it to GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(left_motor_backwards, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Intilaizes Left_Motor and configuration line and it is required
Left_Motor_speed = 0 #Intilaizes the variable Left_Motor_speed to 0


right_motor_forward = board.GP14 #Initilizes the varibale right_motor_forward and attaches it to GP14
right_motor_backwards = board.GP15 #Initilizes the varibale right_motor_backwards and attaches it to GP15


pwm_La = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(right_motor_backwards, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Right_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Intilaizes Right_Motor and configuration line and it is required
Right_Motor_speed = 0

def Robot_forward():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

def Robot_backwards():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed

def Robot_right():
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed

def Robot_left():
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed

def Robot_stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed


while True:
    message = dabble.read_message()
    if (message != None):
        print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            print("Move both motors forward")
            Robot_forward()
        elif (message.down_arrow_pressed):
            print("Move both motors backward")
            Robot_backwards()
        elif (message.right_arrow_pressed):
            print("Move left motor forward and right motor backward")
            Robot_left()
        elif (message.left_arrow_pressed):
            print("Move left motor backward and right motor forward")
            Robot_right()
        elif (message.no_direction_pressed):
            print("Stop both motors")
            Robot_stop()
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
