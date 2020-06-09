# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():

    #pygame.display.set_caption("TEST GAME")              # タイトルバーに表示する文字
    (w,h) = (600,500)
    (x,y) = (200,250)
    pygame.init()
    pygame.display.set_mode((w, h),0,32)    # 大きさ400*300の画面を生成
    screen = pygame.display.get_surface()
    #pygame.draw.ellipse(screen,(0,100,0),(x,y,10,200),0)

    ##font = pygame.font.Font(None,55);
    while (1):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            if x > 0:
                x -= 10
        if pressed_key[K_RIGHT]:
            if x < w - 200:
                x += 10
        if pressed_key[K_UP]:
            if y > 0:
                y -= 10
        if pressed_key[K_DOWN]:
            if y < h - 25:
                y += 10

        pygame.display.update()     # 画面を更新
        pygame.time.wait(30)
        screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
        
        pygame.draw.ellipse(screen,(0,100,0),Rect(x,y,200,25),0)
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
