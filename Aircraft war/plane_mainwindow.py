"""
    1.游戏流程的搭建
    2.游戏类的创建
"""
import pygame
from plane import plane_class

class PlaneGame(object):
    def __init__(self):
        # pygame模块的初始化
        pygame.init()
        # 创建屏幕
        self.screen = pygame.display.set_mode(plane_class.SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()

        pygame.time.set_timer(plane_class.HERO_FIRE_EVENT,plane_class.HERO_FIRE_TIME)
        pygame.time.set_timer(plane_class.ENEMY_INIT_EVENT, plane_class.ENEMY_INIT_TIME)
        # 创建精灵和精灵组
        self.__create_sprites()

    def start_game(self):
        while True:
            self.clock.tick(plane_class.GAME_FRAME)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprite()
            pygame.display.update()

    # 创建精灵和精灵组的函数，为__init__服务，外部不使用
    def __create_sprites(self):
        # 缺失的音乐/开始游戏/分数/爆炸效果

        # 创建精灵
        bg1 = plane_class.BgSprite("../images/background.png")
        bg2 = plane_class.BgSprite("../images/background.png",True)

        self.hero = plane_class.Hero("../images/me1.png")
        # 背景🆚精灵组
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        # 我方飞机的精灵组
        self.hero_group = pygame.sprite.Group(self.hero)
        # 敌方飞机的精灵组
        self.emery_group = pygame.sprite.Group()


    # 事件检测
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if event.type == plane_class.HERO_FIRE_EVENT:
                self.hero.fire()
            if event.type == plane_class.ENEMY_INIT_EVENT:
                enemy1 = plane_class.Enemy("../images/enemy1.png")
                self.emery_group.add(enemy1)
                enemy2 = plane_class.Enemy("../images/enemy2.png")
                self.emery_group.add(enemy2)
                enemy3 = plane_class.Enemy("../images/enemy3_n1.png")
                self.emery_group.add(enemy3)
                # enemy3 = plane_class.Enemy("../images/enemy3_n2.png")
                # self.emery_group.add(enemy3)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.hero.speed_x = -2
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.hero.speed_x = 2
        else:
            self.hero.speed_x = self.hero.speed = 0



    #  碰撞检测
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.emery_group, True, True)
        emery = pygame.sprite.spritecollide(self.hero, self.emery_group, True)
        # res = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # if len(res) > 0:
        #     pass
        if len(emery) > 0:
            self.hero.kill()
            self.__game_over()

    # 精灵组位置更新
    def __update_sprite(self):
        for group in [self.bg_group, self.hero_group, self.emery_group,self.hero.bullet_group]:
                group.update()
                group.draw(self.screen)

    # 游戏结束
    def __game_over(self):
        print("正在退出游戏...")
        pygame.quit()
        exit()


game = PlaneGame()
game.start_game()
