x = 0
y = 300
img=0
def setup():
    global img
    size(600,600)
    img = loadImage('star.png')
def draw():
    global x,y
    background(15,236,242)
    fill(95,94,64)
    rect(x,y,100,100)
    fill(31,242,5)
    rect(0,400,600,200)
    fill(142,142,142)
    rect(400,250,50,15)
    translate(50,0)
    rect(400,250,50,15)
    translate(0,15)
    rect(400,250,50,15)
    translate(50,0)
    rect(400,250,50,15)
    translate(0,-15)
    rect(400,250,50,15)
    translate(-100,15)
    rect(400,250,50,15)
    translate(0,15)
    rect(400,250,50,15)
    translate(50,-0)
    rect(400,250,50,15)
    translate(-100,15)
    rect(400,250,50,15)
    image(img, 60,70,50,50)
    if key == 'w':
        y = y - 1
    if key == 'd':
        x = x + 1
    if key == 'a':
        x = x - 1
    if key == 's':
        y = y + 1
    text(u"you are lose", 300,300)
        
    if x >306:
        noLoop()
        x=x-1
        loop()
        
        
