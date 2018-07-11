xCoordinate=random(50,200)
yCoordinate=random(50,200)
xspeed=4
ySpeed=9
ellipseSize=20

def setup():
    size (600,800)
    
def draw():
    background(0)
    global xCoordinate, xspeed,yCoordinate,ySpeed,ellipseSize
    
    topBoundary=ellipseSize/2
    bottomBoundary=800 - ellipseSize/2
    
    leftBoundary=ellipseSize/2
    rightBoundary=600 - ellipseSize/2
    
    if yCoordinate >= bottomBoundary or  yCoordinate <= topBoundary:
            ySpeed=-ySpeed
    
    if xCoordinate >= rightBoundary or  xCoordinate <= leftBoundary:
       xspeed=-xspeed
    
    r= random(0,255)       
    xCoordinate+= xspeed
    yCoordinate+= ySpeed
    fill(r,r,90)
    ellipse(xCoordinate,yCoordinate,ellipseSize,ellipseSize)
    
