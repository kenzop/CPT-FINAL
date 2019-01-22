def setup():
    # Size, noFill and 99% of variables are declared in the setup function
    global MEGAMAN_POSITION, PAGE, LEVEL, TIMER, RESET_TIMER, DEATHS, GRAVITY
    global LEFT_PRESSED, FLOOR, RIGHT_PRESSED, UP_PRESSED, rectx, recty, stars
    global title_background, instructions_background, logo, zero_deaths
    global megaman_spawn_points, on_screen_bullet, bulletX, bulletY
    global bullet_size, bullet_timer, draw_bullet, unkillable
    global unkillable_enemies, unkillable_enemies_size, megaman_size
    global unkillable_enemies_spawn_points, in_air, airtime, floor_collision
    global saw1_X, saw1_Y, saw1_up, saw_size, secret, unkillable_enemy1_up
    global unkillable_enemy2_up, enemy, enemy_spawn_point, enemy_size
    global enemy_dead, shooter, shooter_size, shooter_bullet, shooter_bulletX
    global shooter_bulletY, shooter_bullet_timer, draw_shooter_bullet
    global megaman_spawn_point_boss, boss, boss_size, drop_timer, boss_left
    global boss_timer, boss_tracker, boss_spawn_point, boss_hits
    global congratulations

    size(1280, 480)
    noStroke()
    import random

    # Used to draw stars. This code is used in the draw_stars function
    stars = []
    add_star = 0
    # while loop is used instead of a for loop due to the lack of while
    # loops in the program and the lack of places where a while loop
    # would be optimal
    while add_star < 201:
        stars.append([random.randint(1, 1280), random.randint(1, 350)])
        add_star += 1

    FLOOR = 300
    MEGAMAN_POSITION = [50, FLOOR]
    PAGE = 1
    LEVEL = 1
    TIMER = [151, 101, 101, 801]
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
    unkillable_enemy1_up, unkillable_enemy2_up = False, True
    saw_size = 100
    megaman_spawn_points = [50, FLOOR]
    title_background = loadImage('title_screen.jpg')
    title_background.resize(1280, 480)
    instructions_background = loadImage('instructions_background.png')
    instructions_background.resize(1280, 480)
    logo = loadImage('megaman_logo.png')
    logo.resize(400, 180)
    on_screen_bullet = False
    draw_bullet = False
    zero_deaths = loadImage('zero_deaths.jpeg')
    zero_deaths.resize(450, 500)
    congratulations = loadImage('congratulations.PNG')
    megaman_size = 50
    unkillable_enemies_size = 50
    unkillable = loadImage('unkillable.png')
    unkillable.resize(unkillable_enemies_size, unkillable_enemies_size)
    unkillable_enemies = [[800, FLOOR], [700, 250], [1000, 100]]
    unkillable_enemies_spawn_points = ([[800, FLOOR], [700, 250],
                                        [1000, 100]])
    enemy = [600, FLOOR]
    enemy_size = 50
    enemy_spawn_point = [600, FLOOR]
    enemy_dead = False
    shooter = [[1000, FLOOR], [50, FLOOR], [1100, FLOOR]]
    shooter_size = 50
    shooter_bullet = [False, False, False]
    draw_shooter_bullet = [False, False, False]
    shooter_bulletX = [1000, 50, 1100]
    shooter_bulletY = FLOOR
    shooter_bullet_timer = [0, 0, 0]
    megaman_spawn_point_boss = [width/2, FLOOR]
    boss = [width/2, 50]
    boss_size = 50
    boss_left = False
    drop_timer = 0
    boss_timer = 0
    boss_tracker = 0
    boss_spawn_point = [width/2, 50]
    boss_hits = 0
    secret = False


# Used to track user inputs and move megaman accordingly
def keyPressed():
    # Checks if the user has pressed a key. This determines if the
    # player can either move, shoot, or jump
    global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED
    global MEGAMAN_POSITION, on_screen_bullet, in_air
    if keyCode == RIGHT:
        RIGHT_PRESSED = True
    elif keyCode == LEFT:
        LEFT_PRESSED = True
    if keyCode == UP:
        in_air = True
    if keyCode == 32:
        on_screen_bullet = True


def keyReleased():
    # Used to make mobility a little more flowing and natural
    global LEFT_PRESSED, RIGHT_PRESSED, UP_PRESSED
    if keyCode == RIGHT:
        RIGHT_PRESSED = False
    elif keyCode == LEFT:
        LEFT_PRESSED = False


