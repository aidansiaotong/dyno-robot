import numpy as np


class Configuration:
    def __init__(self):
        self.ps4_color = {"red": 254, "blue": 7, "green": 204}
        self.ps4_deactivated_color = {"red": 0, "blue": 68, "green": 34}
        
        self.max_x_velocity = 0.4 ## CHANGE/ADJUST MY VALUE
        self.max_y_velocity = 0.3 ## CHANGE/ADJUST MY VALUE
        
        self.dt = 0.01