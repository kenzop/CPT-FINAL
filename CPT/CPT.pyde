def setup():
    global MEGAMAN_POSITION, PAGE, rectx, recty, title_background, logo
    size(1280, 480)
    MEGAMAN_POSITION = [50, 300]
    PAGE = 1
    rectx = 200
    recty = 100
    title_background = loadImage('title_screen.jpg')
    title_background.resize(1280, 480)
    logo = loadImage('megaman_logo.png')
    logo.resize(400, 180)

# Used to track user inputs and move megaman accordingly
def keyPressed():
    global MEGAMAN_POSITION
    if keyCode == RIGHT:
        MEGAMAN_POSITION[0] += 2
    if keyCode == LEFT:
        MEGAMAN_POSITION[0] -= 2


# Used to check the mouse's location.  This is used on the intro screen 
# to either take the player to the main game or to the instructions
def mousePressed():
    global rectx, recty, PAGE
    if PAGE == 1 and mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        PAGE = 3
    
    if mouseX > width-2*rectx and mouseX < width-rectx and mouseY > height-200 and mouseY <height-recty:
        PAGE = 2
           
def page1():
    background(title_background)
    image(logo, width/2-200, height-400)
    # Code for start button.  Changes color to a darker shade of green if the
    # mouse hovers over it
    fill(0, 255, 0)
    rect(width/4-(rectx/2), height-200, rectx, recty, 5)
    textSize(16)
    fill(255)
    text("Click here to Start", rectx+50, height-recty-40)

    if mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and mouseY > height-200 and mouseY <height-recty:
        fill(0,128,0)
        rect(width/4-(rectx/2), height-200, rectx, recty, 5)
        fill(255)
        textSize(16)  
        text("Click here to Start", rectx+50, height-recty-40)
    
    # Code for Instructions button.  Changes color to a darker shade of red
    # if the mouse hovers over it
    fill(255, 0, 0)
    rect(width-2*rectx, height-200, rectx, recty, 5)  
    textSize(14)  
    fill(255)
    text("Click here for Instructions", width/2+rectx+55, height-recty-40)
    if mouseX > width-2*rectx and mouseX < width-rectx and mouseY > height-200 and mouseY <height-recty:
        fill(153, 0 ,0)
        rect(width-2*rectx, height-200, rectx, recty, 5)  
        fill(255)
        textSize(14)  
        text("Click here for Instructions", width/2+rectx+55, height-recty-40)


def page2():
    pass

def draw():
    if PAGE == 1:
        page1()
    elif PAGE == 2:
        page2()
    elif PAGE == 3:
        background(0)
        rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], 20, 20)
