from pico2d import *

import game_framework

class Pause:
    def __init__(self):
        self.image = load_image('stop.png')
        self.time = 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 90, 90, 400, 300)


def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    pass


def handle_events():
    pass


def pause():
    pass


def resume():
    pass