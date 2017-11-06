from title_scene import TitleScene
from scene_utils import SceneManager
from pygame import init, display, time, event, QUIT, quit
import constants as c


init()
c.screen_surface = display.set_mode((640, 480))
c.screen_rect = c.screen_surface.get_rect()
# ------ constants ------------
clock = time.Clock()
FPS = 60  # desired frame rate in frames per second.
playtime = 0


while c.game_open:
    manager = SceneManager(TitleScene())
    c.game_over = False
    while not c.game_over:
        # do all this each frame
        milliseconds = clock.tick(FPS)  # do not go faster than this frame rate
        playtime += milliseconds / 1000.0
        if event.get(QUIT):
            mainloop = False
            break

        manager.scene.handle_events(event.get())
        manager.scene.update()
        manager.scene.render(c.screen_surface)
        display.flip()  # flip the screen FPS times a second

quit()
