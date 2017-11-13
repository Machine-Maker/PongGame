from title_scene import TitleScene
from scene_utils import SceneManager
from pygame import init, display, time, event, QUIT, quit
import constants as c

from tkinter import Tk, mainloop, StringVar, OptionMenu, Button

# --------- tkinter ---------
OPTIONS = [
    "1920x1080",
    "1366x768",
    "1280x1024",
    "1280x800",
    "1024x768"
]

try:
    highscore_file = open("highscore.txt", "r")
    c.highscore = highscore_file.readline()
    highscore_file.close()
except FileNotFoundError:
    highscore_file = open("highscore.txt", "w")
    highscore_file.write(str(0))
    print("Generating highscore file...")
    highscore_file.close()
    c.highscore = 0


master = Tk()
master.title("Resolution Settings")
c.monitor_dimensions = (master.winfo_screenwidth(), master.winfo_screenheight())
w_width = int(c.monitor_dimensions[0]/7)
w_height = int(c.monitor_dimensions[1]/4)
x = int(c.monitor_dimensions[0]/2 - w_width/2)
y = int(c.monitor_dimensions[1]/2 - w_height/2)
master.geometry("{}x{}+{}+{}".format(w_width, w_height, x, y))

var = StringVar(master)
var.set(OPTIONS[0])

option = OptionMenu(master, var, *OPTIONS)
option.pack()


def ok():
    c.screen_resolution = (int(var.get().split("x")[0]), int(var.get().split("x")[1]))
    master.destroy()
    master.quit()


button = Button(master, text="OK", command=ok)
button.pack()

mainloop()

# --------- pygame ---------
init()
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
            c.game_open = False
            break

        manager.scene.handle_events(event.get())
        manager.scene.update()
        manager.scene.render()
        display.flip()  # flip the screen FPS times a second

quit()
