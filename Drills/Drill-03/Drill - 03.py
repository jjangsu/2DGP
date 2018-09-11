from pico2d import *
import math
                
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
shape = 0
direct =0
pi = 3.14
angle = 0

while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)
    
    
    if(x > 390):
        if(x < 400 ):
            if(y > 85):
                if(y < 90):
                    direct = 4

    if(direct == 0):
        x = x + 2
        if(x > 780):
            direct = 1
    elif(direct == 1):
        y = y + 2
        if(y > 580):
            direct = 2
    elif(direct == 2):
        x = x - 2
        if(x < 20):
            direct = 3
    elif(direct == 3):
        y = y - 2
        if(y < 90):
            direct = 0
    elif(direct == 4):
        angle = angle + 0.1
        radian = angle * pi
        x = (400) + (200 * math.cos(radian))
        y = (300) + (200 * math.sin(radian))
        if(radian >= 2*pi):
            direct = 0
            x = 400
            y = 90
            angle =0
            
    
