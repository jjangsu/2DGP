from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7) #  (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
        self.move_y = random.randint(5, 10)

    def update(self):
        self.y -= self.move_y
        if self.y <= 65:
            self.y = 65

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
        self.move_y = random.randint(5, 10)

    def update(self):
        self.y -= self.move_y
        if self.y <= 65:
            self.y = 65

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

small_num = random.randint(5, 10)
big_num = 20 - small_num

team = [Boy() for i in range(11)]

small_balls = [Small_Ball() for i in range(small_num)]
big_balls = [Big_Ball() for i in range(big_num)]

# boy = Boy()
grass = Grass()

running = True;

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in small_balls:
        ball.update()
    for ball in big_balls:
         ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in small_balls:
        ball.draw()
    for ball in big_balls:
        ball.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()