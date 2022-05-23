GlowScript 2.9 VPython

wall1=box(pos=vector(5,0,0),size=vector(.2,10,10),color=color.yellow)
wall2=wall1.clone(pos=vector(-5,0,0))

wall3=box(pos=vector(0,5,0),size=vector(10,.2,10),color=color.green)
wall4=wall3.clone(pos=vector(0,-5,0))

wall6=box(pos=vector(0,0,-5),size=vector(10,10,.2))
wall5=wall6.clone(pos=vector(0,0,5),opacity=0.1)

gdisplay(xtitle="Time",ytitle="No.of collisions")
curve=gcurve(color=color.red,label="No.of collisions")

atoms=[]
num=30
inp=4
for i in range(0,num):
  atoms.append(sphere(pos=vector(-4+random()*7,-4+random()*7,-4+random()*7),radius=0.25,color=color.red,velocity=vector(random()*20,random()*20,random()*20),make_trail=False,trail_color=color.blue,retain=1000))
  if(i==inp):
    atoms[i].make_trail=False
count=0
t=0
dt=0.01
count=0
while(True):
  rate(1/dt)
  t+=dt
  for i in range(0,num):
    for j in range(0,num):
      if(i==j):
        continue
       
      if(i!=j):
        if(mag(atoms[i].pos-atoms[j].pos)<atoms[i].radius+atoms[j].radius):
          atoms[i].velocity=-atoms[i].velocity
          atoms[j].velocity=-atoms[j].velocity
          count+=1
          #print(count)
      
  for i in range(0,num):
    atoms[i].pos=atoms[i].pos+atoms[i].velocity*dt
    if(atoms[i].pos.x-atoms[i].radius>wall1.pos.x-0.5*wall1.size.x):
      atoms[i].pos.x-atoms[i].radius==wall1.pos.x-0.5*wall1.size.x
      atoms[i].velocity.x=-atoms[i].velocity.x
    if(atoms[i].pos.y-atoms[i].radius>wall3.pos.y-0.5*wall3.size.y):
      atoms[i].pos.y-atoms[i].radius==wall1.pos.y-0.5*wall1.size.y
      atoms[i].velocity.y=-atoms[i].velocity.y  
    if(atoms[i].pos.z-atoms[i].radius>wall5.pos.z-0.5*wall5.size.z):
      atoms[i].velocity.z=-atoms[i].velocity.z
      atoms[i].pos.z-atoms[i].radius==wall1.pos.z-0.5*wall1.size.z
      
    if(atoms[i].pos.x+atoms[i].radius<wall2.pos.x+.5*wall2.size.x):
      atoms[i].pos.x+atoms[i].radius==wall2.pos.x+.5*wall2.size.x
      atoms[i].velocity.x=-atoms[i].velocity.x
    if(atoms[i].pos.y+atoms[i].radius<wall4.pos.y+.5*wall4.size.y):
      atoms[i].pos.y+atoms[i].radius==wall2.pos.x+.5*wall2.size.y
      atoms[i].velocity.y=-atoms[i].velocity.y  
    if(atoms[i].pos.z+atoms[i].radius<wall6.pos.z+.5*wall6.size.z):
      atoms[i].pos.z+atoms[i].radius==wall2.pos.z+.5*wall2.size.z
      atoms[i].velocity.z=-atoms[i].velocity.z
  curve.plot(t,count)
      

      
      
    
      
    
      
      
      
