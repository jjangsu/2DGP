from pico2d import *

import game_framework

class Pause:
    def __init__(self):
        self.image = load_image('stop.png')
        self.time = 0

    def update(self):
        self.time = 1 - self.time
        delay(0.1)
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 90, 90, 400, 300)


def enter():
    global pause
    pause = Pause()


def exit():
    global pause
    del pause


def update():
    global pause
    pause.update()


def draw():
    global pause
    clear_canvas()
    pause.update()
    pause.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def pause():
    pass


def resume():
    pass