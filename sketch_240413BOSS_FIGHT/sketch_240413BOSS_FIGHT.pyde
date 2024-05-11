x = 50
y = 350
img=0
z = 250
c = 0
def collideRectRect(x,y,shirina,dlina,x1,y1,shirina1,dlina1):
    if (x + shirina >= x1) and (x <= x1 + shirina1) and (y + dlina >= y1) and (y <= y1 + dlina1):
        return True
    else:
        return False
    
def setup():
    global img,omg
    size(600,600)
    img = loadImage('s.jpg')
    omg = loadImage('angry_emoji.jpg')
def draw():
    global x,y,img,omg
    image(img,0,0,600,600)
    fill(20,255,0)
    rect(0,450,700,599)
    fill(255,0,0)
    rect(x,y,100,100)
    fill(20,255,0)
    rect(0,0,5,450)
    rect(597,0,5,450)
    image(omg,z,c,150,150)
    if keyPressed==True:
        if key == 'w' or key == 'ц':
            y = y - 4
            if collideRectRect(0,0,5,450,x,y,100,100):
                y=y+5
            else:
                fill(255)
        if key == 'd' or key == 'в':
        
        
            x = x + 4
            if collideRectRect(597,0,5,450,x,y,100,100):
                x=x-5
            else:
                fill(255) 
        if key == 'a' or key == 'ф':
            x = x - 4
            if collideRectRect(0,0,5,450,x,y,100,100):
                x=x+5
            else:
                fill(255) 
        if key == 's' or key == 'ы':
            y = y + 4
            if collideRectRect(0,0,5,450,x,y,100,100):
                y=y-5
                
            if y>350:
                y=350
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
