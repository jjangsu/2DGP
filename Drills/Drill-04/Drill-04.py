from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
y = 1

# 여기를 채우세요.
frame = 0
while( True ):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, y * 100, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    if(y == 1):
        x += 7
    elif(y == 0):
        x -= 7
    if(x > 800):
        y = 0
        frame = 0
    elif(x < 0):
        y = 1
        frame = 0
    delay(0.05)
    get_events()

close_canvas()