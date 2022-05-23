GlowScript 3.1 VPython

#Please refresh the page everytime you run the animation again. (Recommended)

#This simulation has the bot moving forward, rotating 90 degrees
# Again moving forward, flipping and sliding the load by the help of rak-pinion
#Then again moving backwards, rotating 90 degrees, and again moving back
#to reach to its initial position.

# x_axis=cylinder(pos=vector(0,0,0),size=vector(5,0.1,0.1),axis=vector(1,0,0),color=color.blue)
robo_len=4.5
robo_wid=4.5
robo_height=2.9
castor_height=0.511
triangle_height=0.7
motor_diameter=0.6
rak_velocity=0.1
rak_radius=0.5
first_wall=box(pos=vector(-3.2,1,0),size=vector(0.2,2,6))
# floor=box(pos=vector(7.8-3.2,-0.2,0),size=vector(15.6,0.1,6))
# second_wall=box(pos=vector(12.4,1,0),size=vector(0.2,2,6))

robo_body=box(pos=vector(0,castor_height+0.5*robo_height,0),
               size=vector(robo_len,robo_height,robo_wid),
               color=color.yellow)
# top=shapes.points(pos=[[0.5*robo_len,castor_height+robo_height],
#                       [0.5*robo_len,castor_height+robo_height+triangle_height],
#                       [-0.5*robo_len+motor_diameter,castor_height+robo_height]])  
# top_part=extrusion(path=[vector(0,0,-0.5*robo_wid),vector(0,0,0.5*robo_wid)],shape=top)                      
# top_part.color=color.green
flipper=box(pos=vector(-0.5*motor_diameter,castor_height+robo_height,0),
           size=vector(robo_len-motor_diameter,0.1,robo_wid),color=color.orange)
flipper.rotate(axis=vector(0,0,-1),angle=0.19,
             origin=vector(0.5*robo_len-motor_diameter,castor_height+robo_height,0))                      

pinion=box(pos=vector(0,castor_height+robo_height,0),size=vector(robo_len,0.1,0.1),color=color.blue)

g1=shapes.circle(radius=rak_radius)
vec_path=[vector(-0.5*robo_len+rak_radius,castor_height+robo_height,-0.1),vector(-0.5*robo_len+rak_radius,castor_height+robo_height,0.1)]
rak=extrusion(path=vec_path,shape=g1)
# robot=robo_body
robot=compound([robo_body,pinion]) 
def flipperopen():
  t=0
  tmax=2
  dt=0.01
  while(t<=tmax):
    rate(1/dt)
    t+=dt
  angle_max=30*pi/180
  theta=0
  while(theta<=angle_max and rak.pos.z+3.5*rak_radius<system.pos.z+0.5*robo_len):
    rate(1/dt)
    flipper.rotate(axis=vector(1,0,0),angle=rak_velocity*dt/rak_radius,
                 origin=vector(system.pos.x,castor_height+robo_height,system.pos.z+0.5*robo_len-motor_diameter))
    rak.rotate(axis=vector(-1,0,0),angle=rak_velocity*dt/rak_radius)
    rak.pos.z+=velocity*dt
    theta+=rak_velocity*dt/rak_radius
    
def flipperclose():
  t=0 
  tmax=2
  angle_max=30*pi/180
  dt=0.01
  while(t<=tmax):
    rate(1/dt)
    t+=dt
  theta=0
  while(theta<=angle_max and rak.pos.z>system.pos.z-0.5*robo_len):
    rate(1/dt)
    flipper.rotate(axis=vector(-1,0,0),angle=rak_velocity*dt/rak_radius,
                 origin=vector(system.pos.x,castor_height+robo_height,system.pos.z+0.5*robo_len-motor_diameter))
    rak.rotate(axis=vector(1,0,0),angle=rak_velocity*dt/rak_radius)             
    rak.pos.z-=velocity*dt
    theta+=rak_velocity*dt/rak_radius
    # robot.pos.x-=velocity*dt
    # flipper.pos.x-=velocity*dt
  t=0
  while(t<=tmax):
    rate(1/dt)
    t+=dt

