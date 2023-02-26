import pygame
import random
import math

pygame.init()

window = pygame.display.set_mode((1024, 600))

pygame.display.set_caption("W E L C O M E")

icon = pygame.image.load('images/bg.png')
pygame.display.set_icon(icon)

BG = pygame.image.load('images/pic1.png')

HM = pygame.image.load('images/hm.png')
HMX = 500
HMY = 275
HMX_change = 0
HMY_change = 0

LB = pygame.image.load('images/lb.png')
LBX = random.randint(100, 900)
LBY = random.randint(25, 100)
LBX_change = -15
LBY_change = 15

CN = pygame.image.load('images/cn.png')
CNX = random.randint(100, 900)
CNY = random.randint(25, 100)
CNX_change = 15
CNY_change = -15

game_over_state = True

game_over_font = pygame.font.Font('freesansbold.ttf', 32)


def draw(x1, y1, x2, y2, x3, y3):
    window.blit(LB, (x1, y1))
    window.blit(CN, (x2, y2))
    window.blit(HM, (x3, y3))


def game_over():
    game_over_text = game_over_font.render('GAME OVER', True, (0, 0, 0))
    window.blit(game_over_text, (400, 300))


def collision(x1, y1, x2, y2, x3, y3):
    distance_LB_HM = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
    distance_CN_HM = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))

    if distance_LB_HM < 32 or distance_CN_HM < 32:
        return True
    else:
        return False


run = True

while run:
    window.fill((80, 160, 240))

    window.blit(BG, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                HMX_change += 10

            if event.key == pygame.K_LEFT:
                HMX_change -= 10

            if event.key == pygame.K_UP:
                HMY_change -= 10

            if event.key == pygame.K_DOWN:
                HMY_change += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                HMX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                HMY_change = 0

    if LBX <= 10 or LBX >= 950:
        LBX_change = -LBX_change

    if LBY <= 10 or LBY >= 525:
        LBY_change = -LBY_change

    if CNX <= 10 or CNX >= 950:
        CNX_change = -CNX_change

    if CNY <= 10 or CNY >= 525:
        CNY_change = -CNY_change

    if HMX <= 10:
        HMX = 10
    if HMX >= 950:
        HMX = 950
    if HMY <= 10:
        HMY = 10
    if HMY >= 525:
        HMY = 525

    if game_over_state:
        HMX += HMX_change
        HMY += HMY_change

        LBX += LBX_change
        LBY += LBY_change

        CNX += CNX_change
        CNY += CNY_change

    draw(LBX, LBY, CNX, CNY, HMX, HMY)

    collision_LB_HM = collision(LBX, LBY, CNX, CNY, HMX, HMY)
    collision_CN_HM = collision(LBX, LBY, CNX, CNY, HMX, HMY)

    if collision_LB_HM or collision_CN_HM:
        game_over_state = False
        game_over()

    pygame.display.update()
