x = 0
y = 0
img = 0
value = 0
xc = 0
def setup():
    global img,xc
    size(600,600)
    img = loadImage('лайк.jpg') 
    xc = loadImage('цветы.jpg')
def draw():
    global x,y
    image(img,100,100,400,500)
    image(xc,50,50,200,200)
   
