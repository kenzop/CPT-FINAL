def setup():
    global MEGAMAN_POSITION, PAGE, LEVEL, TIMER, RESET_TIMER, DEATHS, GRAVITY, LEFT_PRESSED, FLOOR
    global RIGHT_PRESSED, UP_PRESSED, rectx, recty, title_background, instructions_background, logo
    global zero_deaths, megaman_spawn_points, on_screen_bullet, bulletX, bulletY, bullet_size, bullet_timer, draw_bullet
    global unkillable, unkillable_enemies, unkillable_enemies_size, megaman_size, unkillable_enemies_spawn_points
    global in_air, airtime, floor_collision, saw1_X, saw1_Y, saw1_up, saw_size
    size(1280, 480)
    noStroke()
    FLOOR = [300]
    MEGAMAN_POSITION = [50, FLOOR[0]]
    PAGE = 1
    LEVEL = 1
    TIMER = [151, 201]
    RESET_TIMER = TIMER[:]
    DEATHS = 0
    GRAVITY = 5
    in_air = False
    airtime = 0
    floor_collision = False
    LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED = False, False, False
    bulletX = MEGAMAN_POSITION[0]
    bulletY = MEGAMAN_POSITION[1]
    bullet_timer = 0
    bullet_size = 10
    rectx = 200
    recty = 100
    saw1_X = 1000
    saw1_Y = 100
    saw1_up = False
    saw_size = 100
    megaman_spawn_points = [50, FLOOR[0]]
    title_background = loadImage('title_screen.jpg')
    title_background.resize(1280, 480)
    instructions_background = loadImage('instructions_background.png')
    instructions_background.resize(1280, 480)
    logo = loadImage('megaman_logo.png')
    logo.resize(400, 180)
    on_screen_bullet = False
    draw_bullet = False
    zero_deaths = loadImage('zero_deaths.jpeg')
    zero_deaths.resize(75, 75)
    megaman_size = 50
    unkillable_enemies_size = 50
    unkillable = loadImage('unkillable.png')
    unkillable.resize(unkillable_enemies_size, unkillable_enemies_size)
    unkillable_enemies = [[800, FLOOR[0]], [700, 250], [800, 300]]
    unkillable_enemies_spawn_points = [[800, FLOOR[0]], [700, 250], [800, 300]]
    
    
# Used to track user inputs and move megaman accordingly
def keyPressed():
    global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED, MEGAMAN_POSITION, on_screen_bullet, in_air
    if keyCode == RIGHT:
        RIGHT_PRESSED = True
    elif keyCode == LEFT:
        LEFT_PRESSED = True
    if keyCode == UP:
        in_air = True
    if keyCode == 32:
        on_screen_bullet = True
'''
TESTING ONLY
    if keyCode == DOWN:
        MEGAMAN_POSITION[1] += 3
'''

def keyReleased():
    global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED
    if keyCode == RIGHT:
        RIGHT_PRESSED = False
    elif keyCode == LEFT:
        LEFT_PRESSED = False


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
    text("(UNKILLABLE)", 1075, 210)
    image(unkillable, 1100, 225)


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
    global MEGAMAN_POSITION, DEATHS, unkillable_enemies, TIMER, bullet_timer, on_screen_bullet, draw_bullet
    noFill()
    rect(x, y-2*mid, 1.35*x, 2*mid)
    fill(211,211,211)
    for spike in range(10):
        triangle(x, y, x+2*mid, y, x+mid, y-mid*2)
        x += 2*mid

    # Hitbox for spikes.  NOTE: Since the player is not able to clip through the 
    # floor, the collision continues below the spikes all the way to infinity
    if MEGAMAN_POSITION[0] > x/3.5 and MEGAMAN_POSITION[0] < x and MEGAMAN_POSITION[1] > y/1.25:        
        in_air = False
        airtime = 0
        MEGAMAN_POSITION = megaman_spawn_points[:]
        unkillable_enemies[0][0] = unkillable_enemies_spawn_points[0][0]
        DEATHS += 1
        TIMER[0] = RESET_TIMER[0]
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False


def level1_saw(x, y):
    global MEGAMAN_POSITION, DEATHS, TIMER, saw1_Y, saw1_up, bullet_timer, on_screen_bullet, draw_bullet
    # draw saw
    fill(211,211,211)
    ellipse(x, y, saw_size, saw_size)
    # saw movement
    if saw1_up == False:
        saw1_Y += 1
        if saw1_Y >= 300:
            saw1_up = True
    if saw1_up == True:
        saw1_Y -= 1
        if saw1_Y < 50:
            saw1_up = False
    
    
    # saw hitbox
    if MEGAMAN_POSITION[0]+megaman_size > saw1_X and MEGAMAN_POSITION[0] < saw1_X + saw_size and MEGAMAN_POSITION[1] < saw1_Y + saw_size/2 and MEGAMAN_POSITION[1] > saw1_Y - saw_size:
        in_air = False
        airtime = 0
        MEGAMAN_POSITION = megaman_spawn_points[:]
        unkillable_enemies[0][0] = unkillable_enemies_spawn_points[0][0]
        DEATHS += 1
        TIMER[0] = RESET_TIMER[0]
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False

