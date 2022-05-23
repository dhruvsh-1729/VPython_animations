GlowScript 3.1 VPython

ball=sphere(pos=vec(10,0,0),mass=1,eq_pos=vec(7,0,0),color=color.red,velocity=vec(0,0,0),a=vec(0,0,0))
wall=box(pos=vec(-0.5,0,0),size=vec(1,2,2))
spring=helix(pos=vec(0,0,0),coils=10,stiffness=2,axis=vec(-1,0,0))
vel_arrow=arrow(pos=vector(10,0,0),axis=vector(1,0,0))
acc_arrow=arrow(pos=vector(10,0,0),axis=vector(1,0,0),color=color.yellow)
t=0
dt=0.01
tmax=50

g_ball=sphere(pos=vec(-3,-10,0),mass=1,eq_pos=vec(-3,-10,0),color=color.yellow,velocity=vec(0,0,0),a=vec(0,0,0),g=vec(0,-9.81,0))
wall2=box(pos=vec(-3,0.5,0),size=vec(2,1,2))
spring2=helix(pos=vec(-3,0,0),coils=20,stiffness=5,axis=vec(0,1,0))
# vel_arrow=arrow(pos=vector(10,0,0),axis=vector(1,0,0))
# acc_arrow=arrow(pos=vector(10,0,0),axis=vector(1,0,0),color=color.yellow)


while(t<=tmax):
  rate(1/dt)
  spring_force=-spring.stiffness*(ball.pos-ball.eq_pos)
  ball.a=spring_force/ball.mass
  ball.velocity+=ball.a*dt
  ball.pos+=ball.velocity*dt
  vel_arrow.pos=ball.pos
  vel_arrow.axis=ball.velocity
  acc_arrow.pos=ball.pos
  acc_arrow.axis=ball.a
  spring.axis.x=ball.pos.x
  
  force=-spring2.stiffness*(g_ball.pos-g_ball.eq_pos)+g_ball.mass*g_ball.g
  g_ball.a=force/g_ball.mass
  g_ball.velocity+=g_ball.a*dt
  g_ball.pos+=g_ball.velocity*dt
  spring2.axis.y=g_ball.pos.y
  t+=dt
  
