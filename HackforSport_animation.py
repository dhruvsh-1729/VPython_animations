GlowScript 3.1 VPython

robot=box(pos=vector(5,1,0),size=vec(4,1,3),color=color.red,velocity=4)
glass=cylinder(pos=vector(5,.5+1,0),size=vec(2,0.5,0.5),color=color.yellow,axis=vec(0,1,0))

seat_cover=box(pos=vec(-5,4,0),color=color.blue,size=vec(5,0.4,6))
seat_back=box(pos=vec(-5,7,0),color=color.blue,size=vec(5,6,0.4))
support1=cylinder(pos=vec(-2.7,0,2.7),size=vec(3.8,0.5,0.5),axis=vec(0,1,0))
support2=cylinder(pos=vec(-2.7,0,-2.7),size=vec(3.8,0.5,0.5),axis=vec(0,1,0))
support3=cylinder(pos=vec(-2.7-5,0,2.7),size=vec(3.8,0.5,0.5),axis=vec(0,1,0))
support4=cylinder(pos=vec(-2.7-5,0,-2.7),size=vec(3.8,0.5,0.5),axis=vec(0,1,0))

door1=box(pos=vector(-5+2.5/2,1.9,2.7),size=vec(2.5,3.4,0.2))
door2=box(pos=vector(-5-2.5/2,1.9,2.7),size=vec(2.5,3.4,0.2))
rail1=box(pos=vector(0,0,1.5),size=vec(10,0.2,0.2))
rail2=box(pos=vector(0,0,-1.5),size=vec(10,0.2,0.2))
t=0
dt=0.01

while(robot.pos.x>seat_cover.pos.x):
  rate(1/dt)
  robot.pos.x-=robot.velocity*dt
  glass.pos.x-=robot.velocity*dt
  
  t+=dt
t=0
while(door1.pos.x<support1.pos.x+0.5*door1.size.x):
  rate(1/dt)
  door1.pos.x+=robot.velocity*dt
  door2.pos.x-=robot.velocity*dt
  
  t+=dt
t=0
while(robot.pos.z<4):
  rate(1/dt)
  robot.pos.z+=robot.velocity*dt
  glass.pos.z+=robot.velocity*dt
  t+=dt