def unkillable_enemy1_hitbox():
    # If the player hits the enemy, they die, the level resets, and the death counter increments
    global MEGAMAN_POSITION, DEATHS, TIMER, unkillable_enemies, bullet_timer, on_screen_bullet, draw_bullet
    if MEGAMAN_POSITION[0]+megaman_size/1.25 >= unkillable_enemies[0][0] and MEGAMAN_POSITION[0]/0.99 <= unkillable_enemies[0][0]+unkillable_enemies_size and MEGAMAN_POSITION[1] > unkillable_enemies[0][1]-unkillable_enemies_size and MEGAMAN_POSITION[1] < unkillable_enemies[0][1]+unkillable_enemies_size:
        MEGAMAN_POSITION = megaman_spawn_points[:]
        unkillable_enemies[0][0] = unkillable_enemies_spawn_points[0][0]
        DEATHS += 1
        TIMER[0] = RESET_TIMER[0]
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False
    
    # If the bullet hits this enemy, the bullet despawns and the enemy is left untouched
    if bulletX >= unkillable_enemies[0][0] and bulletX <= unkillable_enemies[0][0]+unkillable_enemies_size and bulletY <= unkillable_enemies[0][1]+bullet_size and bulletY > unkillable_enemies[0][1]-bullet_size:
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False

   
def level1():
    global LEVEL, PAGE, DEATHS, TIMER, MEGAMAN_POSITION, unkillable_enemies, unkillable_enemies_spawn_points, megaman_spawn_points, bullet_timer, on_screen_bullet, draw_bullet
    background(0)
    fill(255)
    text("DEATHS:" + str(DEATHS), 10, 15)
    text("TIMER:" + str(int(TIMER[0])), 100, 15)
    rect(0, 350, width, height)
    fill(255,0,0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], megaman_size, megaman_size)
    level1_spikes(150, 350, 10)
    level1_saw(saw1_X, saw1_Y)
    # Unkillable enemy and its hitbox
    image(unkillable, unkillable_enemies[0][0], unkillable_enemies[0][1])
    unkillable_enemies[0][0] -= 1
    unkillable_enemy1_hitbox()
    TIMER[0] -= 0.1
    
    if TIMER[0] <= 0:
        DEATHS += 1
        TIMER[0] = RESET_TIMER[0]
        MEGAMAN_POSITION = megaman_spawn_points[:]
        unkillable_enemies[0][0] = unkillable_enemies_spawn_points[0][0]
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False
    
    if draw_bullet == True:
        fill(255)
        rect(bulletX, bulletY, bullet_size, bullet_size)
            
    if MEGAMAN_POSITION[0] > 1200:
        LEVEL = 2
        draw_bullet = False
        on_screen_bullet = False
        bullet_timer = 0
        MEGAMAN_POSITION = megaman_spawn_points[:]
               
def level2():
    global LEVEL, PAGE, DEATHS, TIMER, MEGAMAN_POSITION, unkillable_enemies, unkillable_enemies_spawn_points, megaman_spawn_points, bullet_timer, on_screen_bullet, draw_bullet
    background(255)
    fill(0)
    text("DEATHS:" + str(DEATHS), 10, 15)
    text("TIMER:" + str(int(TIMER[1])), 100, 15)
    rect(0, 350, width, height)
    fill(255,0,0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], megaman_size, megaman_size)
    TIMER[1] -= 0.1
    
    if TIMER[1] <= 0:
        DEATHS += 1
        TIMER[1] = RESET_TIMER[1]
        MEGAMAN_POSITION = megaman_spawn_points[:]
        unkillable_enemies[0][0] = unkillable_enemies_spawn_points[0][0]
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False
    
    if draw_bullet == True:
        fill(255)
        rect(bulletX, bulletY, bullet_size, bullet_size)
   
    '''        
    if MEGAMAN_POSITION[0] > 1200:
        LEVEL = 3
        draw_bullet = False
        on_screen_bullet = False
        bullet_timer = 0
    '''    
           
def page3():
    global LEVEL, PAGE, MEGAMAN_POSITION, bulletX, bulletY, on_screen_bullet, bullet_timer, draw_bullet
    global in_air, airtime
    if RIGHT_PRESSED == True:
        MEGAMAN_POSITION[0] += 3
    if LEFT_PRESSED == True and MEGAMAN_POSITION[0] > 0:
        MEGAMAN_POSITION[0] -= 3
    if in_air == True:
        airtime += 0.2
        if airtime > 10:
            MEGAMAN_POSITION[1] += 1
            if LEVEL == 1 and MEGAMAN_POSITION[1] > FLOOR[0]: 
                airtime = 0
                in_air = False
                MEGAMAN_POSITION[1] = FLOOR[0]
        else:
            MEGAMAN_POSITION[1] -= 2

    if on_screen_bullet == False:
        bulletX = MEGAMAN_POSITION[0]
        bulletY = MEGAMAN_POSITION[1]
        
    if on_screen_bullet == True:
        draw_bullet = True
        bulletX += 8
        bullet_timer += 1
        if bullet_timer > 100:
            bulletX = MEGAMAN_POSITION[0]
            bulletY = MEGAMAN_POSITION[1]
            draw_bullet = False
            on_screen_bullet = False
            bullet_timer = 0
    print(LEVEL)
   
    if LEVEL == 1:
        level1()
         
    if LEVEL == 2:
        level2()
        
def draw():
    global DEATHS
    if PAGE == 1:
        page1()
        DEATHS = 0
    elif PAGE == 2:
        page2()
    elif PAGE == 3:
        page3()
