from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)


time_per_action = 1.2
frames_per_action = 8
actions_per_time = 1.0 / time_per_action
FRAMES_PER_SEC = frames_per_action * actions_per_time

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, throwin_speed = 15, throwin_angle = 45): #velocity 15m/s
        if Bird.image == None:
            Bird.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = throwin_speed * math.cos(math.radians(throwin_angle))

        self.yv = abs(throwin_speed * math.sin(math.radians(throwin_angle)))
        self.frame = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.frame = (FRAMES_PER_SEC * game_framework.frame_time + self.frame) % 8
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        if self.y < 60:
            game_world.remove_object(self)

