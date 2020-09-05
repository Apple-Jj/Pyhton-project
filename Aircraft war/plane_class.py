"""
    该文件设计飞机大战中的所有游戏元素类定义的文件
"""
import pygame
import random

# 1.该类是一个游戏元素的基类（子弹，背景图，我方飞机，敌方飞机所有类都继承该类）该基类继承精灵类
#   将精灵添加到精灵组中，统一管理的
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
GAME_FRAME = 60
HERO_FIRE_EVENT = pygame.USEREVENT + 1
HERO_FIRE_TIME = 200
ENEMY_INIT_EVENT = pygame.USEREVENT + 2
ENEMY_INIT_TIME = 1000
ENEMY_SPEED_MIN = 1
ENEMY_SPEED_MAX = 5


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_dir, speed=1):
        super().__init__()  # 初始化父类的构造函数
        self.image = pygame.image.load(image_dir)  # image成员加载图片
        self.rect = self.image.get_rect()  # rect(x,y,width,height) get_rect()-->Rect(0,0,image_width,image_height)
        self.speed = speed  # 设置图片移动的初始化速度

    def update(self):
        self.rect.y += self.speed  # 默认移动的方向向下

class BgSprite(GameSprite):
    def __init__(self,image_dir,is_second=False):
        super().__init__(image_dir)
        if not is_second:
            self.rect.y = - self.rect.height

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height

            pass

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("../images/bullet2.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()

class Hero(GameSprite):
    def __init__(self,hero_dir):
        super().__init__(hero_dir,0)
        self.speed_x = 0
        self.rect.centerx = int(SCREEN_RECT.width/2)
        self.rect.centery = SCREEN_RECT.height - 120 - int(self.rect.height/2)
        self.bullet_group = pygame.sprite.Group()
        self.me_change = 0

    def update(self):
        self.me_change += 1
        if self.me_change % 10 == 0:
            if self.me_change % 4 == 0:
                self.image = pygame.image.load("../images/me2.png")
            else:
                self.image = pygame.image.load("../images/me1.png")
        self.rect.x += self.speed_x
        self.rect.y += self.speed
        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

        if self.rect.centerx <= 0:
            self.rect.centerx = 0

        if self.rect.centerx > SCREEN_RECT.width:
            self.rect.centerx = SCREEN_RECT.width


    def fire(self):
        bullet1 = Bullet()
        bullet1.rect.centerx = self.rect.centerx
        bullet1.rect.bottom = self.rect.top
        self.bullet_group.add(bullet1)



class Enemy(GameSprite):
    def __init__(self, enemy_dir):
        super().__init__(enemy_dir)
        self.speed = random.randint(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height


    # def __init__(self, enemy_dir):
    #
    #     super(Enemy, self).__init__(enemy_dir)
    #     self.direction = {"right": True, "left": False, "up": False, "down": False}  # 判断移动方向
    #     self.image = pygame.image.load("../images/enemy1.png")
    #     self.image_boom_list = []
    #     self.image_boom_list.append(pygame.image.load("../images/enemy1_down1.png"))
    #     self.image_boom_list.append(pygame.image.load("../images/enemy1_down2.png"))
    #     self.image_boom_list.append(pygame.image.load("../images/enemy1_down3.png"))
    #     self.image_boom_list.append(pygame.image.load("../images/enemy1_down4.png"))

    def update(self):
        super().update()
        if self.rect.top == SCREEN_RECT.height:
            self.kill()
