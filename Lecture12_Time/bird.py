from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)


time_per_action = 1.2
frames_per_action = 8
actions_per_time = 1.0 / time_per_action
FRAMES_PER_SEC = frames_per_action * actions_per_time

frame_border = [
    (4,   186, 0,   168),   # 1행 1열
    (187, 369, 0,   168),
    (370, 552, 0,   168),
    (553, 735, 0,   168),
    (736, 918, 0,   168),

    (4,   186, 169, 337),   # 2행 1열
    (187, 369, 169, 337),
    (370, 552, 169, 337),
    (553, 735, 169, 337),
    (736, 918, 169, 337),

    (4,   186, 338, 506),   # 3행 1열
    (187, 369, 338, 506),
    (370, 552, 338, 506),
    (553, 735, 338, 506),
    (736, 918, 338, 506),
]

max_frame = len(frame_border)

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, throwin_speed = 15, throwin_angle = 45): #velocity 15m/s
        if Bird.image == None:
            Bird.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = throwin_speed * math.cos(math.radians(throwin_angle))
        self.yv = abs(throwin_speed * math.sin(math.radians(throwin_angle)))
        self.frame = 0
        self.dir = 1

    def draw(self):
        action = frame_border[int(self.frame)]

        if dir == 1:
            self.image.clip_composite_draw(action[0], action[1], action[3], action[4], 0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(action[0], action[1], action[3], action[4], 0, 'v', self.x, self.y, 100, 100)

    def update(self):
        self.frame = (FRAMES_PER_SEC * game_framework.frame_time + self.frame) % 15
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        if self.y < 60:
            game_world.remove_object(self)

