import math
import numpy as np
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
from fplanck import fokker_planck, boundary, gaussian_pdf

class fPattern():
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

    sim = []

    servoPattern=[]
    planckPdf=[]
    planckPattern=[]

    def __init__(self, inputPatternName, Nsteps, stopTime):
        nm = 1e-9
        viscosity = 8e-4
        radius = 50*nm
        drag = 6*np.pi*viscosity*radius

        L = 20*nm
        F = lambda x: 5e-21*(np.sin(x/L) + 4)/L

        self.sim = fokker_planck(temperature=300, drag=drag, extent=600*nm,
            resolution=10*nm, boundary=boundary.periodic, force=F)
        
        self.servoPattern = self.setupServos(inputPatternName)
        self.planckPdf = self.funcify(self.servoPattern)
        self.planckPattern = self.planckify(self.planckPdf, Nsteps, stopTime)

    
    def planckify(self, pdf, Nsteps, stopTime):
        time, Pt = self.sim.propagate_interval(pdf, stopTime, Nsteps=Nsteps)
        return time, Pt

    def funcify(self, pattern):
        def pdf(*args):
            values = np.ones_like(args)
            for i, _ in enumerate(args):
                values *= pattern[i]
            return values

        return pdf
    
    """
    setupServos
    Sets up a pattern for the servos to follow, uses lists for each action for each servo,
        in centisecond intervals.
    returns a single list of each servo list appended together.
    """

    def setupServos(self, patternName):
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

        if patternName == "forward":
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
        