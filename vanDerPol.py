import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation
from scipy.integrate import odeint

fig = plt.figure()
mu = 0.1
ax = plt.axes(xlim = (-5,5), ylim = (-5,5))
line, = ax.plot([],[],lw = 2)

def init():
	line.set_data([],[])
	return line,

def VDP_Oscillator_derivative(x, t):
    nx0 = x[1]
    nx1 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
    res = np.array([nx0, nx1])
    return res

ts = np.linspace(0.0, 50.0, 5000.0)
xs = odeint(VDP_Oscillator_derivative, [-3.0, -3.0], ts)



def update(num,xs,line):
	line.set_data(xs[:num,0], xs[:num,1])
	return line,


xs2 = odeint(VDP_Oscillator_derivative, [-3.0, -3.0], ts)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_ylim([-3.0,3.0])
ax2.plot(xs[1000:,0])
ax2.plot(xs[1000:,1])



anim = animation.FuncAnimation(fig, update, len(xs),init_func = init, fargs=[xs, line],interval=1, blit=True)


plt.show()


