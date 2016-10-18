import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation
from scipy.integrate import odeint

fig = plt.figure()

ax = plt.axes(xlim = (-5,5), ylim = (-5,5))
ax.set_xticks(np.arange(-5,5,1))
ax.set_yticks(np.arange(-5,5,1))
plt.grid()
plt.xlabel("x",fontsize = 20)
plt.ylabel("y",fontsize = 20)

handles = ["mu = 3","mu = 0.6"]

lines = [plt.plot([],[],lw = 2,label = handles[i])[0] for i in range(2)]
fig.legend(lines,handles,loc = "center right")
fig.suptitle("Phase portrait with limit cycle",fontsize = 24)

def init():
	for line in lines:
		line.set_data([],[])
	return lines

def VDP_Oscillator_derivative(x, t,mu):
	global a
	nx0 = x[1]
	nx1 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
	res = np.array([nx0, nx1,x[0]])
	return res

ts = np.linspace(0.0, 50.0, 5000.0)
xs = [odeint(VDP_Oscillator_derivative, [-3.0, -3.0,1.0], ts, args = (3,)),odeint(VDP_Oscillator_derivative, [0.2, 0.0,0.0], ts, args = (0.6,))]



def update(num,xs,lines):
	j = 0

	for line in lines:
		line.set_data(xs[j][:num,0], xs[j][:num,1])
		j = j + 1
	return lines

xs2 = odeint(VDP_Oscillator_derivative, [-3.0, -3.0,1.0], ts, args = (0.5,))
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_ylim([-3.0,3.0])
plt.xlabel('Time Coordinate', fontsize=18)
plt.ylabel('Variable Value', fontsize=18)
plt.title('State Variables vs Time (mu = 0.5)', fontsize = 24)
ax2.plot(xs[1][1000:,0],label = "x1")
ax2.plot(xs[1][1000:,1],label = "x2")
plt.legend(loc="upper right")
plt.savefig("vanDerPol_state_space.png")
plt.close()


anim = animation.FuncAnimation(fig, update, len(xs[0]),init_func = init, fargs=[xs, lines],interval=1, blit=True)

#plt.show()


