holding = False
mainMenu = True
fps = 7.5
alive = False
groundBrightness = 10
blockBrightness = 150
playerBrightness = 255
jumpState = 0
score = 0

#Main Menu
basic.plot_leds("""
. . # . .
. # . # .
# # # # #
# . . . #
# . . . #
""")

# A Button Handler
def a_controller():
    global holding, mainMenu
    if mainMenu:
        start()
    elif holding:
        run()

# B Button Handler
def b_controller():
    global alive
    if alive:
        jump()

# Method is executed at start of running the game
def run():
    global holding, mainMenu, fps, blockBrightness, playerBrightness, jumpState, alive, score
    blockPos = []
    holding = False
    blockOnScreen = False
    alive = True
    while alive:
        basic.pause(1000 / fps)
        #Jump if needed
        if jumpState >= 1:
            for y in range(4):
                led.unplot(1, y)
            if jumpState < 3:
                led.plot_brightness(1, 2 - jumpState, 255)
                led.plot_brightness(1, 3 - jumpState, 255)
            elif jumpState >= 3:
                led.plot_brightness(1, 0 + (jumpState - 3), 255)
                led.plot_brightness(1, 1 + (jumpState - 3), 255)
            jumpState += 1
            if jumpState == 6:
               jumpState = 0
        #Move block
        if not blockOnScreen:
            if randint(0, 5) == 5:
                #Spawn block
                score += 1
                block = randint(1, 3)
                led.plot_brightness(4, block, blockBrightness)
                blockPos[0] = int(4)
                blockPos[1] = int(block)
                basic.pause(200)    
                blockOnScreen = True
        else:
            #Move block
            x = blockPos[0]
            y = blockPos[1]
            if led.point_brightness(x, y) != playerBrightness:
                led.unplot(x, y)
            x -= 1
            if x >= 0:
                blockPos[0] = int(x)
                if led.point_brightness(x, y) != playerBrightness:
                    led.plot_brightness(x, y, blockBrightness)
            else:
                blockOnScreen = False
            #Check if player collides with block
            if led.point_brightness(x, y) == playerBrightness:
                alive = False
                dead()

#Method for handling if a player dies
def dead():
    global score, mainMenu
    basic.clear_screen()
    basic.show_string("GAMEOVER")
    basic.show_string("SCORE")
    basic.show_number(score)
    basic.clear_screen()
    basic.plot_leds("""
    . . # . .
    . # . # .
    # # # # #
    # . . . #
    # . . . #
    """)
    mainMenu = True

#Method to start jumping
def jump():
    global jumpState
    jumpState = 1

#Method for Main Menu
def start():
    global holding, mainMenu, groundBrightness, playerBrightness
    mainMenu = False
    basic.clear_screen()
    for i in range(5):
        led.plot_brightness(i, 4, groundBrightness)
    led.plot_brightness(1, 2, playerBrightness)
    led.plot_brightness(1, 3, playerBrightness)
    holding = True

# Easter-Egg Jingle Method
def jingle():
    #Axel F jingle because why not
    music.play_tone(Note.D, 200)
    basic.pause(200)
    music.play_tone(Note.D, 200)
    basic.pause(200)
    music.play_tone(Note.D, 200)
    basic.pause(200)
    music.play_tone(Note.F, 200)
    basic.pause(100)
    music.play_tone(Note.D, 200)
    basic.pause(100)
    music.play_tone(Note.G, 200)
    basic.pause(50)
    music.play_tone(Note.D, 200)
    basic.pause(50)
    music.play_tone(Note.C, 200)
    basic.pause(100)
    music.play_tone(Note.D, 200)
    basic.pause(150)
    music.play_tone(Note.A, 200)
    basic.pause(150)
    music.play_tone(Note.D, 200)
    basic.pause(100)
    music.play_tone(Note.BB, 200)
    basic.pause(100)
    music.play_tone(Note.A, 200)
    basic.pause(100)
    music.play_tone(Note.G, 200)
    basic.pause(100)
    music.play_tone(Note.D, 200)
    basic.pause(100)
    music.play_tone(Note.A, 200)
    basic.pause(100)
    music.play_tone(Note.D5, 200)
    basic.pause(150)
    music.play_tone(Note.D, 200)
    basic.pause(100)
    music.play_tone(Note.C, 200)
    basic.pause(100)
    music.play_tone(Note.C, 200)
    basic.pause(100)
    music.play_tone(Note.E, 200)
    basic.pause(100)
    music.play_tone(Note.D, 200)

# Button Events
input.on_button_event(Button.AB, input.button_event_click(), jingle)
input.on_button_event(Button.A, input.button_event_click(), a_controller)
input.on_button_event(Button.B, input.button_event_click(), b_controller)