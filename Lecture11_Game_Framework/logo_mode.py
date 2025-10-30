from pico2d import *
import game_framework
import title_mode

image = None
logo_start_time = 0.0



def init():
    global image, logo_start_time
    logo_start_time = get_time()
    image = load_image('tuk_credit.png')
    pass

def finish():
    #메모리 해제
    global image
    del image

def update():
    if get_time() - logo_start_time > 2.0:
        game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    event_list = get_events() # 버퍼로부터 모든 입력을 갖고는 온다
    # 아무것도 안한다 - 그냥 버퍼만 flush하는것
    pass


def pause():
    pass

def resume():
    pass

