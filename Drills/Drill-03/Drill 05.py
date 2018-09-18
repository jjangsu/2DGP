from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def go_to_132_243():
    x, y = 203, 535
    frame = 0
    pitureY = 0
    move_ratio_x = (203 - 132) // 40
    move_ratio_y = (535 - 243) // 40

    while x >= 132 and y >= 243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, pitureY * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= move_ratio_x
        y -= move_ratio_y
        delay(0.02)


def go_to_535_470():
    x, y = 132, 243
    frame = 0
    pitureY = 1
    move_ratio_x = (535 - 132) // 40
    move_ratio_y = (470 - 243) // 40

    while (x <= 535 and y <= 470):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, pitureY * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 10
        x += move_ratio_x
        y += move_ratio_y
        delay(0.02)


def go_to_477_203():

    pass
def go_to_715_136():
    pass
def go_to_316_225():
    pass
def go_to_510_92():
    pass
def go_to_692_518():
    pass
def go_to_682_336():
    pass
def go_to_712_349():
    pass
def go_to_203_535():
    pass

def move_to_xy():
    # go_to_132_243()
    go_to_535_470()
    go_to_477_203()
    go_to_715_136()
    go_to_316_225()
    go_to_510_92()
    go_to_692_518()
    go_to_682_336()
    go_to_712_349()
    go_to_203_535()
    pass

while True:
    move_to_xy()

close_canvas()
