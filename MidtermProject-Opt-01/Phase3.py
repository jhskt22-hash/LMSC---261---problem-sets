

def setup():
    size(400,400) # canvas is now 400 x 400
    no_stroke() # Disable drawing of the stroke!
def drawObject(x, y, s):
    push() # saves current coordinate / style
    translate(x, y) # moves the origin to x,y
    scale(s) # scales the object by factor of the parameter 's'
    
    # phase 2 drawing code:
    fill(0) # fill all shapes that are drawn with black color unless otherwise specified
    rect(40, 10, 60, 10) # Draw rectangles
    rect(40, 10, 5, 50)
    rect(100, 10, 5, 50)
    
    # left note head color!
    fill(230, 0, 90)
    ellipse(30, 60, 30, 20)
    
    # right note head color!
    fill(255, 20, 147)
    ellipse(90, 60, 30, 20)
    
    #---------------------------------------
    
    pop() # restore previous coordinate system and style that was saved using push()
    
def draw():
    drawObject(0, 0, 1) # draws at original scale at top left, referencing (x, y, s) for origin position (0, 0) and scale (1) respectively.
    drawObject(100, 100, 2) # draws the object at a different scale and origin position to verify isolation
    drawObject(50, 240, 0.7) # draws a third smaller note, for verification, again.