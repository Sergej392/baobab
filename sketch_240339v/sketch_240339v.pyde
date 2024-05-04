z = 50
s = 50
r = 200
g = 191
b = 191
def setup():
    size(600,600)
def draw():
    global z,s,r,g,b
    background(0)
    ellipse(300,300,z,s)
if z > 600:
    z = 0
def mouseClicked():
    global z,s,r,g,b
    fill(r,g,b)
    z = z + 10
    s = s + 10
    r = r + 1
    g = g - 10
    b = b - 10
if z > 600:
    z = 0
