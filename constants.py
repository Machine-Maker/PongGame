from os import environ


radius1 = 40
blue = (0, 0, 255)
screen_surface = None
screen_rect = None
game_over = False
game_open = True
final_score = 0
played_music = False
screen_resolution = None
monitor_dimensions = None
highscore = None


def change_window_location(x, y):
    environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(int(x), int(y))
