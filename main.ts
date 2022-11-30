let holding = false
let mainMenu = true
let fps = 7.5
let alive = true
let groundBrightness = 10
let blockBrightness = 150
let playerBrightness = 255
// Start plot
basic.plotLeds(`
. . # . .
. # . # .
# # # # #
# . . . #
# . . . #
`)
input.onButtonEvent(Button.A, input.buttonEventClick(), function a_controller() {
    
    if (mainMenu) {
        start()
    }
    
    if (holding) {
        run()
    }
    
})
function run() {
    let block: number;
    let x: number;
    let y: number;
    
    let blockPos = []
    holding = false
    let blockOnScreen = false
    while (alive) {
        basic.pause(1000 / fps)
        if (!blockOnScreen) {
            if (randint(0, 5) == 5) {
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
            if (x != 1) {
                led.unplot(x, y)
            } else if (!(y >= 2 && y <= 3)) {
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
            
        }
        
    }
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
    music.playTone(Note.C, music.beat())
})
