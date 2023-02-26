import pygame
import math
import random

pygame.init()

window = pygame.display.set_mode((1024, 768))

pygame.display.set_caption("G A M E")

icon = pygame.image.load('images/bg.png')
pygame.display.set_icon(icon)

BG = pygame.image.load('images/pic1.png')

coordinate_change = 15

LB = pygame.image.load('images/lb.png')
LBX = 250
LBY = 600
LBX_change = 0
LBY_change = 0

CN = pygame.image.load('images/cn.png')
CNX = 700
CNY = 600
CNX_change = 0
CNY_change = 0

HM = pygame.image.load('images/hm.png')
HMX = random.randint(50, 1000)
HMY = random.randint(25, 100)
HMX_change = coordinate_change
HMY_change = coordinate_change

LB_score = 0
CN_score = 0

LB_score_X = 10
LB_score_Y = 10
CN_score_X = 680
CN_score_Y = 10

font = pygame.font.Font('freesansbold.ttf', 32)


def show_LB_score(x, y):
    score_LB = font.render("Player 1 Score : " + str(LB_score), True, (0, 0, 0))
    window.blit(score_LB, (x, y))


def show_CN_score(x, y):
    score_CN = font.render("Player 2 Score : " + str(CN_score), True, (0, 0, 0))
    window.blit(score_CN, (x, y))


def draw(x1, y1, x2, y2, x3, y3):
    window.blit(LB, (x1, y1))
    window.blit(CN, (x2, y2))
    window.blit(HM, (x3, y3))


def LB_collision(HMX, HMY, LBX, LBY):
    LB_HM_distance = math.sqrt(math.pow(HMX - LBX, 2) + math.pow(HMY - LBY, 2))

    if LB_HM_distance < 32:
        return True
    else:
        return False


def CN_collision(HMX, HMY, CNX, CNY):
    CN_HM_distance = math.sqrt(math.pow(HMX - CNX, 2) + math.pow(HMY - CNY, 2))

    if CN_HM_distance < 32:
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
            if event.key == pygame.K_UP:
                LBY_change -= coordinate_change
            if event.key == pygame.K_DOWN:
                LBY_change += coordinate_change
            if event.key == pygame.K_LEFT:
                LBX_change -= coordinate_change
            if event.key == pygame.K_RIGHT:
                LBX_change += coordinate_change
            if event.key == pygame.K_w:
                CNY_change -= coordinate_change
            if event.key == pygame.K_s:
                CNY_change += coordinate_change
            if event.key == pygame.K_a:
                CNX_change -= coordinate_change
            if event.key == pygame.K_d:
                CNX_change += coordinate_change

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                LBY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                LBX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                CNY_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                CNX_change = 0

    if LBX <= 10:
        LBX = 10
    if LBX >= 950:
        LBX = 950
    if LBY <= 20:
        LBY = 20
    if LBY >= 675:
        LBY = 675

    if CNX <= 10:
        CNX = 10
    if CNX >= 950:
        CNX = 950
    if CNY <= 20:
        CNY = 20
    if CNY >= 675:
        CNY = 675

    if HMX <= 0:
        HMX_change += coordinate_change
    if HMX >= 960:
        HMX_change -= coordinate_change
    if HMY <= 0:
        HMY_change += coordinate_change
    if HMY >= 700:
        HMY_change -= coordinate_change

    collision_LB = LB_collision(HMX, HMY, LBX, LBY)
    collision_CN = CN_collision(HMX, HMY, CNX, CNY)

    if collision_LB:
        LB_score += 1

        if LBY <= HMY:
            if LBX <= HMX:
                LBX -= 15
                LBY -= 15
                HMX_change = coordinate_change
                HMY_change = coordinate_change

            if LBX >= HMX:
                LBX += 15
                LBY -= 15
                HMX_change = -coordinate_change
                HMY_change = coordinate_change

        if LBY >= HMY:
            if LBX <= HMX:
                LBX -= 15
                LBY += 15
                HMX_change = coordinate_change
                HMY_change = -coordinate_change

            if LBX >= HMX:
                LBX += 15
                LBY += 15
                HMX_change = -coordinate_change
                HMY_change = -coordinate_change

    if collision_CN:
        CN_score += 1

        if CNY <= HMY:
            if CNX <= HMX:
                CNX -= 15
                CNY -= 15
                HMX_change = coordinate_change
                HMY_change = coordinate_change

            if CNX >= HMX:
                CNX += 15
                CNY -= 15
                HMX_change = -coordinate_change
                HMY_change = coordinate_change

        if CNY >= HMY:
            if CNX <= HMX:
                CNX -= 15
                CNY += 15
                HMX_change = coordinate_change
                HMY_change = -coordinate_change

            if CNX >= HMX:
                CNX += 15
                CNY += 15
                HMX_change = -coordinate_change
                HMY_change = -coordinate_change

    HMX += HMX_change
    HMY += HMY_change

    LBX += LBX_change
    LBY += LBY_change

    CNX += CNX_change
    CNY += CNY_change

    draw(LBX, LBY, CNX, CNY, HMX, HMY)

    show_LB_score(LB_score_X, LB_score_Y)
    show_CN_score(CN_score_X, CN_score_Y)

    pygame.display.update()
