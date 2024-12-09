import numpy as np
import time
from JoystickInterface import JoystickInterface
from Configuration import Configuration


def main():
    
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
                # circle
                print("Sitting")
                # insert sit function here
            
            if command.stand_event == 1:
                # triangle
                print("Standing")
                # insert stand function here
                
            if command.walk_event == 1:
                # x
                print("Walking")
                # insert walk function here
            
            if command.step_up_event == 1:
                # square
                print("Stepping up")
                # insert step up function here
            
            #print(command.horizontal_velocity)
            if command.horizontal_velocity[0] > 0.01:
                print("Walking forward") # walk function here

        
        
main()
            
