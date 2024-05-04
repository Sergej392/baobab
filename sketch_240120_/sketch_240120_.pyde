x = 100
y = 100
img = 0 
value = 0
xc = 0
def setup():
    global img,xc
    size(600,600)
    img = loadImage('say_aaaaaa.jpg') 
    xc = loadImage('very_scary.jpg')
def draw():
    global x,y
    
    
    # img = 0
    # fill(img)
    
def mouseClicked(): 
    global value,img,xc
    # if img == 0:    
    #     img = 255
    # else:
    #     img = 0
    image(img,100,100,400,500)
    image(xc,50,50,200,200)
   