# while(True):
#   flipperopen()
#   flipperclose()

#To make normal wheel left
rimradius=1.7
rimthickness=0.2
rim1=ring(pos=vector(0,rimradius,0.5*robo_wid+0.1),axis=vector(0,0,1),radius=rimradius,thickness=rimthickness,color=color.red)
g1=shapes.gear(color=color.yellow,radius=rimradius-rimthickness,n=20);
vec_path=[vector(0,rimradius,0.5*robo_wid),vector(0,rimradius,0.1+0.5*robo_wid)]
gear1=extrusion(path=vec_path,shape=g1)
left_wheel=compound([gear1,rim1]);
#To make normal wheel right
rim2=ring(pos=vector(0,rimradius,-0.5*robo_wid-0.1),axis=vector(0,0,1),radius=rimradius,thickness=rimthickness,color=color.red)
g2=shapes.gear(color=color.yellow,radius=rimradius-rimthickness,n=20);
vec_path=[vector(0,rimradius,-0.5*robo_wid),vector(0,rimradius,-0.1-0.5*robo_wid)]
gear2=extrusion(path=vec_path,shape=g2)
right_wheel=compound([gear2,rim2]);

#To make the castor wheel front
castor_diameter=0.511
inward_castorlength=0.2
wheel1=sphere(pos=vector(0.5*robo_len-inward_castorlength,castor_diameter/2,0),radius=castor_diameter/2,color=color.green)
castor_support1=cylinder(pos=vector(0.5*robo_len-inward_castorlength,castor_diameter/4,0),size=vector(0.8*castor_diameter,castor_diameter,castor_diameter),axis=vector(0,1,0),color=color.yellow)
castor_wheelfront=compound([wheel1,castor_support1])

#To make the castor wheel rear
wheel2=sphere(pos=vector(-0.5*robo_len+inward_castorlength,castor_diameter/2,0),radius=castor_diameter/2,color=color.green)
castor_support2=cylinder(pos=vector(-0.5*robo_len+inward_castorlength,castor_diameter/4,0),size=vector(0.8*castor_diameter,castor_diameter,castor_diameter),axis=vector(0,1,0),color=color.yellow)
castor_wheelrear=compound([wheel2,castor_support2])
system=compound([robot,castor_wheelfront,castor_wheelrear])

#scene.camera.follow(system)
t=0
dt=0.01
tmax=3
velocity=3
#Bot moves forward in x direction
while(t<=tmax):
  rate(1/dt)
  system.pos.x+=velocity*dt
  left_wheel.pos.x+=velocity*dt
  left_wheel.rotate(axis=vector(0,0,-1),angle=velocity*dt/rimradius)
  right_wheel.pos.x+=velocity*dt
  right_wheel.rotate(axis=vector(0,0,-1),angle=velocity*dt/rimradius)
  flipper.pos.x+=velocity*dt
  rak.pos.x+=velocity*dt
  t+=dt
  
# flipperopen()
# flipperclose()

#Bot rotates 90 degrees 
t=0
theta=0
dtheta=0.01
while(theta<=pi/2):
  rate(1/dt)
  system.rotate(axis=vector(0,-1,0),angle=dtheta)
  left_wheel.pos.x=system.pos.x-(0.5*robo_wid)*sin(theta)
  left_wheel.pos.z=0.5*robo_wid*cos(theta)
  left_wheel.rotate(axis=vector(0,-1,0),angle=dtheta)
  left_wheel.rotate(axis=left_wheel.pos-system.pos,angle=velocity*dt/rimradius,origin=left_wheel.pos)
  left_wheel.pos.x-=2*rimthickness

  right_wheel.pos.z=-0.5*robo_wid*cos(theta)
  right_wheel.pos.x=system.pos.x+0.5*robo_wid*sin(theta)
  right_wheel.rotate(axis=vector(0,-1,0),angle=dtheta)
  right_wheel.rotate(axis=system.pos-right_wheel.pos,angle=velocity*dt/rimradius,origin=right_wheel.pos)
  right_wheel.pos.x+=2*rimthickness
  rak.pos.x=system.pos.x-0.5*robo_len*cos(theta)
  rak.pos.z=-0.5*robo_len*sin(theta)
  rak.rotate(axis=vector(0,-1,0),angle=dtheta)
  flipper.rotate(axis=vector(0,-1,0),angle=dtheta)
  theta+=dtheta

