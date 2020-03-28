import matplotlib.pyplot as plt

from fPattern import fPattern

myFokkinPattern = fPattern('forward', 10)

plt.plot(myFokkinPattern.servoPattern)
plt.show()
plt.plot(myFokkinPattern.planckPattern)
plt.show()