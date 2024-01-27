x = 0
dirx=1
def setup():
    size(600,600)
def draw():
    global x,dirx
    background(0)
    ellipse(x,100,100,100)
    
    if mousePressed == True:
        x = x + dirx
        
        if x > 581:
            
            dirx = -1
            
        if x < 0:
            
            dirx = +1
 
