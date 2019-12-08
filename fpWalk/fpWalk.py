import yaml
import time
from hexapod import Hexapod_12DOF

class fpWalk():
    #servos
    frontLeftRaise=[]
    frontRightRaise=[]
    centerLeftRaise=[]
    centerRightRaise=[]
    backLeftRaise=[]
    backRightRaise=[]
    frontLeftRotate=[]
    frontRightRotate=[]
    centerLeftRotate=[]
    centerRightRotate=[]
    backLeftRotate=[]
    backRightRotate=[]

    def __init__(self):
        self.my_hexapod = None
        config = open('config_12DOF.yaml')
        my_config = yaml.safe_load(config)
        self.my_hexapod = Hexapod_12DOF(my_config)
        
    def setPos(self, servo, pos):
        self.my_hexapod.servos[servo].set_position(pos)

    def runLoop(self,servoArray):
        step = len(servoArray)/12
        for x in range(0,len(servoArray)/12):
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
    
    """
    setupServos
    Sets up a pattern for the servos to follow, uses lists for each action for each servo,
        in centisecond intervals.
    returns a single list of each servo list appended together.
    """

    def setupServos(self, pattern):
        # Clear servo arrays
        self.frontLeftRaise.clear()
        self.frontRightRaise.clear()
        self.centerLeftRaise.clear()
        self.centerRightRaise.clear()
        self.backLeftRaise.clear()
        self.backRightRaise.clear()
        self.frontLeftRotate.clear()
        self.frontRightRotate.clear()
        self.centerLeftRotate.clear()
        self.centerRightRotate.clear()
        self.backLeftRotate.clear()
        self.backRightRotate.clear()

        if pattern == "forward":
            for _ in range(20):
                self.frontLeftRaise.append(50)
                self.frontRightRaise.append(50)
                self.centerLeftRaise.append(50)
                self.centerRightRaise.append(50)
                self.backLeftRaise.append(50)
                self.backRightRaise.append(50)
                self.frontLeftRotate.append(100)
                self.frontRightRotate.append(100)
                self.centerLeftRotate.append(100)
                self.centerRightRotate.append(100)
                self.backLeftRotate.append(100)
                self.backRightRotate.append(100)
            for _ in range(20): # Raise 3 legs
                self.frontLeftRaise.append(self.frontLeftRaise[-1])
                self.frontRightRaise.append(0)
                self.centerLeftRaise.append(0)
                self.centerRightRaise.append(self.centerRightRaise[-1])
                self.backLeftRaise.append(self.backLeftRaise[-1])
                self.backRightRaise.append(0)
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Rotate 3 legs forward
                self.frontLeftRaise.append(self.frontLeftRaise[-1])
                self.frontRightRaise.append(self.frontRightRaise[-1])
                self.centerLeftRaise.append(self.centerLeftRaise[-1])
                self.centerRightRaise.append(self.centerRightRaise[-1])
                self.backLeftRaise.append(self.backLeftRaise[-1])
                self.backRightRaise.append(self.backRightRaise[-1])
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(0)
                self.centerLeftRotate.append(0)
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(0)
            for _ in range(20): # Lower 3 legs
                self.frontLeftRaise.append(0)
                self.frontRightRaise.append(70)
                self.centerLeftRaise.append(70)
                self.centerRightRaise.append(0)
                self.backLeftRaise.append(0)
                self.backRightRaise.append(70)
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Rotate 3 legs back
                self.frontLeftRaise.append(self.frontLeftRaise[-1])
                self.frontRightRaise.append(self.frontRightRaise[-1])
                self.centerLeftRaise.append(self.centerLeftRaise[-1])
                self.centerRightRaise.append(self.centerRightRaise[-1])
                self.backLeftRaise.append(self.backLeftRaise[-1])
                self.backRightRaise.append(self.backRightRaise[-1])
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(100)
                self.centerLeftRotate.append(100)
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(100)
            for _ in range(20): # Center 3 legs
                self.frontLeftRaise.append(50)
                self.frontRightRaise.append(50)
                self.centerLeftRaise.append(50)
                self.centerRightRaise.append(50)
                self.backLeftRaise.append(50)
                self.backRightRaise.append(50)
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Prep for a step (left-right-left step
                self.frontLeftRaise.append(50)
                self.frontRightRaise.append(50)
                self.centerLeftRaise.append(50)
                self.centerRightRaise.append(50)
                self.backLeftRaise.append(50)
                self.backRightRaise.append(50)
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Raise 3 legs
                self.frontLeftRaise.append(0)
                self.frontRightRaise.append(self.frontRightRaise[-1])
                self.centerLeftRaise.append(self.centerLeftRaise[-1])
                self.centerRightRaise.append(0)
                self.backLeftRaise.append(0)
                self.backRightRaise.append(self.backRightRaise[-1])
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Rotate 3 legs forward
                self.frontLeftRaise.append(self.frontLeftRaise[-1])
                self.frontRightRaise.append(self.frontRightRaise[-1])
                self.centerLeftRaise.append(self.centerLeftRaise[-1])
                self.centerRightRaise.append(self.centerRightRaise[-1])
                self.backLeftRaise.append(self.backLeftRaise[-1])
                self.backRightRaise.append(self.backRightRaise[-1])
                self.frontLeftRotate.append(0)
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(0)
                self.backLeftRotate.append(0)
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Lower 3 legs
                self.frontLeftRaise.append(70)
                self.frontRightRaise.append(0)
                self.centerLeftRaise.append(0)
                self.centerRightRaise.append(70)
                self.backLeftRaise.append(70)
                self.backRightRaise.append(0)
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Rotate 3 legs back
                self.frontLeftRaise.append(self.frontLeftRaise[-1])
                self.frontRightRaise.append(self.frontRightRaise[-1])
                self.centerLeftRaise.append(self.centerLeftRaise[-1])
                self.centerRightRaise.append(self.centerRightRaise[-1])
                self.backLeftRaise.append(self.backLeftRaise[-1])
                self.backRightRaise.append(self.backRightRaise[-1])
                self.frontLeftRotate.append(100)
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(100)
                self.backLeftRotate.append(100)
                self.backRightRotate.append(self.backRightRotate[-1])
            for _ in range(20): # Center 3 legs
                self.frontLeftRaise.append(50)
                self.frontRightRaise.append(50)
                self.centerLeftRaise.append(50)
                self.centerRightRaise.append(50)
                self.backLeftRaise.append(50)
                self.backRightRaise.append(50)
                self.frontLeftRotate.append(self.frontLeftRotate[-1])
                self.frontRightRotate.append(self.frontRightRotate[-1])
                self.centerLeftRotate.append(self.centerLeftRotate[-1])
                self.centerRightRotate.append(self.centerRightRotate[-1])
                self.backLeftRotate.append(self.backLeftRotate[-1])
                self.backRightRotate.append(self.backRightRotate[-1])
        
        servos = (self.frontLeftRaise + self.frontRightRaise + self.centerLeftRaise
        + self.centerRightRaise + self.backLeftRaise + self.backRightRaise
        + self.frontLeftRotate + self.frontRightRotate + self.centerLeftRotate
        + self.centerRightRotate + self.backLeftRotate + self.backRightRotate)
        
        return servos
        
bob = fpWalk()
        