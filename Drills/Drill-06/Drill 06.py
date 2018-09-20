from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
   global running
   global x, y
   global character_dir
   global final_x, final_y
   global charcter_x, character_y

   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_MOUSEMOTION:
           x, y = event.x, KPU_HEIGHT - 1 - event.y
           character_dir = 1
       elif event.type == SDL_MOUSEBUTTONDOWN:
           final_x, final_y = event.x, KPU_HEIGHT - 1 - event.y
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
character_dir = 3

final_x = character_x
final_y = character_y


while running:
    move_x = (final_x - character_x) / 20
    move_y = (final_y - character_y) / 20

    character_x += move_x
    character_y += move_y

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0, 0, 50, 50, x, y)
    character.clip_draw(frame * 100, 100 * character_dir, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()




