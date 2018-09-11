from pico2d import *

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
while (x < 800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(0 + x, 90 + y)
    x = x + 2
    y = y + 1
    delay(0.01)

close_canvas()
