a=0
v=0
h=0
def setup():
    size(600,600)
def draw():
    global a,v,h 
    background(34,234,21)
    fill(214,232,21)
    rect(20,150,150,350)
    fill(a,v,h)
    rect(220,150,150,350)
    fill(252,8,0)
    rect(420,150,150,350)
    text(u"g", 150,350)
    text(u"w", 220,150)
    text(u"r",420,150)
    if keyPressed==True:
        if key=='g':
            clear()
        if key=='w':
            a=255
            v=0
            h=0
            
        if key=='k':
            a=0
            v=255
            h=0
