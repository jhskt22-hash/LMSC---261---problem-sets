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
    background(255) # clear background for each frame
        
    #1 grid dimensions
    collumns = 10
    rows = 10
        
    #2 define cell width & height
    cell_width = float(width) / collumns
    cell_height = float(height) / rows
        
    #3 calculate scale factor s
        
    s = cell_width / 100.0
        
    #4 nested for loops to set up the tile on the canvas
    for x in range (collumns):
        for y in range(rows):
            pos_x = x * cell_width
            pos_y = y * cell_height
            drawObject(pos_x, pos_y, s) 