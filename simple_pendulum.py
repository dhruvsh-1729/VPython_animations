GlowScript 2.9 VPython

tmax=30
#Simple Pendulum
mass=1.0
length=1.0
damping=0.5
grav=10
theta=0.5
omega=0.0
time=0.0
dt=0.001
timeperiod=0
Amp=0.4
driver_freq=sqrt(10)
gdisplay(xtitle="Time(seconds)",ytitle="Theta(radians)")
theta_curve=gcurve(color=color.green,label="theta(in radians)")
gdisplay(xtitle="Theta(in radians)",ytitle="Omega(in radians per second")
phase_space=gcurve(color=color.blue,label="Phase space curve")
bob=sphere(pos=vector(length*sin(theta),-length*cos(theta),0),radius=length*0.1,color=color.red) 
rod=cylinder(pos=vector(0,0,0),axis=bob.pos,color=color.white,radius=bob.radius*0.1)
  
def ang_acc(theta,omega,time):
  
  Fd=Amp*cos(driver_freq*time)
  ang_acc=-grav/length*sin(theta)-damping*omega+Fd/mass
  
  return ang_acc
  
while(time<=tmax):
  rate(1000)
  omega=omega+ang_acc(theta,omega,time)*dt
  theta=theta+omega*dt
  time+=dt
  bob.pos=vector(length*sin(theta),-length*cos(theta),0)
  rod.axis=bob.pos
  theta_curve.plot(time,theta)
  phase_space.plot(theta,omega)
