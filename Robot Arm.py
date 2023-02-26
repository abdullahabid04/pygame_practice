# ============================================================================
# * This code displays the motion of a 3-Arms of Robot                       *
# * The 3 Arms are shown by straight lines                                   *
# * These arms are controlled from the keyboard                              *
# * Arrow keys controls  the movement of first arm                           *
# * Alphabets keys (w, a, s, d) controls the movement of second arm          *
# * Alphabets keys (i, j, k, l) controls the movement of third arm           *
# * If you find any mistake in my code Let me know                           *
# * Prepared by :                                                            *
# *              Abdullah                                                    *
# ============================================================================

import pygame   # imports the pygame library
import time     # imports the time library


pygame.init()   # initialize pygame

screen = pygame.display.set_mode((800, 600))   # Sets height and width of screen

pygame.display.set_caption("Robot Arm")   # Sets the caption on the screen

icon = pygame.image.load('images/pic1.png')   # loads  the image and stores in variable icon
pygame.display.set_icon(icon)   # Sets icon on the screen


# ========================================
# Variables for position of arms
# ========================================

Arm1_start_x = 200   # x coordinate of start position of arm1
Arm1_start_y = 500   # y coordinate of start position of arm1
Arm1_end_x = 200   # x coordinate of end position of arm1
Arm1_end_y = 400   # y coordinate of end position of arm1

Arm2_start_x = Arm1_end_x   # x coordinate of start position of arm2
Arm2_start_y = Arm1_end_y   # y coordinate of start position of arm2
Arm2_end_x = 300   # x coordinate of end position of arm2
Arm2_end_y = 300   # y coordinate of end position of arm2

Arm3_start_x = Arm2_end_x   # x coordinate of start position of arm3
Arm3_start_y = Arm2_end_y   # y coordinate of start position of arm3
Arm3_end_x = 400   # x coordinate of end position of arm3
Arm3_end_y = 250   # y coordinate of end position of arm3

Arm4_start_x = Arm3_end_x   # x coordinate of start position of arm4
Arm4_start_y = Arm3_end_y   # y coordinate of start position of arm4
Arm4_end_x = 500   # x coordinate of end position of arm4
Arm4_end_y = 225   # y coordinate of end position of arm4

# ========================================
# variables for changing position of arms
# ========================================

Arm2_start_x_change = 0   # change of x coordinate of start position of arm2
Arm2_start_y_change = 0   # change of y coordinate of start position of arm2
Arm2_end_x_change = 0   # change of x coordinate of end position of arm2
Arm2_end_y_change = 0   # change of y coordinate of end position of arm2

Arm3_start_x_change = 0   # change of x coordinate of start position of arm3
Arm3_start_y_change = 0   # change of y coordinate of start position of arm3
Arm3_end_x_change = 0   # change of x coordinate of end position of arm3
Arm3_end_y_change = 0   # change of y coordinate of end position of arm3

Arm4_start_x_change = 0   # change of x coordinate of start position of arm4
Arm4_start_y_change = 0   # change of y coordinate of start position of arm4
Arm4_end_x_change = 0   # change of x coordinate of end position of arm4
Arm4_end_y_change = 0   # change of y coordinate of end position of arm4

run = True   # test variable for while loop

