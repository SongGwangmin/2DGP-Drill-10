from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0            # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

centimeter = 100
meter = centimeter / 100

time_per_action = 1
frames_per_action = 14
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
    (553, 735, 338, 506)
]


class Bird:
    image = None

    def __init__(self, x = 400, y = 300): #velocity 15m/s
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y

        self.frame = random.randint(0, 13)
        self.dir = 1

    def draw(self):
        action = frame_border[int(self.frame)]

        if self.dir == 1:
            self.image.clip_composite_draw(action[0] - 4, 506 - action[3], 181, 167, 0, '', self.x, self.y, meter * PIXEL_PER_METER, meter * PIXEL_PER_METER)
        else:
            self.image.clip_composite_draw(action[0] - 4, 506 - action[3], 181, 167, 0, 'h', self.x, self.y, meter * PIXEL_PER_METER, meter * PIXEL_PER_METER)

    def update(self):
        self.frame = (FRAMES_PER_SEC * game_framework.frame_time + self.frame) % 14
        self.x += game_framework.frame_time * RUN_SPEED_PPS * self.dir
        if self.x < 30:
            self.dir = 1
            print(self.dir)
        elif self.x > 1600 - 30:
            self.dir = -1
            print(self.dir)

