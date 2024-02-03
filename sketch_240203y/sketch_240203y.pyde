x = 250
y = 250
bg=255
def setup():
    size(600,600)
def draw():
    global x,y,bg
    background(bg)
    rect(250,250,100,100)
    
def mouseClicked():
    global bg
    if mouseX > 250 and mouseX < 350 and mouseY > 250 and mouseY < 350:
        bg = 0
