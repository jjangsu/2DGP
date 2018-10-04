import turtle
import random
from pico2d import*


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2-y1) /(x2-x1)
    b = y1 - x1 * a

    for x in range(x1, x2 + 1, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)


def draw_line(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    for i in range(0, 100 + 1, 10):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        draw_point((x,y))
    draw_point(p2)


def draw_character(p1, p2):
    global character
    #draw_big_point(p1)
    #draw_big_point(p2)

    frame = 0
    character_dir = 1

    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        clear_canvas()
        KPU.draw(1280/2, 1024/2)
        character.clip_draw(frame * 100, character_dir * 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.02)

open_canvas(1280, 1024)

character = load_image('animation_sheet.png')
KPU = load_image('KPU_GROUND.png')

size = 20
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]

n = 1

while True:
    draw_character(points[n-1], points[n])
    n = (n + 1) % size