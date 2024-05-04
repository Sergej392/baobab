y = 0
dirY = 1
def setup():
    size(600,600)
def draw():
    global y,dirY
    background(0)
    ellipse(300,y,100,100)
    y = y + dirY
    if y == 590:
        dirY = -1
    if y == 0:
        dirY = 1
