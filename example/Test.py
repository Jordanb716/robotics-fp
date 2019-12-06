import argparse
import socket
import time
import yaml


from hexapod import Hexapod_12DOF
 

class selftest():

    def __init__(self):
        # open config file
        config = open('config_12DOF.yaml')
        my_config = yaml.load(config, Loader=yaml.FullLoader)
        self.my_hexapod = Hexapod_12DOF(my_config)
    
    def test_leg(self,name,lift=False,rotate=False,time_step=0.1):
    
        if lift:
            value = 0
            for x in range(5):
                self.my_hexapod.move_leg(name=name, rotate_value=0, raise_value=value)
                time.sleep(2*time_step)
                value += 25
                
        if rotate:
            value = 0
            for x in range(5):
                self.my_hexapod.move_leg(name=name, rotate_value=value, raise_value=0)
                time.sleep(2*time_step)
                value += 25
                
    def test_all_legs(self,lift=False,rotate=False,time_step=0.1):
        
        if lift:
            value = 0
            for x in range(5):
                self.my_hexapod.move_all_legs(raise_value=value)
                time.sleep(2*time_step)
                value += 25
                
        if rotate:
            value = 0
            for x in range(5):
                self.my_hexapod.move_all_legs(rotate_value=value)
                time.sleep(2*time_step)
                value += 25


if __name__ == '__main__':
    
    test = selftest()
    cont_test = True
    
    while cont_test:
        print("name")
        name=input(">>")
        
        if name == 'all':
            test.test_all_legs(lift=True)
            test.test_all_legs(rotate=True)
        elif name == 'reset':
            test.my_hexapod.reset()
        else:
            test.test_leg(name=name,lift=True)
            test.test_leg(name=name,rotate=True)
            
        print("\n\ncontinue testing?")
        resp = input("y/n  ")[0]
        if resp == 'n' or resp == 'N':
            cont_test = False








