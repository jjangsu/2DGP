from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def go_to_132_243():
    pass
def go_to_535_470():
    pass
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
    go_to_132_243()
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