# Used to check the mouse's location.  This is used on the intro screen
# to either take the player to the main game or to the instructions
# and on the instuctions screen to warp you to either warp you to
# the begining of the game, or to the secret boss warp screen
def mousePressed():
    global rectx, recty, PAGE
    if (PAGE == 1 and mouseX > width/4-(rectx/2) and
        mouseX < width/4+(rectx/2) and mouseY > height-200 and
            mouseY < height-recty):
        PAGE = 3
    if (PAGE == 1 and mouseX > width-2*rectx and mouseX < width-rectx and
            mouseY > height-200 and mouseY < height-recty):
        PAGE = 2
    if (PAGE == 2 and mouseX > width/2-rectx/2 and mouseX < width/2+rectx/2 and
            mouseY > height - 125 and mouseY < height-125 + recty):
        PAGE = 3
    if (PAGE == 2 and mouseX > 1075 and mouseX < 1175 and mouseY > 200 and
            mouseY < 210):
        PAGE = 6


# Used to determine if the player can progress to the boss
# If any number is pressed, the boss battle loads
# If any other key is pressed, the program exits
def keyTyped():
    global secret
    if PAGE == 6:
        try:
            int(key)
        except:
            exit()
        else:
            secret = True


# Title screen
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

    if (mouseX > width/4-(rectx/2) and mouseX < width/4+(rectx/2) and
            mouseY > height-200 and mouseY < height-recty):
        fill(0, 128, 0)
        rect(width/4 - (rectx/2), height - 200, rectx, recty, 5)
        fill(255)
        textSize(16)
        text("Click here to Start", rectx+50, height-recty-40)

    # Code for Instructions button.  Changes color to a darker shade of red
    # if the mouse hovers over it
    fill(255, 0, 0)
    rect(width-2*rectx, height-200, rectx, recty, 5)
    textSize(14)
    fill(255)
    text("Click here for Instructions", width/2 + rectx + 55,
         height-recty - 40)
    if (mouseX > width-2*rectx and mouseX < width-rectx and
            mouseY > height - 200 and mouseY < height-recty):
        fill(153, 0, 0)
        rect(width-2*rectx, height - 200, rectx, recty, 5)
        fill(255)
        textSize(14)
        text("Click here for Instructions", width/2+rectx + 55,
             height - recty - 40)


# Instructions screen
def page2():
    # The instructions
    global rectx, recty
    background(instructions_background)
    textSize(16)
    fill(255, 0, 0)
    text("Help Megaman defeat Dr. Wily and save the world!", 250, 100)
    text("Press the left and right arrow keys to move and the" +
         " up key to jump.", 250, 175)
    text("Press the space bar to shoot enemies out of the way. Be" +
         " careful though, some enemies can't be killed.", 250, 250)
    text("Can you beat the game with zero deaths?", 250, 325)
    text("(UNKILLABLE)", 1075, 210)
    image(unkillable, 1100, 225)
    fill(0, 255, 0)
    rect(1100, 300, 50, 50)

    # Secret warp to the boss warp screen
    if mouseX > 1075 and mouseX < 1175 and mouseY > 200 and mouseY < 210:
        fill(0)
        text("(UNKILLABLE)", 1075, 210)


# Code for start button in the instructions menu
    fill(255, 255, 0)
    rect(width/2-rectx/2, height-125, rectx, recty, 5)
    fill(218, 112, 214)
    text("Click here to Start", width/2-rectx+130, height/2+recty+75)
    if (mouseX > width/2-rectx/2 and mouseX < width/2+rectx/2 and
            mouseY > height-125 and mouseY < height-125+recty):
        fill(255, 219, 88)
        rect(width/2-rectx/2, height-125, rectx, recty, 5)
        fill(218, 112, 214)
        text("Click here to Start", width/2-rectx+130, height/2+recty+75)


# Code used to draw stars in the background for asthetics
def draw_stars():
    import random
    fill(255)
    for star in range(len(stars)):
        ellipse(stars[star][0], stars[star][1], 5, 5)

    for star in range(len(stars)):
        stars[star][0] += 0.1

    # remove stars
    for star in range(len(stars)-1, 0, -1):
        if stars[star-1][0] >= width + 5:
            stars.pop(star-1)

    # add new star every second
    if frameCount % 60 == 0:
        stars.append([0, random.randint(1, height)])


