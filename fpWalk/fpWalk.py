import time
import yaml

from hexapod import Hexapod_12DOF
from fPattern import fPattern

my_hexapod = None
config = open('config_12DOF.yaml')
my_config = yaml.safe_load(config)
my_hexapod = Hexapod_12DOF(my_config)

def setPos(self, servo, pos):
    self.my_hexapod.servos[servo].set_position(pos)

def runLoop(self,servoArray):
    step = round(len(servoArray)/12)
    for x in range(0,step):
        self.setPos("left_front_raise", servoArray[x])
        self.setPos("right_front_raise", servoArray[step+x])
        self.setPos("left_center_raise", servoArray[step*2+x])
        self.setPos("right_center_raise", servoArray[step*3+x])
        self.setPos("left_back_raise", servoArray[step*4+x])
        self.setPos("right_back_raise", servoArray[step*5+x])
        self.setPos("left_front_rotate", servoArray[step*6+x])
        self.setPos("right_front_rotate", servoArray[step*7+x])
        self.setPos("left_center_rotate", servoArray[step*8+x])
        self.setPos("right_center_rotate", servoArray[step*9+x])
        self.setPos("left_back_rotate", servoArray[step*10+x])
        self.setPos("right_back_rotate", servoArray[step*11+x])
        time.sleep(0.01)
