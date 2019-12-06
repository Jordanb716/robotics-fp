import yaml

from hexapod import Hexapod_12DOF


class angeldevil():
    faced = 'N'  #robot direction flag
    
    def __init__(self):
 
        self.my_hexapod = None
    
        # open config file
        config = open('config_12DOF.yaml')
        my_config = yaml.load(config, Loader=yaml.FullLoader)
        self.my_hexapod = Hexapod_12DOF(my_config)
        
#-------------------------------------------------------------------------------
#  Mechanics
        
    def face_north(self):
        if self.faced == 'E': #east
            cycles = 5
        elif self.faced == 'NE': #northeast
            cycles = 3
            
        for x in range(cycles):
            self.my_hexapod.rotate(back=False,left=True)
            self.my_hexapod.step()
            self.my_hexapod.rotate(back=True,left=True)
            
        if self.faced != 'N' and self.faced != 'E' and self.faced != 'NE':
            print("\n----------------------------\nHelp!! Face me North before continueing\n\n\n")
        
        self.my_hexapod.reset()
        self.faced = 'N'
        
    def go_north(self):
        print("Moving North\n")
        #Move forward
        self.my_hexapod.step(steps=5, time_step=0.1)
        self.my_hexapod.rotate(steps=2,back=True,left=True)
        self.faced = 'N'
                  
    def go_east(self):
        print("Moving East\n")
        #Turn right, then move forward
        for x in range(4):
            self.my_hexapod.rotate(back=False)
            self.my_hexapod.step()
            self.my_hexapod.rotate(back=True)
            
        self.my_hexapod.step(steps=4, time_step=0.1)
        self.faced = 'E'
        self.face_north()
        
    def go_northeast(self):
        print("Moving Northeast\n")
        self.my_hexapod.turn_right(steps=5)
        self.my_hexapod.step(steps=5, time_step=0.1)
        self.faced = 'NE'
        self.face_north()


#-------------------------------------------------------------------------------
#  Game
        
        
    def angel_turn(self):
        choice = 0
        while choice != 1 and choice != 2:
            print("---Angels turn---\n")
            print("1) Stay Still")
            print("2) Move North\n\n")
            choice = input(">> ")
            print("")
            choice = int(choice[0])
            if(choice == 1):
                print("staying still\n")
            elif (choice == 2):
                self.go_north()
            
            
        
    def devil_turn(self):
        choice = 0
        while choice != 1 and choice != 2:
            print("---devils turn---\n")
            print("1) Move East")
            print("2) Move Northeast\n\n")
            choice = input(">> ")
            print("")
            choice = int(choice[0])
            if(choice == 1):
                self.go_east()
            elif (choice == 2):
                self.go_northeast()
        print("\n\n")
                

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
        
if __name__ == '__main__':
    game = angeldevil()
    play = True
    while play:
        game.angel_turn()
        game.devil_turn()
        print("Would you like to continue?")
        choice = input("(y/n) ")[0] #only single character
        print(choice)
        if choice == 'n' or choice == 'N':
            play = False
        
 