# Spikes that appear in level 1
def level1_spikes(x, y, mid):
    global MEGAMAN_POSITION, DEATHS, unkillable_enemies, TIMER
    global bullet_timer, on_screen_bullet, draw_bullet
    noFill()
    rect(x, y-2*mid, 1.35*x, 2*mid)
    fill(211, 211, 211)
    # Draws a series of triangles to give the impression of spikes
    for spike in range(10):
        triangle(x, y, x+2*mid, y, x+mid, y-mid*2)
        x += 2*mid

    # Hitbox for spikes.  NOTE: Since the player is not able to clip through
    # the floor, the collision continues below the spikes
    # all the way to infinity
    if (MEGAMAN_POSITION[0] > x/3.5 and MEGAMAN_POSITION[0] < x and
            MEGAMAN_POSITION[1] > y/1.25):
        level1_reset()


# Sawblade that moves up and down on level 1
def level1_saw(x, y):
    global MEGAMAN_POSITION, DEATHS, TIMER, saw1_Y, saw1_up, bullet_time
    global on_screen_bullet, draw_bullet
    # draw saw
    fill(211, 211, 211)
    ellipse(x, y, saw_size, saw_size)
    # saw movement
    if saw1_up is False:
        saw1_Y += 1
        if saw1_Y >= 300:
            saw1_up = True
    if saw1_up is True:
        saw1_Y -= 1
        if saw1_Y < 50:
            saw1_up = False

    # saw hitbox
    if (MEGAMAN_POSITION[0]+megaman_size > saw1_X and
            MEGAMAN_POSITION[0] < saw1_X + saw_size and
            MEGAMAN_POSITION[1] < saw1_Y + saw_size/2 and
            MEGAMAN_POSITION[1] > saw1_Y - saw_size):
        level1_reset()


