s = 0
w = 0
def setup():
    size(600,600)
def draw():
    global s,w
    background(0)
    ellipse(300,300,s,w)
    if keyPressed==True:
        if key=='s':
            
