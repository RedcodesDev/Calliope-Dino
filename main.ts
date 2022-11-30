let holding = false
let mainMenu = true
let fps = 7.5
let alive = false
let groundBrightness = 10
let blockBrightness = 150
let playerBrightness = 255
let jumpState = 0
let score = 0
// Start plot
basic.plotLeds(`
. . # . .
. # . # .
# # # # #
# . . . #
# . . . #
`)
function run() {
    let y: number;
    let block: number;
    let x: number;
    
    let blockPos = []
    holding = false
    let blockOnScreen = false
    alive = true
    while (alive) {
        basic.pause(1000 / fps)
        // Jump if needed
        if (jumpState >= 1) {
            for (y = 0; y < 5; y++) {
                led.unplot(1, y)
            }
            if (jumpState < 3) {
                led.plotBrightness(1, 2 - jumpState, 255)
                led.plotBrightness(1, 3 - jumpState, 255)
            } else if (jumpState >= 3) {
                led.plotBrightness(1, 0 + (jumpState - 3), 255)
                led.plotBrightness(1, 1 + (jumpState - 3), 255)
            }
            
            jumpState += 1
            if (jumpState == 6) {
                jumpState = 0
            }
            
        }
        
        // Move block
        if (!blockOnScreen) {
            if (randint(0, 5) == 5) {
                score += 1
                block = randint(1, 3)
                led.plotBrightness(4, block, blockBrightness)
                blockPos[0] = Math.trunc(4)
                blockPos[1] = Math.trunc(block)
                basic.pause(200)
                blockOnScreen = true
            }
            
        } else {
            x = blockPos[0]
            y = blockPos[1]
            if (led.pointBrightness(x, y) != playerBrightness) {
                led.unplot(x, y)
            }
            
            x -= 1
            if (x >= 0) {
                blockPos[0] = Math.trunc(x)
                if (led.pointBrightness(x, y) != playerBrightness) {
                    led.plotBrightness(x, y, blockBrightness)
                }
                
            } else {
                blockOnScreen = false
            }
            
            // Check if player collides with block
            if (led.pointBrightness(x, y) == playerBrightness) {
                alive = false
                dead()
            }
            
        }
        
    }
}

function dead() {
    
    basic.clearScreen()
    basic.showString("GAMEOVER")
    basic.showString("SCORE" + score)
    basic.clearScreen()
    basic.plotLeds(`
    . . # . .
    . # . # .
    # # # # #
    # . . . #
    # . . . #
    `)
    mainMenu = true
}

function jump() {
    
    jumpState = 1
}

function start() {
    
    mainMenu = false
    basic.clearScreen()
    for (let i = 0; i < 5; i++) {
        led.plotBrightness(i, 4, groundBrightness)
    }
    led.plotBrightness(1, 2, playerBrightness)
    led.plotBrightness(1, 3, playerBrightness)
    holding = true
}

input.onButtonEvent(Button.AB, input.buttonEventClick(), function jingle() {
    // Axel F jingle because why not
    music.playTone(Note.D, 200)
    basic.pause(200)
    music.playTone(Note.D, 200)
    basic.pause(200)
    music.playTone(Note.D, 200)
    basic.pause(200)
    music.playTone(Note.F, 200)
    basic.pause(100)
    music.playTone(Note.D, 200)
    basic.pause(100)
    music.playTone(Note.G, 200)
    basic.pause(50)
    music.playTone(Note.D, 200)
    basic.pause(50)
    music.playTone(Note.C, 200)
    basic.pause(100)
    music.playTone(Note.D, 200)
    basic.pause(150)
    music.playTone(Note.A, 200)
    basic.pause(150)
    music.playTone(Note.D, 200)
    basic.pause(100)
    music.playTone(Note.Bb, 200)
    basic.pause(100)
    music.playTone(Note.A, 200)
    basic.pause(100)
    music.playTone(Note.G, 200)
    basic.pause(100)
    music.playTone(Note.D, 200)
    basic.pause(100)
    music.playTone(Note.A, 200)
    basic.pause(100)
    music.playTone(Note.D5, 200)
    basic.pause(150)
    music.playTone(Note.D, 200)
    basic.pause(100)
    music.playTone(Note.C, 200)
    basic.pause(100)
    music.playTone(Note.C, 200)
    basic.pause(100)
    music.playTone(Note.E, 200)
    basic.pause(100)
    music.playTone(Note.D, 200)
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function a_controller() {
    
    if (mainMenu) {
        start()
    } else if (holding) {
        run()
    }
    
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function b_controller() {
    
    if (alive) {
        jump()
    }
    
})
