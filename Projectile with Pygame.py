import pygame
import math
import time as t


ScreenWidth = 1200
ScreenHeight = 600

x = 0
y = 0
time = 0
force = 0
angle = 0
release = False

GravitationalAcceleration = -9.8


pygame.init()
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("P R O J E C T I L E    M O T I O N")
icon = pygame.image.load("images/lab_logo.png")
pygame.display.set_icon(icon)


class Ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius - 1)

    def coordinates_of_ball(self, initial_x, initial_y, force, angle, time):
        x_component = math.cos(angle) * force
        y_component = math.sin(angle) * force

        distance_x = x_component * time
        distance_y = (y_component * time) + ((GravitationalAcceleration * (math.pow(time, 2))) / 2)

        final_x = round(distance_x + initial_x)
        final_y = round(initial_y - distance_y)

        return (final_x, final_y)


font = pygame.font.Font('freesansbold.ttf', 15)


def texts():
    angletxt = font.render("angle   : " + str(int(math.degrees(angle))), True, (0, 0, 0))
    timetxt = font.render("time     : " + str(int(time)), True, (0, 0, 0))
    coordinatestxt = font.render("X : " + str(int(ball.x)) + " , " + "y : " + str(int(ball.y)), True, (0, 0, 0))
    forcetxt = font.render("force    : " + str(int(force)), True, (0, 0, 0))

    win.blit(angletxt, (10, 10))
    win.blit(timetxt, (10, 40))
    win.blit(coordinatestxt, (10, 55))
    win.blit(forcetxt, (10, 25))


def update_window():
    win.fill((64, 64, 64))

    ball.draw(win)

    pygame.draw.line(win, (0, 0, 0), (7, 7), (125, 7))
    pygame.draw.line(win, (0, 0, 0), (7, 7), (7, 70))
    pygame.draw.line(win, (0, 0, 0), (7, 70), (125, 70))
    pygame.draw.line(win, (0, 0, 0), (125, 70), (125, 7))

    texts()

    pygame.display.update()


def find_angle(pos):
    ball_x = ball.x
    ball_y = ball.y

    try:
        angle = math.atan((ball_y - pos[1]) / (ball_x - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < ball_y and pos[0] > ball_x:
        angle = abs(angle)
    elif pos[1] < ball_y and pos[0] < ball_x:
        angle = math.pi - angle
    elif pos[1] > ball_y and pos[0] < ball_x:
        angle = math.pi + abs(angle)
    elif pos[1] > ball_y and pos[0] > ball_x:
        angle = (math.pi * 2) - angle

    return angle


ball = Ball(600, 593, 7, (255, 255, 255))

run = True

while run:
    if release:
        if ball.y <= ScreenHeight - ball.radius:
            time += 0.025
            Pos = Ball.coordinates_of_ball(ball, x, y, force, angle, time)
            ball.x = Pos[0]
            ball.y = Pos[1]

            if ball.x > ScreenWidth - ball.radius:
                ball.x = ScreenWidth - ball.radius
            elif ball.x < 0:
                ball.x = ball.radius
        else:
            ball.y = ScreenHeight - ball.radius
            release = False

    pos = pygame.mouse.get_pos()
    line = [(ball.x, ball.y), pos]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if release is False:
                release = True
                x = ball.x
                y = ball.y
                time = 0
                force = math.sqrt(math.pow(line[1][1] - line[0][1], 2) + math.pow(line[1][0] - line[0][0], 2)) / 8
                angle = find_angle(pos)

    update_window()

pygame.quit()
