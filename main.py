holding = False
mainMenu = True
fps = 7.5
alive = True
groundBrightness = 10
blockBrightness = 150
playerBrightness = 255

#Start plot
basic.plot_leds("""
. . # . .
. # . # .
# # # # #
# . . . #
# . . . #
""")

input.on_button_event(Button.A, input.button_event_click(), a_controller)

def a_controller():
    global holding, mainMenu

    if mainMenu:
        start()
    elif holding:
        run()
    else:
        jump()

def run():
    global holding, mainMenu, fps, blockBrightness, playerBrightness
    blockPos = []
    holding = False
    blockOnScreen = False
    while alive:
        basic.pause(1000 / fps)
        if not blockOnScreen:
            if randint(0, 5) == 5:
                block = randint(1, 3)
                led.plot_brightness(4, block, blockBrightness)
                blockPos[0] = int(4)
                blockPos[1] = int(block)
                basic.pause(200)    
                blockOnScreen = True
        else:
            x = blockPos[0]
            y = blockPos[1]
            if (x != 1):
                led.unplot(x, y)
            else:
                if not(y >= 2 and y <=3):
                    led.unplot(x, y)
            x -= 1
            if x >= 0:
                blockPos[0] = int(x)
                if led.point_brightness(x, y) != playerBrightness:
                    led.plot_brightness(x, y, blockBrightness)
            else:
                blockOnScreen = False

def jump():
    pass

def start():
    global holding, mainMenu, groundBrightness, playerBrightness

    mainMenu = False
    basic.clear_screen()
    for i in range(5):
        led.plot_brightness(i, 4, groundBrightness)

    led.plot_brightness(1, 2, playerBrightness)
    led.plot_brightness(1, 3, playerBrightness)
    holding = True

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


input.on_button_event(Button.AB, input.button_event_click(), jingle)