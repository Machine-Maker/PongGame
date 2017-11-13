from scene_utils import Scene
from pygame import font, KEYDOWN, K_SPACE, mixer, display
from game_scene import GameScene
import constants as c


class TitleScene(Scene):
    def __init__(self):
        super().__init__()
        self.w_width = int(c.monitor_dimensions[0]/4)
        self.w_height = int(c.monitor_dimensions[1]/2)
        c.change_window_location(c.monitor_dimensions[0]/2-self.w_width/2, c.monitor_dimensions[1]/2 - self.w_height/2)
        display.set_caption("PongGame by: Jake Potrebic", "Pong")
        self.screen = display.set_mode((self.w_width, self.w_height))
        self.font = font.SysFont("Cambria Math", 40, bold=True)
        self.small_font = font.SysFont("Arial", 24)
        self.f = open("highscore.txt", "r+")
        self.highscore = self.f.readline()
        c.highscore = self.highscore
        self.f.close()

    def render(self):
        self.screen.fill((0, 200, 0))
        text1 = self.font.render("Pong!", True, (255, 255, 255))
        text2 = self.small_font.render("Made by Jake, Anna, and Rylie", True, (255, 255, 255))
        text3 = self.font.render("> press space to start <", True, (255, 255, 255))
        text4 = self.small_font.render("Current Highscore: {}".format(self.highscore), True, (255, 255, 255))
        self.screen.blit(text1, (self.screen.get_width()/2 - text1.get_width()/2, self.w_height/10))
        self.screen.blit(text2, (self.screen.get_width()/2 - text2.get_width()/2, self.w_height/5))
        self.screen.blit(text3, (self.screen.get_width()/2 - text3.get_width()/2, self.w_height/(5/2)))
        self.screen.blit(text4, (self.screen.get_width()/2 - text4.get_width()/2, self.w_height/2))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                mixer.music.stop()
                self.manager.go_to(GameScene())

