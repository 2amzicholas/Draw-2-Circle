#from cmath import pi, e
from math import *
from numpy import array as np_array, linspace
import matplotlib.pyplot as plot


splitcount = 512
circcount = 32
domainint = 1
domain = [0, domainint]

def f(x):
	if x < 0.5:
		return 1
	elif x > 0.5:
		return 0
	else:
		return 0.5
		


t = linspace(domain[0],domain[1],splitcount)
dt = 1/splitcount
y = []


for i in range(0,splitcount):
	y.insert(i, f(t[i]))

y = np_array(y)
x = np_array(t)

circ = []

for n in range(-circcount,circcount):
	c = sum(y*(e**(-n*2*pi*1j*t))*dt)
	circ.insert(n+circcount,c)
	#plot.plot(x,c*e**(n*2*pi*1j*t))
print("REALS")
for n in range(-circcount,circcount):
	c = circ[n+circcount]
	print(c.real*10000, end=",")
print("IMAGS")
for n in range(-circcount,circcount):
	c = circ[n+circcount]
	print(c.imag*10000, end=",")
	
def f1(x):
	out = 0
	for n in range(-circcount,circcount):
		c = circ[n+circcount]
		out = out + c*e**(n*2*pi*1j*x)
	return out

y1 = []
for i in range(0,splitcount):
	y1.insert(i, f1(x[i]))

y1 = np_array(y1)

##### visualise the input function
plot.plot(x,y1,"blue")
plot.plot(x,y,"green")
plot.plot(domain,[0,0],"black")
plot.plot([0,0],[y.min(),y.max()],"black")
plot.show(block=True)



