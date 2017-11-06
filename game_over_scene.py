from scene_utils import Scene
from pygame import font, KEYDOWN, K_ESCAPE, K_SPACE
import constants as c


class GameOverScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = font.SysFont("Cambria Math", 40, bold=True)

    def render(self, screen):
        screen.fill((0, 200, 0))
        text1 = self.font.render("Game Over!", True, (255, 255, 255))
        text2 = self.font.render("Your score: {}".format(c.final_score), True, (255, 255, 255))
        text3 = self.font.render("> press space to play again <", True, (255, 255, 255))
        text4 = self.font.render("> press esc to quit <", True, (255, 255, 255))
        screen.blit(text1, (screen.get_width()/2 - text1.get_width()/2, 100))
        screen.blit(text2, (screen.get_width()/2 - text2.get_width()/2, 150))
        screen.blit(text3, (screen.get_width()/2 - text3.get_width()/2, 250))
        screen.blit(text4, (screen.get_width()/2 - text4.get_width()/2, 300))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    c.game_over = True
                    c.game_open = False
                elif e.key == K_SPACE:
                    c.game_over = True
