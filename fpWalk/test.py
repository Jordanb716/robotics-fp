import matplotlib.pyplot as plt

from fPattern import fPattern

myFokkinPattern = fPattern('forward', 20, 2e-5)

plt.plot(myFokkinPattern.servoPattern)
plt.show()
plt.plot(myFokkinPattern.planckPattern[1].flatten())
plt.show()