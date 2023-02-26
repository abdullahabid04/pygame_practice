import pygame
import math


pygame.init()

win = pygame.display.set_mode((800, 800))

x = 100
y = 100

angle = 0

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((128, 128, 128))

    x1, y1 = x * math.cos(angle) + 600, y * math.sin(angle) + 200
    x2, y2 = x * math.cos(angle) + 200, y * math.sin(angle) + 200
    x3, y3 = x * math.cos(angle) + 600, y * math.sin(angle) + 600
    x4, y4 = x * math.cos(angle) + 200, y * math.sin(angle) + 600
    x5, y5 = x * math.cos(angle) + 400, y * math.sin(angle) + 400

    pygame.draw.circle(win, (255, 255, 255), (400, 400), 110)
    pygame.draw.circle(win, (255, 255, 255), (600, 200), 110)
    pygame.draw.circle(win, (255, 255, 255), (200, 200), 110)
    pygame.draw.circle(win, (255, 255, 255), (600, 600), 110)
    pygame.draw.circle(win, (255, 255, 255), (200, 600), 110)

    pygame.draw.circle(win, (0, 0, 0), (400, 400), 5)
    pygame.draw.circle(win, (0, 0, 0), (600, 200), 5)
    pygame.draw.circle(win, (0, 0, 0), (200, 200), 5)
    pygame.draw.circle(win, (0, 0, 0), (600, 600), 5)
    pygame.draw.circle(win, (0, 0, 0), (200, 600), 5)

    pygame.draw.circle(win, "blue", (x1, y1), 10)
    pygame.draw.circle(win, "blue", (x2, y2), 10)
    pygame.draw.circle(win, "blue", (x3, y3), 10)
    pygame.draw.circle(win, "blue", (x4, y4), 10)
    pygame.draw.circle(win, "blue", (x5, y5), 10)

    pygame.draw.line(win, (0, 0, 0), (600, 200), (200, 200), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 200), (200, 600), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 600), (600, 600), 5)
    pygame.draw.line(win, (0, 0, 0), (600, 600), (600, 200), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 200), (600, 600), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 600), (600, 200), 5)

    pygame.draw.line(win, (0, 0, 0), (600, 200), (x1, y1), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 200), (x2, y2), 5)
    pygame.draw.line(win, (0, 0, 0), (600, 600), (x3, y3), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 600), (x4, y4), 5)
    pygame.draw.line(win, (0, 0, 0), (400, 400), (x5, y5), 5)

    pygame.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 5)
    pygame.draw.line(win, (0, 0, 0), (x1, y1), (x3, y3), 5)
    pygame.draw.line(win, (0, 0, 0), (x3, y3), (x4, y4), 5)
    pygame.draw.line(win, (0, 0, 0), (x4, y4), (x2, y2), 5)
    pygame.draw.line(win, (0, 0, 0), (x1, y1), (x4, y4), 5)
    pygame.draw.line(win, (0, 0, 0), (x3, y3), (x2, y2), 5)

    angle += 0.01

    pygame.display.update()

pygame.quit()