while run:
    screen.fill((80, 160, 240))   # Sets the background color of screen

    for event in pygame.event.get():   # loops through all the events in pygame.events
        if event.type == pygame.QUIT:   # checks wheather the X button is clicked on the screen
            run = False   # if clicked set run to False

        if event.type == pygame.KEYDOWN:   # checks that any key is pressed on the keyboard
            # <-movement keys for arm1->

            if event.key == pygame.K_UP:
                Arm2_end_y_change = -1
                Arm3_start_y_change = -1
                Arm3_end_y_change = -1
                Arm4_start_y_change = -1
                Arm4_end_y_change = -1

            if event.key == pygame.K_DOWN:
                Arm2_end_y_change = 1
                Arm3_start_y_change = 1
                Arm3_end_y_change = 1
                Arm4_start_y_change = 1
                Arm4_end_y_change = 1

            if event.key == pygame.K_RIGHT:
                Arm2_end_x_change = 1
                Arm3_start_x_change = 1
                Arm3_end_x_change = 1
                Arm4_start_x_change = 1
                Arm4_end_x_change = 1

            if event.key == pygame.K_LEFT:
                Arm2_end_x_change = -1
                Arm3_start_x_change = -1
                Arm3_end_x_change = -1
                Arm4_start_x_change = -1
                Arm4_end_x_change = -1

            # ==========END==========

            # <-movement keys for arm2->

            if event.key == pygame.K_w:
                Arm3_end_y_change = -1
                Arm4_start_y_change = -1
                Arm4_end_y_change = -1

            if event.key == pygame.K_s:
                Arm3_end_y_change = 1
                Arm4_start_y_change = 1
                Arm4_end_y_change = 1

            if event.key == pygame.K_d:
                Arm3_end_x_change = 1
                Arm4_start_x_change = 1
                Arm4_end_x_change = 1

            if event.key == pygame.K_a:
                Arm3_end_x_change = -1
                Arm4_start_x_change = -1
                Arm4_end_x_change = -1

            # ==========END==========

            # <-movement keys for arm3->

            if event.key == pygame.K_i:
                Arm4_end_y_change = -1

            if event.key == pygame.K_k:
                Arm4_end_y_change = 1

            if event.key == pygame.K_l:
                Arm4_end_x_change = 1

            if event.key == pygame.K_j:
                Arm4_end_x_change = -1

            # ==========END==========

        if event.type == pygame.KEYUP:   # checks that key is released
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Arm2_end_y_change = 0
                Arm3_start_y_change = 0
                Arm3_end_y_change = 0
                Arm4_start_y_change = 0
                Arm4_end_y_change = 0

            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                Arm2_end_x_change = 0
                Arm3_start_x_change = 0
                Arm3_end_x_change = 0
                Arm4_start_x_change = 0
                Arm4_end_x_change = 0

            if event.key == pygame.K_w or event.key == pygame.K_s:
                Arm3_end_y_change = 0
                Arm4_start_y_change = 0
                Arm4_end_y_change = 0

            if event.key == pygame.K_d or event.key == pygame.K_a:
                Arm3_end_x_change = 0
                Arm4_start_x_change = 0
                Arm4_end_x_change = 0

            if event.key == pygame.K_i or event.key == pygame.K_k:
                Arm4_end_y_change = 0

            if event.key == pygame.K_j or event.key == pygame.K_l:
                Arm4_end_x_change = 0

    # =========================setting the coordinates of the arms============================

    Arm2_start_x += Arm2_start_x_change
    Arm2_start_y += Arm2_start_y_change
    Arm2_end_x += Arm2_end_x_change
    Arm2_end_y += Arm2_end_y_change

    Arm3_start_x += Arm3_start_x_change
    Arm3_start_y += Arm3_start_y_change
    Arm3_end_x += Arm3_end_x_change
    Arm3_end_y += Arm3_end_y_change

    Arm4_start_x += Arm4_start_x_change
    Arm4_start_y += Arm4_start_y_change
    Arm4_end_x += Arm4_end_x_change
    Arm4_end_y += Arm4_end_y_change

    # ========================================================================================

    # ====================Keeps the arms in a specified range=================================

    # ============x coordinates of arms===========

    if Arm2_end_x <= 100:
        Arm2_end_x = 100

    if Arm2_end_x >= 700:
        Arm2_end_x = 700

    if Arm3_start_x <= 100:
        Arm3_start_x = 100

    if Arm3_start_x >= 700:
        Arm3_start_x = 700

    if Arm3_end_x <= 100:
        Arm3_end_x = 100

    if Arm3_end_x >= 700:
        Arm3_end_x = 700

    if Arm4_start_x <= 100:
        Arm4_start_x = 100

    if Arm4_start_x >= 700:
        Arm4_start_x = 700

    if Arm4_end_x <= 100:
        Arm4_end_x = 100

    if Arm4_end_x >= 700:
        Arm4_end_x = 700

    # ============y coordinates of arms===========

    if Arm2_end_y <= 100:
        Arm2_end_y = 100

    if Arm2_end_y >= 500:
        Arm2_end_y = 500

    if Arm3_start_y <= 100:
        Arm3_start_y = 100

    if Arm3_start_y >= 500:
        Arm3_start_y = 500

    if Arm3_end_y <= 100:
        Arm3_end_y = 100

    if Arm3_end_y >= 500:
        Arm3_end_y = 500

    if Arm4_start_y <= 100:
        Arm4_start_y = 100

    if Arm4_start_y >= 500:
        Arm4_start_y = 500

    if Arm4_end_y <= 100:
        Arm4_end_y = 100

    if Arm4_end_y >= 500:
        Arm4_end_y = 500

    # ========================================================================================

    # =======================Draw four lines on the screen====================================

    pygame.draw.line(screen, (0, 0, 0), (Arm1_start_x, Arm1_start_y), (Arm1_end_x, Arm1_end_y), 4)
    pygame.draw.line(screen, (255, 0, 0), (Arm2_start_x, Arm2_start_y), (Arm2_end_x, Arm2_end_y), 4)
    pygame.draw.line(screen, (0, 255, 0), (Arm3_start_x, Arm3_start_y), (Arm3_end_x, Arm3_end_y), 4)
    pygame.draw.line(screen, (0, 0, 255), (Arm4_start_x, Arm4_start_y), (Arm4_end_x, Arm4_end_y), 4)
    # ========================================================================================

    # ==========================Draw circles on the joints of arms============================

    pygame.draw.circle(screen, (0, 0, 0), (Arm1_end_x, Arm1_end_y), 20, 3)
    pygame.draw.circle(screen, (0, 0, 0), (Arm2_end_x, Arm2_end_y), 20, 3)
    pygame.draw.circle(screen, (0, 0, 0), (Arm3_end_x, Arm3_end_y), 20, 3)
    pygame.draw.circle(screen, (0, 0, 0), (Arm4_end_x, Arm4_end_y), 20, 3)

    # ==========================Draw the base of the first arm================================

    pygame.draw.line(screen, (0, 0, 0), (Arm1_start_x - 50, Arm1_start_y), (Arm1_start_x + 50, Arm1_start_y), 10)

    # ========================================================================================

    pygame.display.update()   # updates the display on the screen every time the loop iterates

    time.sleep(0.03)   # adds a delay before the next iteration

    # =====================================THE END============================================
