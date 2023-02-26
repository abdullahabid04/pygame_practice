import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")

spaceShip = pygame.image.load("images/lb.png")

spaceShip_x = 370
spaceShip_y = 500
spaceShip_x_change = 0
spaceShip_y_change = 0

bullet = pygame.image.load("images/cn.png")

bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = -25
bullet_state = "Ready"

spaceInvader = []
spaceInvader_x = []
spaceInvader_y = []
spaceInvader_x_change = []
spaceInvader_y_change = []

number_of_spaceInvaders = 3

for i in range(number_of_spaceInvaders):
    spaceInvader.append(pygame.image.load("images/hm.png"))

    spaceInvader_x.append(random.randint(0, 736))
    spaceInvader_y.append(random.randint(100, 200))
    spaceInvader_x_change.append(5)
    spaceInvader_y_change.append(0)

backGround = pygame.image.load("images/pic1.png")
icon = pygame.image.load("images/bg.png")

pygame.display.set_icon(icon)

score_value = 0

score_font = pygame.font.Font("freesansbold.ttf", 32)

score_text_x = 10
score_text_y = 10

game_over_font = pygame.font.Font("freesansbold.ttf", 80)

game_over_text_x = 170
game_over_text_y = 250


def game_over(x, y):
    game_over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over_text, (x, y))


def show_score(x, y):
    score_text = score_font.render("Score : " + str(score_value), False, (0, 0, 0))
    screen.blit(score_text, (x, y))


def draw_spaceShip(x, y):
    screen.blit(spaceShip, (x, y))


def draw_spaceInvader(x, y, i):
    screen.blit(spaceInvader[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet, (x, y))


def Collision(spaceInvader_x, spaceInvader_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(bullet_x - spaceInvader_x, 2)) + (math.pow(bullet_y - spaceInvader_y, 2)))

    if distance < 32:
        return True
    else:
        return False


run = True

while run:
    screen.fill((0, 0, 0))
    screen.blit(backGround, (-100, -40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spaceShip_x_change = 5

            if event.key == pygame.K_LEFT:
                spaceShip_x_change = -5

            if event.key == pygame.K_SPACE:
                if bullet_state is "Ready":
                    bullet_x = spaceShip_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                spaceShip_x_change = 0

    for i in range(number_of_spaceInvaders):
        if spaceInvader_y[i] > 400:
            for j in range(number_of_spaceInvaders):
                spaceInvader_y[j] = 2000
            game_over(game_over_text_x, game_over_text_y)
            break

        if spaceInvader_x[i] < 0:
            spaceInvader_x_change[i] = 5
            spaceInvader_y[i] += 25
        elif spaceInvader_x[i] > 736:
            spaceInvader_x_change[i] = -5
            spaceInvader_y[i] += 25

        collision = Collision(spaceInvader_x[i], spaceInvader_y[i], bullet_x, bullet_y)

        if collision:
            bullet_y = 500
            bullet_state = "Ready"
            score_value += 1
            spaceInvader_x[i] = random.randint(0, 736)
            spaceInvader_y[i] = random.randint(100, 150)

        spaceInvader_x[i] += spaceInvader_x_change[i]
        spaceInvader_y[i] += spaceInvader_y_change[i]

        draw_spaceInvader(spaceInvader_x[i], spaceInvader_y[i], i)

    spaceShip_x += spaceShip_x_change
    spaceShip_y += spaceShip_y_change

    if spaceShip_x < 0:
        spaceShip_x = 0

    if spaceShip_x > 736:
        spaceShip_x = 736

    if bullet_state is "Fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_x += bullet_x_change
        bullet_y += bullet_y_change

    if bullet_y < 0:
        bullet_y = 500
        bullet_state = "Ready"

    draw_spaceShip(spaceShip_x, spaceShip_y)

    show_score(score_text_x, score_text_y)

    pygame.display.update()
