from scene_utils import Scene
from pygame import font, KEYDOWN, K_SPACE, mixer
from game_scene import GameScene


class TitleScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = font.SysFont("Cambria Math", 40, bold=True)
        self.small_font = font.SysFont("Arial", 24)

    def render(self, screen):
        screen.fill((0, 200, 0))
        text1 = self.font.render("Pong!", True, (255, 255, 255))
        text2 = self.small_font.render("Made by Jake Potrebic", True, (255, 255, 255))
        text3 = self.font.render("> press space to start <", True, (255, 255, 255))
        screen.blit(text1, (screen.get_width()/2 - text1.get_width()/2, 50))
        screen.blit(text2, (screen.get_width()/2 - text2.get_width()/2, 150))
        screen.blit(text3, (screen.get_width()/2 - text3.get_width()/2, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                mixer.music.stop()
                self.manager.go_to(GameScene())