# An unkillable enemy that moves to the left on level 1
def unkillable_enemy1_hitbox():
    # If the player hits the enemy, they die, the level resets
    # and the death counter increments
    global MEGAMAN_POSITION, DEATHS, TIMER, unkillable_enemies, bullet_timer
    global on_screen_bullet, draw_bullet
    if (MEGAMAN_POSITION[0]+megaman_size/1.25 >= unkillable_enemies[0][0] and
            MEGAMAN_POSITION[0]/0.99 <=
            unkillable_enemies[0][0] + unkillable_enemies_size and
            MEGAMAN_POSITION[1] > unkillable_enemies[0][1] -
            unkillable_enemies_size and MEGAMAN_POSITION[1] <
            unkillable_enemies[0][1]+unkillable_enemies_size):
        level1_reset()

    # If the bullet hits this enemy, the bullet despawns and the
    # enemy is left untouched
    if (bulletX >= unkillable_enemies[0][0] and bulletX <=
            unkillable_enemies[0][0]+unkillable_enemies_size and
            bulletY <= unkillable_enemies[0][1] +
            unkillable_enemies_size and
            bulletY > unkillable_enemies[0][1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False


# An unkillable enemy that moves up and down (level 2)
def unkillable_enemy2_hitbox():
    global MEGAMAN_POSITION, DEATHS, TIMER, unkillable_enemies
    global bullet_timer, on_screen_bullet, draw_bullet

    # Hitbox
    if (MEGAMAN_POSITION[0]+megaman_size/1.25 >= unkillable_enemies[1][0] and
            MEGAMAN_POSITION[0]/0.99 <= unkillable_enemies[1][0] +
            unkillable_enemies_size and MEGAMAN_POSITION[1] >
            unkillable_enemies[1][1]-unkillable_enemies_size and
            MEGAMAN_POSITION[1] < unkillable_enemies[1][1] +
            unkillable_enemies_size):
        level2_reset()

# If the player shoots at the enemy, the bullet despawns and
# nothing happens
    if (bulletX >= unkillable_enemies[1][0] and bulletX <=
            unkillable_enemies[1][0]+unkillable_enemies_size and
            bulletY <= unkillable_enemies[1][1] +
            unkillable_enemies_size and
            bulletY > unkillable_enemies[1][1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False


# An unkillable enemy that moves up and down (level 2)
def unkillable_enemy3_hitbox():
    global MEGAMAN_POSITION, DEATHS, TIMER, unkillable_enemies
    global bullet_timer, on_screen_bullet, draw_bullet

    # Hitbox
    if (MEGAMAN_POSITION[0]+megaman_size/1.25 >= unkillable_enemies[2][0] and
            MEGAMAN_POSITION[0]/0.99 <= unkillable_enemies[2][0] +
            unkillable_enemies_size and MEGAMAN_POSITION[1] >
            unkillable_enemies[2][1]-unkillable_enemies_size and
            MEGAMAN_POSITION[1] < unkillable_enemies[2][1] +
            unkillable_enemies_size):
        level2_reset()

# If the player shoots at the enemy, the bullet despawns and
# nothing happens
    if (bulletX >= unkillable_enemies[2][0] and
            bulletX <= unkillable_enemies[2][0] + unkillable_enemies_size and
            bulletY <= unkillable_enemies[2][1] +
            unkillable_enemies_size and
            bulletY > unkillable_enemies[2][1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False


def enemy_hitbox():
    # If the player hits the enemy, they die, the level resets
    # and the death counter increments
    global MEGAMAN_POSITION, DEATHS, TIMER, enemy, enemy_dead, bullet_timer
    global on_screen_bullet, draw_bullet
    if (MEGAMAN_POSITION[0] + megaman_size/1.25 >= enemy[0] and
            MEGAMAN_POSITION[0]/0.99 <= enemy[0]+enemy_size and
            MEGAMAN_POSITION[1] > enemy[1]-enemy_size and
            MEGAMAN_POSITION[1] < enemy[1]+enemy_size):
        level2_reset()

    # If the bullet hits this enemy, the bullet despawns and
    # the enemy is left dead
    if (bulletX >= enemy[0] and bulletX <= enemy[0]+enemy_size and
            bulletY <= enemy[1]+enemy_size and
            bulletY > enemy[1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False
        enemy_dead = True


def shooter_enemy1():
    # If the player hits the enemy, they die, the level resets
    # and the death counter increments
    global MEGAMAN_POSITION, DEATHS, TIMER, shooter, shooter_bullet_timer
    global bullet_timer, on_screen_bullet, draw_bullet, shooter_bulletX
    if (MEGAMAN_POSITION[0]+megaman_size/1.25 >= shooter[0][0] and
            MEGAMAN_POSITION[0]/0.99 <= shooter[0][0]+shooter_size and
            MEGAMAN_POSITION[1] > shooter[0][1]-shooter_size and
            MEGAMAN_POSITION[1] < shooter[0][1]+shooter_size):
        level3_reset()

    # if the player shoots the enemy, nothing happens
    if (bulletX >= shooter[0][0] and bulletX <= shooter[0][0]+shooter_size and
            bulletY <= shooter[0][1]+shooter_size and
            bulletY > shooter[0][1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False

    # dictates if the bullet should shoot or not
    if shooter_bullet_timer[0] > 120:
        draw_shooter_bullet[0] = True
        shooter_bulletX[0] -= 6
    if shooter_bullet_timer[0] > 240:
        shooter_bullet_timer[0] = 0
        draw_shooter_bullet[0] = False
        shooter_bulletX[0] = shooter[0][0]

    shooter_bullet_timer[0] += 1

    # enemy bullet collision detection
    if (shooter_bulletX[0] >= MEGAMAN_POSITION[0] and
            shooter_bulletX[0] <= MEGAMAN_POSITION[0]+megaman_size and
            shooter_bulletY <= MEGAMAN_POSITION[1]+megaman_size and
            shooter_bulletY > MEGAMAN_POSITION[1]-bullet_size):
        level3_reset()


def shooter_enemy2():
    # If the player hits the enemy, they die, the level resets
    # and the death counter increments
    global MEGAMAN_POSITION, DEATHS, TIMER, shooter, shooter_bullet_timer
    global bullet_timer, on_screen_bullet, draw_bullet, shooter_bulletX
    if (MEGAMAN_POSITION[0]+megaman_size/1.25 >= shooter[1][0] and
            MEGAMAN_POSITION[0]/0.99 <= shooter[1][0]+shooter_size and
            MEGAMAN_POSITION[1] > shooter[1][1]-shooter_size and
            MEGAMAN_POSITION[1] < shooter[1][1]+shooter_size):
        level3_reset()

    # if the player shoots the enemy, nothing happens
    if (bulletX >= shooter[1][0] and bulletX <= shooter[1][0]+shooter_size and
            bulletY <= shooter[1][1]+shooter_size and
            bulletY > shooter[1][1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False

    # dictates if the bullet should shoot or not
    if shooter_bullet_timer[1] > 120:
        draw_shooter_bullet[1] = True
        shooter_bulletX[1] += 3
    if shooter_bullet_timer[1] > 360:
        shooter_bullet_timer[1] = 0
        draw_shooter_bullet[1] = False
        shooter_bulletX[1] = shooter[1][0]

    shooter_bullet_timer[1] += 1

    # enemy bullet collision detection
    if (shooter_bulletX[1] >= MEGAMAN_POSITION[0] and
            shooter_bulletX[1] <= MEGAMAN_POSITION[0]+megaman_size and
            shooter_bulletY <= MEGAMAN_POSITION[1]+megaman_size and
            shooter_bulletY > MEGAMAN_POSITION[1]-bullet_size):
        level4_reset()


def shooter_enemy3():
    # If the player hits the enemy, they die, the level resets
    # and the death counter increments
    global MEGAMAN_POSITION, DEATHS, TIMER, shooter, shooter_bullet_timer
    global bullet_timer, on_screen_bullet, draw_bullet, shooter_bulletX
    if (MEGAMAN_POSITION[0]+megaman_size/1.25 >= shooter[2][0] and
            MEGAMAN_POSITION[0]/0.99 <= shooter[2][0]+shooter_size and
            MEGAMAN_POSITION[1] > shooter[2][1]-shooter_size and
            MEGAMAN_POSITION[1] < shooter[2][1]+shooter_size):
        level3_reset()

    # if the player shoots the enemy, nothing happens
    if (bulletX >= shooter[2][0] and bulletX <= shooter[2][0]+shooter_size and
            bulletY <= shooter[2][1]+shooter_size and
            bulletY > shooter[2][1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False

    # dictates if the bullet should shoot or not
    if shooter_bullet_timer[2] > 120:
        draw_shooter_bullet[2] = True
        shooter_bulletX[2] -= 3
    if shooter_bullet_timer[2] > 360:
        shooter_bullet_timer[2] = 0
        draw_shooter_bullet[2] = False
        shooter_bulletX[2] = shooter[2][0]

    shooter_bullet_timer[2] += 1

    # enemy bullet collision detection
    if (shooter_bulletX[2] >= MEGAMAN_POSITION[0] and
            shooter_bulletX[2] <= MEGAMAN_POSITION[0]+megaman_size and
            shooter_bulletY <= MEGAMAN_POSITION[1]+megaman_size and
            shooter_bulletY > MEGAMAN_POSITION[1]-bullet_size):
        level4_reset()


# The first level of the game
def level1():
    global LEVEL, PAGE, TIMER, MEGAMAN_POSITION, unkillable_enemies
    global bullet_timer, on_screen_bullet, draw_bullet
    background(0)
    draw_stars()
    fill(255)
    text("DEATHS:" + str(DEATHS), 10, 15)
    text("TIMER:" + str(int(TIMER[0])), 100, 15)
    rect(0, 350, width, height)
    fill(255, 0, 0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], megaman_size, megaman_size)
    level1_spikes(150, 350, 10)
    level1_saw(saw1_X, saw1_Y)
    # Unkillable enemy and its hitbox
    image(unkillable, unkillable_enemies[0][0], unkillable_enemies[0][1])
    unkillable_enemies[0][0] -= 1
    unkillable_enemy1_hitbox()
    TIMER[0] -= 0.1

    # If the timer hits zero, the level resets. Same for all levels
    if TIMER[0] <= 0:
        level1_reset()

    # If the player hit space, a bullet will be drawn. All levels
    if draw_bullet is True:
        fill(255)
        rect(bulletX, bulletY, bullet_size, bullet_size)

    # Warps player to next level if they get to the end of the
    # screen. Same for all levels except boss battle
    if MEGAMAN_POSITION[0] > 1200:
        LEVEL = 2
        draw_bullet = False
        on_screen_bullet = False
        bullet_timer = 0
        MEGAMAN_POSITION = megaman_spawn_points[:]


# Second level
def level2():
    global LEVEL, PAGE, TIMER, MEGAMAN_POSITION, unkillable_enemies
    global unkillable_enemy1_up, unkillable_enemy2_up, bullet_timer
    global on_screen_bullet, draw_bullet
    background(0)
    draw_stars()
    fill(255)
    text("DEATHS:" + str(DEATHS), 10, 15)
    text("TIMER:" + str(int(TIMER[1])), 100, 15)
    rect(0, 350, width, height)
    fill(255, 0, 0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], megaman_size, megaman_size)
    image(unkillable, unkillable_enemies[1][0], unkillable_enemies[1][1])
    image(unkillable, unkillable_enemies[2][0], unkillable_enemies[2][1])

    # Moves the first unkillable enemy up and down
    if unkillable_enemy1_up is False:
        unkillable_enemies[1][1] += 4
        if unkillable_enemies[1][1] >= 300:
            unkillable_enemy1_up = True
    if unkillable_enemy1_up is True:
        unkillable_enemies[1][1] -= 4
        if unkillable_enemies[1][1] < 10:
            unkillable_enemy1_up = False

    # Moves the second unkillable enemy up and down
    if unkillable_enemy2_up is False:
        unkillable_enemies[2][1] += 4
        if unkillable_enemies[2][1] >= 300:
            unkillable_enemy2_up = True
    if unkillable_enemy2_up is True:
        unkillable_enemies[2][1] -= 4
        if unkillable_enemies[2][1] < 10:
            unkillable_enemy2_up = False

    unkillable_enemy2_hitbox()
    unkillable_enemy3_hitbox()

    # Code that checks if the killable enemy has been killed.
    # If he has, the program stops drawing it
    if enemy_dead is False:
        enemy_hitbox()
        fill(0, 0, 255)
        rect(enemy[0], enemy[1], enemy_size, enemy_size)
        enemy[0] -= 5

    TIMER[1] -= 0.1
    if TIMER[1] <= 0:
        level2_reset()

    if draw_bullet is True:
        fill(255)
        rect(bulletX, bulletY, bullet_size, bullet_size)

    if MEGAMAN_POSITION[0] > 1200:
        LEVEL = 3
        draw_bullet = False
        on_screen_bullet = False
        bullet_timer = 0
        MEGAMAN_POSITION = megaman_spawn_points[:]


# Third level in the game
def level3():
    global LEVEL, PAGE, TIMER, MEGAMAN_POSITION, unkillable_enemies
    global bullet_timer, on_screen_bullet, draw_bullet
    background(0)
    draw_stars()
    fill(255)
    text("DEATHS:" + str(DEATHS), 10, 15)
    text("TIMER:" + str(int(TIMER[2])), 100, 15)
    rect(0, 350, width, height)
    fill(255, 0, 0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], megaman_size, megaman_size)
    fill(0, 255, 0)
    rect(shooter[0][0], shooter[0][1], shooter_size, shooter_size)
    shooter_enemy1()
    TIMER[2] -= 0.1

    if TIMER[2] <= 0:
        level3_reset()

    if draw_bullet is True:
        fill(255)
        rect(bulletX, bulletY, bullet_size, bullet_size)

    if MEGAMAN_POSITION[0] > 1200:
        PAGE = 4
        draw_bullet = False
        on_screen_bullet = False
        bullet_timer = 0
        MEGAMAN_POSITION = megaman_spawn_point_boss[:]

    # Dictates if the program should draw the enemy's bullet.
    # Same for boss battle
    if draw_shooter_bullet[0] is True:
        fill(255)
        rect(shooter_bulletX[0], shooter_bulletY, bullet_size, bullet_size)


# Code for the final boss
# NOTE: Due to the difficulty of the final boss, the amount of
# damage delt to him is carried over if the player dies.
# Therefore, the boss only needs to be hit three times in total
# rather than in one attempt
def boss_battle():
    global boss, boss_left, drop_timer, boss_timer, boss_tracker
    global boss_hits, bullet_timer, on_screen_bullet, draw_bullet
    import random
    # Moves boss from left to right
    if boss_left is False:
        boss[0] += 4
    if boss[0] >= 1200:
        boss_left = True
    if boss_left is True:
        boss[0] -= 4
        if boss[0] < 300:
            boss_left = False

    # Program decides whether or not the boss should swoop down and
    # attack. This is decided every time the boss_timer variable is
    # equal to 50.
    if drop_timer == 0:
        boss_timer += 1
    if boss_timer == 50:
        boss_tracker = random.randint(0, 10)
        boss_timer = 0

    if boss_tracker == 1 or boss_tracker == 2:
        drop_timer += 1
    if drop_timer < 100 and drop_timer != 0:
        boss[1] += 2
    if drop_timer >= 100:
        if boss[1] >= 50:
            boss[1] -= 2
        if boss[1] <= 50:
            boss_tracker = 0
            drop_timer = 0

    # Boss' hitbox
    if (MEGAMAN_POSITION[0] + megaman_size/1.25 >= boss[0] and
            MEGAMAN_POSITION[0]/0.99 <= boss[0]+boss_size and
            MEGAMAN_POSITION[1] > boss[1]-boss_size and
            MEGAMAN_POSITION[1] < boss[1]+boss_size):
        level4_reset()
    if (bulletX >= boss[0] and bulletX <= boss[0]+boss_size and
            bulletY <= boss[1]+boss_size and
            bulletY > boss[1]-bullet_size):
        bullet_timer = 0
        on_screen_bullet = False
        draw_bullet = False
        boss_hits += 1


# Where the first three levels are drawn
def page3():
    physics()
    if LEVEL == 1:
        level1()
    if LEVEL == 2:
        level2()
    if LEVEL == 3:
        level3()


# Where the boss battle is initated
def page4():
    global LEVEL, PAGE, TIMER, MEGAMAN_POSITION, unkillable_enemies
    global bullet_timer, on_screen_bullet, draw_bullet
    physics()
    background(0)
    draw_stars()
    fill(255)
    text("DEATHS:" + str(DEATHS), 10, 15)
    text("TIMER:" + str(int(TIMER[3])), 100, 15)
    rect(0, 350, width, height)
    fill(255, 0, 0)
    rect(MEGAMAN_POSITION[0], MEGAMAN_POSITION[1], megaman_size, megaman_size)
    fill(0, 255, 0)
    rect(shooter[1][0], shooter[1][1], shooter_size, shooter_size)
    rect(shooter[2][0], shooter[2][1], shooter_size, shooter_size)
    fill(255, 0, 255)
    rect(boss[0], boss[1], boss_size, boss_size)

    shooter_enemy2()
    shooter_enemy3()
    boss_battle()

    TIMER[3] -= 0.1

    if TIMER[3] <= 0:
        level4_reset()

    if draw_bullet is True:
        fill(255)
        rect(bulletX, bulletY, bullet_size, bullet_size)

    if draw_shooter_bullet[1] is True:
        fill(255)
        rect(shooter_bulletX[1], shooter_bulletY, bullet_size, bullet_size)
    if draw_shooter_bullet[2] is True:
        fill(255)
        rect(shooter_bulletX[2], shooter_bulletY, bullet_size, bullet_size)

    # If the boss has been hit 3 times, the program decides whether or not
    # the player has earned the true ending based on the number of deaths
    if boss_hits == 3:
        if DEATHS > 0:
            PAGE = 5
        else:
            PAGE = 7
    print(boss_hits)


# Congratulations screen
def page5():
    background(0)
    # The congratulations message is a reference to Ghosts 'n
    # Goblins, arguably one of the worst games ever made on
    # the NES due to its horrendus controls and
    # extreme difficulty
    image(congratulations, width/2-150, height/2-100)


# If the player dies, this code is initated to reset the level
# Happens during level 1
def level1_reset():
    global DEATHS, TIMER, MEGAMAN_POSITION, unkillable_enemies
    global unkillable_enemies_spawn_points, megaman_spawn_points
    global bullet_timer, on_screen_bullet, draw_bullet
    DEATHS += 1
    TIMER[0] = RESET_TIMER[0]
    MEGAMAN_POSITION = megaman_spawn_points[:]
    unkillable_enemies[0][0] = unkillable_enemies_spawn_points[0][0]
    bullet_timer = 0
    on_screen_bullet = False
    draw_bullet = False


# If the player dies, this code is initated to reset the level
# Happens during level 2
def level2_reset():
    global DEATHS, TIMER, MEGAMAN_POSITION, unkillable_enemies
    global unkillable_enemies_spawn_points, megaman_spawn_points, enemy
    global enemy_spawn_point, bullet_timer, on_screen_bullet
    global draw_bullet, enemy_dead
    DEATHS += 1
    TIMER[1] = RESET_TIMER[1]
    MEGAMAN_POSITION = megaman_spawn_points[:]
    unkillable_enemies[1][1] = unkillable_enemies_spawn_points[1][1]
    unkillable_enemies[2][1] = unkillable_enemies_spawn_points[2][1]
    enemy[0] = enemy_spawn_point[0]
    bullet_timer = 0
    on_screen_bullet = False
    draw_bullet = False
    enemy_dead = False


# If the player dies, this code is initated to reset the level
# Happens during level 3
def level3_reset():
    global DEATHS, TIMER, MEGAMAN_POSITION, megaman_spawn_points, bullet_timer
    global on_screen_bullet, draw_bullet, shooter_bullet_timer
    global draw_shooter_bullet, shooter_bulletX
    DEATHS += 1
    TIMER[2] = RESET_TIMER[2]
    MEGAMAN_POSITION = megaman_spawn_points[:]
    bullet_timer = 0
    on_screen_bullet = False
    draw_bullet = False
    shooter_bullet_timer[0] = 0
    draw_shooter_bullet[0] = False
    shooter_bulletX[0] = shooter[0][0]


# If the player dies, this code is initated to reset the level
# Happens during the final boss fight
def level4_reset():
    global DEATHS, TIMER, MEGAMAN_POSITION, megaman_spawn_points, bullet_timer
    global on_screen_bullet, draw_bullet, shooter_bullet_timer
    global draw_shooter_bullet, shooter_bulletX, boss
    global drop_timer, boss_timer, boss_tracker
    DEATHS += 1
    TIMER[3] = RESET_TIMER[3]
    MEGAMAN_POSITION = megaman_spawn_point_boss[:]
    bullet_timer = 0
    on_screen_bullet = False
    draw_bullet = False
    shooter_bullet_timer[1] = 0
    draw_shooter_bullet[1] = False
    shooter_bulletX[1] = shooter[1][0]
    shooter_bullet_timer[2] = 0
    draw_shooter_bullet[2] = False
    shooter_bulletX[2] = shooter[2][0]
    boss = boss_spawn_point[:]
    drop_timer = 0
    boss_timer = 0
    boss_tracker = 0


# The gameplay physics
def physics():
    global LEVEL, PAGE, MEGAMAN_POSITION, bulletX, bulletY, on_screen_bullet
    global bullet_timer, draw_bullet
    global in_air, airtime
    # Determines if the player should move up or down
    if RIGHT_PRESSED is True:
        MEGAMAN_POSITION[0] += 3
    if LEFT_PRESSED is True and MEGAMAN_POSITION[0] > 0:
        MEGAMAN_POSITION[0] -= 3

    # Determines if the player is allowed to jump
    if in_air is True:
        airtime += 0.2
        if airtime > 10:
            MEGAMAN_POSITION[1] += 1
            if LEVEL == 1 and MEGAMAN_POSITION[1] > FLOOR:
                airtime = 0
                in_air = False
                MEGAMAN_POSITION[1] = FLOOR
            if LEVEL == 2 and MEGAMAN_POSITION[1] > FLOOR:
                airtime = 0
                in_air = False
                MEGAMAN_POSITION[1] = FLOOR
            if LEVEL == 3 and MEGAMAN_POSITION[1] > FLOOR:
                airtime = 0
                in_air = False
                MEGAMAN_POSITION[1] = FLOOR
        else:
            MEGAMAN_POSITION[1] -= 2

    # Determines if the player can shoot a bullet and if
    # a bullet is already on screen
    if on_screen_bullet is False:
        bulletX = MEGAMAN_POSITION[0]
        bulletY = MEGAMAN_POSITION[1]

    if on_screen_bullet is True:
        draw_bullet = True
        bulletX += 6
        bullet_timer += 1
        if bullet_timer > 100:
            bulletX = MEGAMAN_POSITION[0]
            bulletY = MEGAMAN_POSITION[1]
            draw_bullet = False
            on_screen_bullet = False
            bullet_timer = 0


# Secret warp to the final boss screen
def page6():
    global PAGE
    background(0)
    fill(255)
    text("Hey uh you're not supposed to be here so just reset" +
         " the program and go back ok?", width/2 - 400, height/2)
    if secret is True:
        PAGE = 4  # Warps to boss fight


# Nothing more than a small Easter egg if the player beats the
# game flawless
def page7():
    # A reference to PewDiePie. Go subscribe to him
    # so he can beat T Series
    background(255)
    image(zero_deaths, width/2-150, height/2-250)


def draw():
    global DEATHS
    if PAGE == 1:
        page1()
        DEATHS = 0
    elif PAGE == 2:
        page2()
    elif PAGE == 3:
        page3()
    elif PAGE == 4:
        page4()
    elif PAGE == 5:
        page5()
    elif PAGE == 6:
        page6()
    elif PAGE == 7:
        page7()
