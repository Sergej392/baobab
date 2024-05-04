y = 300
def setup():
    size(600,600)
def draw():
    global y
    background(0)
    if keyPressed:
        if key == "d":
            rotate(100)
        elif keyCode == DOWN:
            y = y + 1

    ellipse(300,y,300,300)
    ellipse(300,y,250,250)
    ellipse(300,y,200,200)
    ellipse(300,y,150,150)
    ellipse(300,y,100,100)
    ellipse(300,y,50,50)
    ellipse(305,450,10,10)
    ellipse(305,150,10,10)
    ellipse(150,300,10,10)
    ellipse(450,300,10,10)
