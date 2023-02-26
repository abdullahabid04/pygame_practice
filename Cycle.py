import pygame
import math


ScreenWidth = 1320
ScreenHeight = 660


pygame.init()
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("C I R C U L A R   M O T I O N")
icon = pygame.image.load("images/lab_logo.png")
pygame.display.set_icon(icon)

x = 100
y = 100

angle = 0

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((50, 75, 255))

    for i in range(1, 6, 2):
        for j in range(0, 11, 2):
            pygame.draw.circle(win, (255, 255, 255), (110 + (110 * j), 110 * i), 110, 20)
            x1, y1 = x * math.cos(angle) + (110 + (110 * j)), y * math.sin(angle) + (110 * i)
            pygame.draw.circle(win, (0, 0, 0), (x1, y1), 10)

    angle -= 0.01

    pygame.display.update()
