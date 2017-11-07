from scene_utils import Scene
from pygame import Surface, mouse, font, draw, mixer, display
from pygame.sprite import Sprite, Group, collide_rect
from game_over_scene import GameOverScene
import constants as c


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        w_width = int(c.screen_resolution[0])
        w_height = int(c.screen_resolution[1])
        c.change_window_location(c.monitor_dimensions[0]/2 - w_width/2, c.monitor_dimensions[1]/2 - w_height/2)
        self.screen = display.set_mode((w_width, w_height))
        self.screen_rect = self.screen.get_rect()
        self.bg = Surface(self.screen.get_size())
        self.bg.convert()
        self.bg.fill((100, 155, 200))
        self.ball = Ball((0, 0, 0), c.radius1)
        self.block = Block(c.blue, 200, 25)
        self.sprites_list = Group(self.ball, self.block)
        self.score_label = ScoreLabel()
        self.game_over = False

    def render(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.score_label.image, (0, 0))
        self.sprites_list.draw(self.screen)

    def update(self):
        self.sprites_list.update(self)
        self.score_label.update()

    def handle_events(self, events):
        pass


class ScoreLabel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.font = font.SysFont("monospace", 15)
        self.score = 0
        self.text = "Score: {}".format(self.score)
        self.color = (0, 0, 0)
        self.image = None

    def update(self):
        self.text = "Score: {}".format(self.score)
        self.image = self.font.render(self.text, 1, self.color)

    def add_one(self):
        self.score += 1


class Ball(Sprite):
    def __init__(self, a_color, radius):
        super().__init__()
        self.image = Surface([radius*2, radius*2])
        self.image.fill((110, 155, 200))
        draw.circle(self.image, a_color, (radius, radius), 40)
        self.rect = self.image.get_rect()
        self.dx1 = 10
        self.dy1 = 10
        mixer.music.load('computer_boop.wav')

    def update(self, game_scene):
        self.rect.x += self.dx1
        self.rect.y += self.dy1
        if self.rect.x + 2*c.radius1 >= c.screen_resolution[0] + 10:
            self.rect.x = c.screen_resolution[0] - 2*c.radius1
            self.dx1 *= -1
        elif self.rect.x <= -10:
            self.rect.x = c.radius1
            self.dx1 *= -1

        if collide_rect(self, game_scene.block):
            if self.dy1 > 0 and self.rect.y + self.rect.height <= c.screen_resolution[1] - c.screen_resolution[1]/10+10:
                self.dy1 *= -1
                mixer.music.play(0)
                game_scene.score_label.add_one()
        elif self.rect.y >= c.screen_resolution[1]:
            c.final_score = game_scene.score_label.score
            game_scene.manager.go_to(GameOverScene())
        elif self.rect.y <= 0:
            self.rect.y = c.radius1
            self.dy1 *= -1


class Block(Sprite):
    def __init__(self, a_color, width, height):
        super().__init__()
        self.image = Surface([width, height])
        self.image.fill(a_color)
        self.rect = self.image.get_rect()
        self.rect.y = c.screen_resolution[1] - c.screen_resolution[1]/10
        self.rect.x = 0

    def update(self, g_scene):
        pos = mouse.get_pos()
        self.rect.x = pos[0]-100
