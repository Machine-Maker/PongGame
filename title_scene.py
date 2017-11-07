from scene_utils import Scene
from pygame import font, KEYDOWN, K_SPACE, mixer, display
from game_scene import GameScene
import constants as c


class TitleScene(Scene):
    def __init__(self):
        super().__init__()
        w_width = int(c.monitor_dimensions[0]/4)
        w_height = int(c.monitor_dimensions[1]/2)
        c.change_window_location(c.monitor_dimensions[0]/2 - w_width/2, c.monitor_dimensions[1]/2 - w_height/2)
        display.set_caption("PongGame by: Jake Potrebic", "Pong")
        self.screen = display.set_mode((w_width, w_height))
        self.font = font.SysFont("Cambria Math", 40, bold=True)
        self.small_font = font.SysFont("Arial", 24)

    def render(self):
        self.screen.fill((0, 200, 0))
        text1 = self.font.render("Pong!", True, (255, 255, 255))
        text2 = self.small_font.render("Made by Jake Potrebic", True, (255, 255, 255))
        text3 = self.font.render("> press space to start <", True, (255, 255, 255))
        self.screen.blit(text1, (self.screen.get_width()/2 - text1.get_width()/2, 50))
        self.screen.blit(text2, (self.screen.get_width()/2 - text2.get_width()/2, 150))
        self.screen.blit(text3, (self.screen.get_width()/2 - text3.get_width()/2, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                mixer.music.stop()
                self.manager.go_to(GameScene())

