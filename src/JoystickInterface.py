import UDPComms
import numpy as np
import time

from Command import Command


class JoystickInterface:
    def __init__(self, config, udp_port=8830, udp_publisher_port=8840):
        self.configuration = config
        self.previous_sit_toggle = 0
        self.previous_stand_toggle = 0
        self.previous_walk_toggle = 0
        self.previous_step_up_toggle = 0
        self.previous_activate_toggle = 0
        
        self.message_rate = 50
        self.udp_handle = UDPComms.Subscriber(udp_port, timeout=1)
        self.udp_publisher = UDPComms.Publisher(udp_publisher_port)
        
        
    def get_command(self, do_print=False):
        try:
            msg = self.udp_handle.get()
            command = Command()
            
            # Check if requesting sit event
            sit_toggle = msg["circle"]
            command.sit_event = (sit_toggle == 1 and self.previous_sit_toggle == 0)
            
            # Check if requesting stand event
            stand_toggle = msg["triangle"]
            command.stand_event = (stand_toggle == 1 and self.previous_stand_toggle == 0)
            
            # Check if requesting walk event
            walk_toggle = msg["x"]
            command.walk_event = (walk_toggle == 1 and self.previous_walk_toggle == 0)
            
            # Check if requesting step up event
            step_up_toggle = msg["square"]
            command.step_up_event = (step_up_toggle == 1 and self.previous_step_up_toggle == 0)
            
            # Check if activating robot
            activate_toggle = msg["R1"]
            command.activate_event = (activate_toggle == 1 and self.previous_activate_toggle == 0)
            
            # Update previous values for toggles and state
            self.previous_sit_toggle = sit_toggle
            self.previous_stand_toggle = stand_toggle
            self.previous_walk_toggle = walk_toggle
            self.previous_step_up_toggle = step_up_toggle
            self.previous_activate_toggle = activate_toggle
            
            # Continuous commands
            x_vel = msg["ly"] * self.configuration.max_x_velocity
            y_vel = msg["lx"] * -self.configuration.max_y_velocity
            command.horizontal_velocity = np.array([x_vel, y_vel])
            
            message_rate = msg["message_rate"]
            message_dt = 1.0 / message_rate
            
            ## Insert any pitch, height control commands
            
            return command
        
        except UDPComms.timeout:
            if do_print:
                print("UDP Timed out")
            return Command()
        
        
    def set_color(self, color):
        joystick_msg = {"ps4_color": color}
        self.udp_publisher.send(joystick_msg)