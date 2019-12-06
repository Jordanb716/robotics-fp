import yaml
from hexapod import Hexapod_12DOF

class fpWalk():
    def __init__(self):
        self.my_hexapod = None
        config = open('config_12DOF.yaml')
        my_config = yaml.safe_load(config)
        self.my_hexapod = Hexapod_12DOF(my_config)
        
        #servos
        fll #front left lift
        flr #front left rotate
        frl #front right lift
        frr
        cll #center left lift
        clr
        crl
        crr
        bll
        blr #back right rotate
        brl
        brr
        
    def setPos(self, servo, pos):
        self.my_hexapod.servos[servo].set_position(pos)
        
    def setupServos(self, pattern):
        if pattern == "forward":
            for x in range(0,20):
                
        
bob = fpWalk()
        