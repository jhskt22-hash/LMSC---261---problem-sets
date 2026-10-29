

def setup():
    size(800,800) # canvas is now 400 x 400
    frame_rate(120)
    no_stroke() # Disable drawing of the stroke!
def drawObject(x, y, s,):
    push() # saves current coordinate / style
    translate(x, y) # moves the origin to x,y
    scale(s) # scales the object by factor of the parameter 's'
    
    rotate(frame_count * 0.08 + (x * -0.007**0.9) + (y * -0.004**0.9)) # we use the multiplier of 0.05 to make the spinning a normal rate instead of super fast.
    # we also offset by our x value * 0.007 so that the higher the x value is , the more of an offset there is, creating a 'wave' illusion. I've done the same for Y, to a lesser extent
    for i in range(1):
        r = random(100)
        stroke(r*5)
        line(12, i, 50+r, i)
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
    background(255) # clear background for each frame
    
    #1 grid dimensions
    collumns = 10
    rows = 10
        
    #2 define cell width & height
    cell_width = float(width) /  (collumns * 1.15) # multiply divisor by 1.15 to get the cells to fit properly within the canvas
    cell_height = float(height) / (rows * 1.15)
        
    #3 calculate scale factor s
        
    s = cell_width / 100.0
        
    #4 nested for loops to set up the tile on the canvas
    for x in range (collumns):
        for y in range(rows):
            pos_x = x * cell_width + 90 #to center the notes more in the canvas
            pos_y = y * cell_height + 90 #to center the notes more in the canvas
            drawObject(pos_x, pos_y, s)