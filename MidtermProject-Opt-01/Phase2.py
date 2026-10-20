

def setup():
    size(150,150) # canvas is 150 x 150
    no_stroke() # Disable drawing of the stroke!
def draw():
    fill(0) # fill all shapes that are drawn with black color
    rect(40, 10, 60, 10) # Draw rectangles
    rect(40, 10, 5, 50)
    rect(100, 10, 5, 50)
    
    # left note head color!
    fill(230, 0, 90)
    ellipse(30, 60, 30, 20)
    
    # right note head color!
    fill(255, 20, 147)
    ellipse(90, 60, 30, 20)