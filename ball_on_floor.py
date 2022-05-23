GlowScript 3.1 VPython

# basket=box(pos=vec(0,0,0),size=vec(1,2,1),color=color.red)
# ball=sphere(pos=basket.size*0.5,radius=0.5,color=color.yellow)

floor=box(pos=vector(0,-0.5,0),size=vec(100,1,100))

env_a=vec(0.5,-9.81,0)
v=25
angle=60
theta=pi*angle/180
init_v=vec(v*cos(theta),v*sin(theta),0)
coef_of_rest=0.7
ball=sphere(pos=vec(-0.5*floor.size.x,2,0),color=color.red,radius=2,velocity=init_v,make_trail=True,trail_color=color.yellow)
t=0
dt=0.001
tmax=10
# lis=[0]
vel_arrow=arrow(pos=vec(-0.5*floor.size.x,2,0),color=color.yellow,axis=vec(cos(theta),sin(theta),0),length=15)
while(t<=tmax):
  rate(1/dt)
  ball.velocity+=env_a*dt
  ball.pos+=ball.velocity*dt
  vel_arrow.pos=ball.pos
  vel_arrow.axis=ball.velocity
  if(ball.pos.y<ball.radius and ball.pos.x<0.5*floor.size.x):
    ball.velocity.y=-coef_of_rest*ball.velocity.y
    # lis.append(ball.pos.x)
    
  # ball.pos+=init_v*dt
  t+=dt
# print(lis)
