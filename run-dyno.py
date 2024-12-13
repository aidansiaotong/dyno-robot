import serial
from time import sleep
import numpy as np
import time
from JoystickInterface import JoystickInterface
from Configuration import Configuration



# Serial port and baud rate configuration
serial_port = "/dev/ttyACM0"  # Update if needed (e.g., "/dev/ttyUSB0")
baud_rate = 9600

# Open the serial connection
ser = serial.Serial(serial_port, baud_rate)

#Global Variables

#homing each servo  
CH0 = 178
CH1 = 186
CH2 = 180
CH3 = 193
CH4 = 174
CH5 = 184
CH6 = 186
CH7 = 177
CH8 = 179
CH9 = 176
CH10 = 179
CH11 = 186
# Functions to set speed and acceleration
def set_speed(channel, speed):
    """
    Sets the speed of the servo on the specified channel.
    Speed is in units of 0.25 microseconds per 10 milliseconds.
    """
    command = bytearray([0x87, channel, speed & 0x7F, (speed >> 7) & 0x7F])
    ser.write(command)

def set_acceleration(channel, acceleration):
    """
    Sets the acceleration of the servo on the specified channel.
    Acceleration is in units of 0.25 microseconds per 100 milliseconds per second.
    """
    command = bytearray([0x89, channel, acceleration & 0x7F, (acceleration >> 7) & 0x7F])
    ser.write(command)

# Main SERVO Function
def servo_angle(channel, angle):
    """
    First choose Channel 0-11
    Target = PMW signal in quarter microseconds
    (e.g., 2000 = 500µs, 10000 = 2500µs)
    Angle = (0-357°)
    """
    if not 0 <= angle <= 357:
        raise ValueError("Angle must be between 0 and 357 degrees.")
    target = int(2000 + (angle / 357) * (10000 - 2000))  # Map 0-357° to 2000-10000
    
    if not 0 <= channel <= 11:
        raise ValueError("Channel must be between 0 and 11.")
    if not 2000 <= target <= 10000:
        raise ValueError("Target must be between 2000 and 10000.")
    
    # Command to set target position
    command = bytearray([0x84, channel, target & 0x7F, (target >> 7) & 0x7F])
    ser.write(command)

def set_speed_all(spec):
     for ch in range(12):
        set_speed(ch, spec)  # Adjust speed value as needed
        #set_acceleration(ch, 5)   Adjust acceleration value as needed

def sit_dog():
    

    servo_angle(4,CH4-25)
    servo_angle(5,CH5+25)
    servo_angle(6,CH6-25)
    servo_angle(7,CH7+25)

    servo_angle(0,CH0+45)
    servo_angle(1,CH1-45)
    servo_angle(2,CH2+45)
    servo_angle(3,CH3-45)

    servo_angle(8,CH8)
    servo_angle(9,CH9)
    servo_angle(10,CH10)
    servo_angle(11,CH11)

    for ab in range (4):          
        servo_angle(8 + ab,180) # plus 8 to ensure it hits channels 8-11

def stand_dog():
    

    servo_angle(4,CH4+20)
    servo_angle(5,CH5-20)
    servo_angle(6,CH6+20)
    servo_angle(7,CH7-20)

    servo_angle(0,CH0+15)
    servo_angle(1,CH1-15)
    servo_angle(2,CH2+15)
    servo_angle(3,CH3-15)

    servo_angle(8,CH8)
    servo_angle(9,CH9)
    servo_angle(10,CH10)
    servo_angle(11,CH11)
    
def lay_dog():
    servo_angle(0,CH0+15)
    servo_angle(1,CH1-15)
    servo_angle(2,CH2+15)
    servo_angle(3,CH3-15)
    servo_angle(4,CH4-65)
    servo_angle(5,CH5+65)
    servo_angle(6,CH6-65)
    servo_angle(7,CH7+65)
    servo_angle(8,CH8)
    servo_angle(9,CH9)
    servo_angle(10,CH10)
    servo_angle(11,CH11)
    
def right_leg_up():
    servo_angle(4,CH4-5)
    servo_angle(5,CH5-20)
    servo_angle(6,CH6-5)
    servo_angle(7,CH7-20)
    servo_angle(0,CH0+25)
    servo_angle(1,CH1-15)
    servo_angle(2,CH2+25)
    servo_angle(3,CH3-15)
    servo_angle(8,CH8+5)
    servo_angle(9,CH9)
    servo_angle(10,CH10+5)
    servo_angle(11,CH11)
    
    sleep(1)
    set_speed_all(5)
    
    servo_angle(4,CH4-5)
    servo_angle(5,CH5+65)
    servo_angle(6,CH6-5)
    servo_angle(7,CH7-20)
    servo_angle(0,CH0+25)
    servo_angle(1,CH1+5)
    servo_angle(2,CH2+25)
    servo_angle(3,CH3-15)
    servo_angle(8,CH8+5)
    servo_angle(9,CH9)
    servo_angle(10,CH10-5)
    servo_angle(11,CH11)
    set_speed_all(15)
    
