import pygame
import time
pygame.init()
screen = pygame.display.set_mode((480, 700))
hero_photo = pygame.image.load("../images/me1.png")
bg_photo = pygame.image.load("../images/background.png")
clock = pygame.time.Clock()
# y = 500
# x = 200
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit(0)
        # elif event.type == pygame.KEYUP:




    screen.blit(bg_photo,(0,0))
    screen.blit(hero_photo,(200,500))
    # x += 1
    # y -= 5
    # if y + 126 < 0:
    #     y = 700
    # time.sleep(0.01)
    pygame.display.update()
    pass

# pygame.quit()