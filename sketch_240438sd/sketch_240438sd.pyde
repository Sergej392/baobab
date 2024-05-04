def collideRectCircle(rx,ry,rw,rh,cx,cy,diameter):
    testX = cx
    testY = cy
  
    if cx < rx:
        testX = rx
    elif cx > rx+rw:
        testX = rx + rw
    if cy < ry:
        testY = ry
    elif cy > ry+rh:
        testY = ry+rh
    
    distance = dist(cx,cy,testX,testY)
 
    if distance <= diameter/2:
        return True
    else:
        return False

shar_x = 0       
shar_y = 0
shar_dx = 0
shar_dy = 0
ladder_x = 0
ladder_y = 0
shar_razmer = 0
ladder_width = 0
ladder_height = 0
def setup():
    size(600,400)
def draw():
    global ladder_x,ladder_y,ladder_width,ladder_height,shar_x,shar_y,shar_razmer,shar_dx,shar_dy
    background(100)
    if collideRectCircle(300,200,100,50,mouseX,mouseY,100):
        fill(255,0,0)
    else:
      fill(255)
    rect(300,200,100,50)
    ellipse(mouseX,mouseY,100,100)
    
    shar_x = shar_x + shar_dx 
    shar_y = shar_y + -shar_dy
      
if shar_x > 580:
    
    shar_dx = shar_dx
if shar_x < 20:
    
    shar_dx=-shar_dx
if keyPressed==True: 
    if key == CODED:
        if keyCode == LEFT:
            ladder_x = ladder_x - 4
        if keyCode == RIGHT:    
            ladder_x = ladder_x + 4
if collideRectCircle(ladder_x,ladder_y,ladder_width,ladder_height,shar_x,shar_y,shar_razmer):
    shar_dy = -random(4,6)
    shar_dx = random(-5,5)
