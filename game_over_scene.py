from scene_utils import Scene
from pygame import font, KEYDOWN, K_ESCAPE, K_SPACE, mixer, display
import constants as c


class GameOverScene(Scene):
    def __init__(self):
        super().__init__()
        self.w_width = int(c.monitor_dimensions[0]/4)
        self.w_height = int(c.monitor_dimensions[1]/2)
        c.change_window_location(c.monitor_dimensions[0]/2-self.w_width/2, c.monitor_dimensions[1]/2 - self.w_height/2)
        self.screen = display.set_mode((self.w_width, self.w_height))
        self.font = font.SysFont("Cambria Math", 40, bold=True)
        if not c.played_music:
            mixer.music.load("trombone_fail.mp3")
            mixer.music.play(0)
            c.played_music = True

    def render(self):
        self.screen.fill((0, 200, 0))
        text1 = self.font.render("Game Over!", True, (255, 255, 255))
        text2 = self.font.render("Your score: {}".format(c.final_score), True, (255, 255, 255))
        text3 = self.font.render("> press space to play again <", True, (255, 255, 255))
        text4 = self.font.render("> press esc to quit <", True, (255, 255, 255))
        self.screen.blit(text1, (self.screen.get_width()/2 - text1.get_width()/2, self.w_height/5))
        self.screen.blit(text2, (self.screen.get_width()/2 - text2.get_width()/2, self.w_height*(3/10)))
        self.screen.blit(text3, (self.screen.get_width()/2 - text3.get_width()/2, self.w_height/2))
        self.screen.blit(text4, (self.screen.get_width()/2 - text4.get_width()/2, self.w_height*(3/5)))

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
                    c.played_music = False
