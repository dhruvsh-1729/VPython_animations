GlowScript 3.1 VPython


support_height=0.2
clearance=1
stack_support_height=6
surrounder_height=10
stack_height=3
stack_width=10
stack_base=box(pos=vec(0,stack_support_height,0),size=vec(15,1,15))
small_clearance=0.1
extrusion_width=0.5
wheel_radius=1
rim_thickness=0.2
rim_radius=wheel_radius+rim_thickness

orig_x_pos=-10
robo_width=9
robo_height=2
y_left=1
from_center=3
link_length=2

support_vector=vec(0.5*stack_base.size.x-clearance,0,0.5*stack_base.size.z-clearance)
support_distance=support_vector.mag
# print(support_distance)

base_cylinders=[cylinder(pos=vector(support_distance*cos(i*pi/2 + pi/4),0,-support_distance*sin(i*pi/2 + pi/4)),
                axis=vec(0,1,0),size=vec(stack_support_height,1,1)) for i in range(4)]

supporters=[cylinder(pos=vector(support_distance*cos(i*pi/2 + pi/4),-0.5*support_height,-support_distance*sin(i*pi/2 + pi/4)),
                axis=vec(0,1,0),size=vec(support_height,2,2)) for i in range(4)]
                
surrounders=[cylinder(pos=vector(support_distance*cos(i*pi/2 + pi/4),stack_support_height+stack_base.size.y-1,-support_distance*sin(i*pi/2 + pi/4)),
                axis=vec(0,1,0),size=vec(surrounder_height,1,1)) for i in range(4)]                
 
stack1=box(pos=vec(0,.5*stack_support_height+stack_base.size.y+stack_height+0.01,0),color=vec(0.81,.46,.13),size=vec(stack_width,stack_height,stack_width)) 
stack2=box(pos=vec(0,.5*stack_support_height+stack_base.size.y+2*stack_height+small_clearance,0),color=vec(0.81,.46,.13),size=vec(stack_width,stack_height,stack_width)) 
stack3=box(pos=vec(0,.5*stack_support_height+stack_base.size.y+3*stack_height+2*small_clearance,0),color=vec(0.81,.46,.13),size=vec(stack_width,stack_height,stack_width)) 
# stacks=[box(pos=vec(0,0.5*support_distance+stack_base.size.y+0.5*(i+1)*(stack_height)+small_clearance,0),size=vec(stack_width,stack_height,stack_width),color=vec(.81,.46,.13)) for i in range(3)]
  
stack_frame=compound([stack_base,base_cylinders[0],base_cylinders[1],
base_cylinders[2],base_cylinders[3],supporters[0],supporters[1],supporters[2],
supporters[3],surrounders[0],surrounders[1],surrounders[2],surrounders[3],
stack1,stack2,stack3])
stack_frame.velocity=vec(0,1,0)

stack_frame1=stack_frame.clone(pos=vec(-30,8.5,-30))

# Now that the stack frame is ready we can make start making the robot and the screw jack

robot_body=box(pos=vec(orig_x_pos,y_left+0.5*robo_height,0),color=color.yellow,size=vec(robo_width,robo_height,robo_width))

gear1=shapes.gear(radius=wheel_radius)
vector_path=[vec(0,0,0),vec(0,0,extrusion_width)]
wheel_l_f=extrusion(pos=vec(orig_x_pos+from_center,0.5*wheel_radius,-0.5*robo_width),path=vector_path,shape=gear1,color=vec(0.5,0.5,0,5))
rim_l_f=ring(pos=vector(orig_x_pos+from_center,0.5*wheel_radius,-0.5*robo_width),axis=vector(0,0,1),radius=rim_radius,thickness=rim_thickness)

wheel_r_f=wheel_l_f.clone(pos=vec(orig_x_pos+from_center,0.5*wheel_radius,0.5*robo_width))
rim_r_f=ring(pos=vector(orig_x_pos+from_center,0.5*wheel_radius,0.5*robo_width),axis=vector(0,0,1),radius=rim_radius,thickness=rim_thickness)

wheel_l_b=wheel_l_f.clone(pos=vec(orig_x_pos-from_center,0.5*wheel_radius,-0.5*robo_width))
rim_l_b=ring(pos=vector(orig_x_pos-from_center,0.5*wheel_radius,-0.5*robo_width),axis=vector(0,0,1),radius=rim_radius,thickness=rim_thickness)

wheel_r_b=wheel_l_f.clone(pos=vec(orig_x_pos-from_center,0.5*wheel_radius,0.5*robo_width))
rim_r_b=ring(pos=vector(orig_x_pos-from_center,0.5*wheel_radius,0.5*robo_width),axis=vector(0,0,1),radius=rim_radius,thickness=rim_thickness)

robot=compound([robot_body,rim_l_f,rim_r_f,rim_l_b,rim_r_b])
wheels=[wheel_l_f,wheel_l_b,wheel_r_f,wheel_r_b]

robot.velocity=vec(2,0,0)
prismatic_joint_height=1

prismatic_joint1=box(pos=vector(orig_x_pos+from_center,0.5*wheel_radius+robot_body.size.y+0.5*prismatic_joint_height,0),size=vector(link_length,prismatic_joint_height,1),color=color.red)
prismatic_joint2=box(pos=vector(orig_x_pos-from_center,0.5*wheel_radius+robot_body.size.y+0.5*prismatic_joint_height,0),size=vector(link_length,prismatic_joint_height,1),color=color.red)


t=0
max=5
dt=0.01

# while(t<=max):
#   rate(1/dt)
#   # stack_frame.pos+=stack_frame.velocity*dt
#   if(robot.pos.x>=0):
#     break
#   else:
#     robot.pos+=robot.velocity*dt
#     for i in range(len(wheels)):
#       wheels[i].pos+=robot.velocity*dt
#       wheels[i].rotate(axis=vec(0,0,-1),angle=(robot.velocity.x/wheel_radius)*dt)

#   t+=dt

link1=box(pos=vec(orig_x_pos,3*sin(orig_theta),0),size=vec(6,0.2,0.2))

link.rotate(axis=vec(0,0,1),angle=-orig_theta)
orig_theta=pi/12
final_theta=pi/6

theta=orig_theta

while(theta<=final_theta):
  rate(1/dtheta)
  
