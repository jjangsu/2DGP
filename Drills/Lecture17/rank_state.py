import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import main_state
import world_build_state

name = "LankingState"

ranking_list = None
font = None
image = None

def enter():
    global ranking_list, game_rank, font, image
    image = load_image('menu.png')
    font = load_font('ENCR10B.TTF', 20)

    with open('rank.json', 'rb') as f:
        ranking_list = json.load(f)

    game_rank = None

    for data in ranking_list:
        if data['score'] < main_state.game_record:
            game_rank = data['rank']
            i = 9
            while i >= game_rank:
                ranking_list[game_rank]['score'] = ranking_list[game_rank - 1]['score']
                i -= 1
            data['score'] = main_state.game_record
            break
    rank_list = json.dumps(ranking_list)
    f = open("rank.json", 'w')
    f.write(rank_list)
    f.close()

    show_lattice()

def update():
    pass

def draw():
    global ranking_list
    global font, image
    clear_canvas()

    image.clip_draw(0, 0, 10, 10, 650, 430, 500, 400)

    font.draw(550, 600, '[Total Ranking]', (0, 0, 0))
    i = 550
    for data in ranking_list:
        font.draw(500, i, '#%d.' % data['rank'], (0, 0, 0))
        font.draw(600, i, 'score: %3f' % data['score'], (0, 0, 0))
        i -= 30

    update_canvas()

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)