def leg_path():

    servo_angle(8,CH8)
    servo_angle(9,CH9)
    servo_angle(10,CH10-7)
    servo_angle(11,CH11+7)
    #LEG B&C should be ON ground
    #LEG A&D on the ground
    servo_angle(1,CH1-44)
    servo_angle(5,CH5+0)
    servo_angle(2,CH2+44)
    servo_angle(6,CH6-0)
    servo_angle(0,CH0+61)
    servo_angle(4,CH4-16)
    servo_angle(3,CH3-61)
    servo_angle(7,CH7+16)
    sleep(.5)
    servo_angle(1,CH1-61)
    servo_angle(5,CH5-29)
    servo_angle(2,CH2+61)
    servo_angle(6,CH6+29)
    servo_angle(0,CH0+36)
    servo_angle(4,CH4-46)
    servo_angle(3,CH3-36)
    servo_angle(7,CH7+46)
    sleep(.5)
    servo_angle(1,CH1-54)
    servo_angle(5,CH5-29)
    servo_angle(2,CH2+54)
    servo_angle(6,CH6+29)
    servo_angle(0,CH0-4)
    servo_angle(4,CH4-31)
    servo_angle(3,CH3-10)
    servo_angle(7,CH7+31)
    sleep(.5)
    #LEG B&C off the ground
    #LEG A&D on the ground
    servo_angle(1,CH1-61)
    servo_angle(5,CH5+16)
    servo_angle(2,CH2+61)
    servo_angle(6,CH6-16)
    servo_angle(0,CH0+44)
    servo_angle(4,CH4-0)
    servo_angle(3,CH3-44)
    servo_angle(7,CH7+0)
    sleep(.5)
    servo_angle(1,CH1-36)
    servo_angle(5,CH5+46)
    servo_angle(2,CH2+36)
    servo_angle(6,CH6-46)
    servo_angle(0,CH0+61)
    servo_angle(4,CH4+29)
    servo_angle(3,CH3-61)
    servo_angle(7,CH7-29)
    sleep(.5)
    servo_angle(1,CH1+4)
    servo_angle(5,CH5+31)
    servo_angle(2,CH2-4)
    servo_angle(6,CH6-31)
    servo_angle(0,CH0+54)
    servo_angle(4,CH4+29)
    servo_angle(3,CH3-54)
    servo_angle(7,CH7-29)
    sleep(.5)
    
    # servo_angle(1,CH1-6)
    # servo_angle(5,CH5+31)
    # servo_angle(2,CH2-6)
    # servo_angle(6,CH6+31)
    # sleep(.25)
    # servo_angle(1,CH1-26)
    # servo_angle(5,CH5+21)
    # servo_angle(2,CH2-26)
    # servo_angle(6,CH6+21)
    # sleep(.1)
    # servo_angle(1,CH1-36)
    # servo_angle(5,CH5+11)
    # servo_angle(2,CH2-36)
    # servo_angle(6,CH6+11)
    # sleep(.1)










#MAIN CODE STARTS HERE:
    
#____________________________________________________________________________________

try:
    configuration = Configuration()
    
    print("Creating joystick listener...")
    joystick_interface = JoystickInterface(configuration)
    print("Done.")
    
    last_loop = time.time()
    
    
    
    while True:
        print("Waiting for user to press R1 to activate Dyno.")
        while True:
            command = joystick_interface.get_command()
            joystick_interface.set_color(configuration.ps4_deactivated_color)
            if command.activate_event == 1:
                break
            time.sleep(0.1)
        print("Robot activated.")
        joystick_interface.set_color(configuration.ps4_color)
        
        ##
        #ACTIVATE SERVOS
        set_speed_all(15)
        
        #WAKE UP WITHOUT OVER CURRENT
        servo_angle(4,CH4-25)
        sleep(.2)
        servo_angle(5,CH5+25)
        sleep(.2)
        servo_angle(6,CH6-25)
        sleep(.2)
        servo_angle(7,CH7+25)
        sleep(.2)
        servo_angle(0,CH0+45)
        sleep(.2)
        servo_angle(1,CH1-45)
        sleep(.2)
        servo_angle(2,CH2+45)
        sleep(.2)
        servo_angle(3,CH3-45)
        sleep(.2)
        servo_angle(8,CH8)
        sleep(.2)
        servo_angle(9,CH9)
        sleep(.2)
        servo_angle(10,CH10)
        sleep(.2)
        servo_angle(11,CH11)
        sleep(.2)
        sit_dog()
        ##
        
        while True:
            now = time.time()
            if now - last_loop < configuration.dt:
                continue
            last_loop = time.time()
            
            command = joystick_interface.get_command()
            if command.activate_event == 1:
                print("Deactivating Dyno.")
                break
            
            if command.sit_event == 1:
                print("Sitting")
                sit_dog()
                sleep(5)
            
            if command.stand_event == 1:
                print("Standing")
                stand_dog()
                sleep(3)
                
            if command.walk_event == 1:
                print("Walking")
                leg_path()
                sleep(5)
            
            if command.step_up_event == 1:
                print("Stepping up")
                right_leg_up()
                sleep(2)
            
            #print(command.horizontal_velocity)
            if command.horizontal_velocity[0] > 0.01:
                print("Walking forward") # walk function here
    
    
    

   
    
   
        
         # Manual MOVEMENT the channel and angle COMMENT IN IF NEEDED
#         channel = int(input("Enter the servo channel (0-11): "))
#         angle = int(input("Enter the servo angle (whole numbers only 0-357°): "))
#         servo_angle(channel, angle)
#         sleep(1)


                






except KeyboardInterrupt:
    print("Exiting program")

finally:
    ser.close()