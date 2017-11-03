import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480),)
screenrect = screen.get_rect()
# ------ constants ------------
clock = pygame.time.Clock()
mainloop = True
FPS = 60  # desired frame rate in frames per second.
playtime = 0
blue = (0, 0, 255)
score = 0

# ------- background ---------
background = pygame.Surface(screen.get_size())
background.fill((100, 155, 200))   # fill the background white (red,green,blue)
background = background.convert()
screen.blit(background, (0, 0))   # draw background on screen (overwriting all)

# ------------ player class --------
all_sprites_list = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, radius):
        super().__init__()
        self.image = pygame.Surface([radius*2, radius*2+20])
        self.image.fill((110, 155, 200))
        pygame.draw.circle(self.image, color, (radius, radius), 40)
        self.rect = self.image.get_rect()


# ----------- bouncing ball (drawing) ------
x1 = 50
y1 = 50
dx1 = 10
dy1 = 10
radius1 = 40
ball = Ball((0, 0, 0), radius1)
all_sprites_list.add(ball)


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


player = Block(blue, 200, 25)
all_sprites_list.add(player)

collision = False

# --------- mainloop ----------
while mainloop:
    # do all this each frame
    milliseconds = clock.tick(FPS)  # do not go faster than this framerate
    playtime += milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        # ----- clean screen ----------
    screen.blit(background, (0, 0))  # draw background on screen (overwriting all)

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]-100
    player.rect.y = 450
    # ------- bouncing ball ---------
    x1 += dx1
    y1 += dy1
    if x1 + 2*radius1 >= screenrect.width + 10:
        x1 = screenrect.width - 2*radius1
        dx1 *= -1
    elif x1 <= -10:
        x1 = radius1
        dx1 *= -1

    if y1 + radius1 < 330:
        collision = False

    if pygame.sprite.collide_rect(ball, player):
        if not collision:
            print("collide")
            dy1 *= -1
            collision = True
    elif y1 + radius1 >= screenrect.height:  # change this later
        print("game over")
        break
    elif y1 - radius1 <= 0:
        y1 = radius1
        dy1 *= -1
    ball.rect.x = x1
    ball.rect.y = y1
    # ----------player-----------------

    all_sprites_list.draw(screen)
    # --------- flip screen ------------------
    pygame.display.flip()  # flip the screen FPS times a second
pygame.quit()
print("This 'game' was played for {:.2f} seconds.".format(playtime))
print("score:", score)