flipper.pos.x+=0.5*motor_diameter
t=0
dt=0.01
tmax=3
velocity=3
#Bot moves forward in z direction
while(t<=tmax):
  rate(1/dt)
  system.pos.z+=velocity*dt
  left_wheel.pos.z+=velocity*dt
  left_wheel.rotate(axis=vector(1,0,0),angle=velocity*dt/rimradius)
  right_wheel.pos.z+=velocity*dt
  right_wheel.rotate(axis=vector(1,0,0),angle=velocity*dt/rimradius)
  flipper.pos.z+=velocity*dt
  rak.pos.z+=velocity*dt
  t+=dt

flipperopen()
flipperclose()

t=0
dt=0.01
tmax=3
velocity=3
#Bot moves backward in z direction
while(t<=tmax):
  rate(1/dt)
  system.pos.z-=velocity*dt
  left_wheel.pos.z-=velocity*dt
  left_wheel.rotate(axis=vector(-1,0,0),angle=velocity*dt/rimradius)
  right_wheel.pos.z-=velocity*dt
  right_wheel.rotate(axis=vector(-1,0,0),angle=velocity*dt/rimradius)
  flipper.pos.z-=velocity*dt
  rak.pos.z-=velocity*dt
  t+=dt

#Bot rotates 90 degrees 
t=0
theta=0
dtheta=0.01
while(theta<=pi/2):
  rate(1/dt)
  system.rotate(axis=vector(0,1,0),angle=dtheta)
  left_wheel.pos.x=system.pos.x-(0.5*robo_wid)*cos(theta)
  left_wheel.pos.z=0.5*robo_wid*sin(theta)
  left_wheel.rotate(axis=vector(0,1,0),angle=dtheta)
  left_wheel.rotate(axis=left_wheel.pos-system.pos,angle=velocity*dt/rimradius,origin=left_wheel.pos)
  left_wheel.pos.z+=2*rimthickness

  right_wheel.pos.z=-0.5*robo_wid*sin(theta)
  right_wheel.pos.x=system.pos.x+0.5*robo_wid*cos(theta)
  right_wheel.rotate(axis=vector(0,1,0),angle=dtheta)
  right_wheel.rotate(axis=system.pos-right_wheel.pos,angle=velocity*dt/rimradius,origin=right_wheel.pos)
  right_wheel.pos.z-=2*rimthickness
  rak.pos.x=system.pos.x-0.5*robo_len*sin(theta)
  rak.pos.z=-0.5*robo_wid*cos(theta)
  rak.rotate(axis=vector(0,1,0),angle=dtheta)
  flipper.rotate(axis=vector(0,1,0),angle=dtheta)
  theta+=dtheta

t=0
dt=0.01
tmax=3
velocity=3
#Bot moves backward in x direction
while(t<=tmax):
  rate(1/dt)
  system.pos.x-=velocity*dt
  left_wheel.pos.x-=velocity*dt
  left_wheel.rotate(axis=vector(0,0,1),angle=velocity*dt/rimradius)
  right_wheel.pos.x-=velocity*dt
  right_wheel.rotate(axis=vector(0,0,1),angle=velocity*dt/rimradius)
  flipper.pos.x-=velocity*dt
  rak.pos.x-=velocity*dt
  t+=dt

#End of simulation
