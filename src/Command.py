import numpy as np


class Command:
    '''Object to store movement command
    '''
    
    def __init__(self):
        self.horizontal_velocity = np.array([0, 0])
        #self.height = 0
        
        self.sit_event = False
        self.stand_event = False
        self.walk_event = False
        self.step_up_event = False
        self.activate_event = False