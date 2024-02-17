x = 300
y = 300
def setup():
    size(600,600)
def draw():
    global x,y
    background(0)
    ellipse(mouseX,mouseY,100,100)
    translate(30,0)
    ellipse(mouseX,mouseY,50,100)
    translate(-70,0)
    ellipse(mouseX,mouseY,50,100)
    translate(60,60)
    ellipse(mouseX,mouseY,50,100)
    translate(-60,0)
    ellipse(mouseX,mouseY,50,100)
    translate(60,-70)
    ellipse(mouseX,mouseY,50,100)
def mouseClicked():
    if mousePressed == True:
        translate(600,600)
        
