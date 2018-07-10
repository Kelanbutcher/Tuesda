xCoordinate=50
speed=2
ellipseSize=50
yCoordinate=50
ySpeed=2

def setup():
    size (400,400)
def draw():
    background(0)
    global xCoordinate, speed, ellipseSize,yCoordinate,ySpeed
    leftTopBoundary=ellipseSize/2
    rightBottomBoundary=400 - ellipseSize/2
    xCoordinate+= speed
    if xCoordinate >= rightBottomBoundary or  xCoordinate <= leftTopBoundary:
       speed=-speed
    if yCoordinate >= rightBottomBoundary or  yCoordinate <= leftTopBoundary:
            yspeed=-ySpeed
    fill(255,255,0)
    ellipse(xCoordinate,yCoordinate,ellipseSize,ellipseSize)
    yCoordinate+= ySpeed
