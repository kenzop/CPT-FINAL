def setup():
    global MEGAMAN_POSITION, PAGE, LEVEL, rectx, recty, title_background, instructions_background, logo
    global megaman_jump_left, megaman_jump_right, megaman_still_left, megaman_still_right, zero_deaths
    size(1280, 480)
    MEGAMAN_POSITION = [50, 300]
    PAGE = 1
    LEVEL = 1
    rectx = 200
    recty = 100
    title_background = loadImage('title_screen.jpg')
    title_background.resize(1280, 480)
    instructions_background = loadImage('instructions_background.png')
    instructions_background.resize(1280, 480)
    logo = loadImage('megaman_logo.png')
    logo.resize(400, 180)
    zero_deaths = loadImage('zero_deaths.jpeg')
    zero_deaths.resize(75, 75)
    megaman_jump_left = loadImage('jump_left.png')
    megaman_jump_left.resize(200, 100)
    megaman_jump_right = loadImage('jump_right.png')
    megaman_jump_right.resize(200, 100)
    megaman_still_left = loadImage('still_left.png')
    megaman_still_left.resize(200, 100)
    megaman_still_right = loadImage('still_right.png')
    megaman_still_right.resize(200, 100)


# Used to track user inputs and move megaman accordingly
def keyPressed():
    global MEGAMAN_POSITION
    if keyCode == RIGHT:
        MEGAMAN_POSITION[0] += 3
    if keyCode == LEFT:
        MEGAMAN_POSITION[0] -= 3


# Used to check the mouse's location.  This is used on the intro screen 
# to either take the player to the main game or to the instructions
def mousePressed():
    global rectx, recty, PAGE
    if PAGE == 1 and mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and mouseY > height-200 and mouseY <height+recty:
        PAGE = 3
    if PAGE == 1 and mouseX > width-2*rectx and mouseX < width-rectx and mouseY > height-200 and mouseY <height-recty:
        PAGE = 2
    if PAGE == 2 and mouseX > width/2-rectx/2 and mouseX < width/2+rectx/2 and mouseY > height-125 and mouseY < height-125+recty:
        PAGE = 3


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

    if mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and mouseY > height-200 and mouseY < height-recty:
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
    # The instructions
    global rectx, recty
    background(instructions_background)
    textSize(16)
    fill(255)
    text("Help Megaman defeat Dr. Wily and save the world!", 250, 100)
    text("Press the left and right arrow keys to move and the up key to jump.", 250, 175)
    text("Press the space bar to shoot enemies out of the way.  Be careful though, some enemies can't be killed.", 250, 250)
    text("Can you beat the game with zero deaths?", 250, 325) 

# Code for start button in the instructions menu
    fill(255,255,0)
    rect(width/2-rectx/2, height-125, rectx, recty, 5)  
    fill(218,112,214)
    text("Click here to Start", width/2-rectx+130, height/2+recty+75)
    if mouseX > width/2-rectx/2 and mouseX < width/2+rectx/2 and mouseY > height-125 and mouseY < height-125+recty:
        fill(255, 219, 88)
        rect(width/2-rectx/2, height-125, rectx, recty, 5)  
        fill(218,112,214)
        text("Click here to Start", width/2-rectx+130, height/2+recty+75)


def level1_spikes(x, y, mid):
    fill(255) #CHANGE
    for spike in range(10):
        triangle(x, y, x+2*mid, y, x+mid, y-mid*2)
        x += 2*mid


def page3():
    background(0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], 50, 50)
    level1_spikes(150, 350, 10)
        
        
def draw():
    if PAGE == 1:
        page1()
    elif PAGE == 2:
        page2()
    elif PAGE == 3:
        page3()
