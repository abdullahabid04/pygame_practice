import numpy as np
import pygame
import sys
import math
from utilities import blit_text


pygame.init()

ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARESIZE = 100

RADIUS = int(SQUARESIZE / 2 - 5)

WIDTH = COLUMN_COUNT * SQUARESIZE
HIEGHT = (ROW_COUNT + 1) * SQUARESIZE

SIZE = (WIDTH, HIEGHT)

SCREEN = pygame.display.set_mode(SIZE)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

myFont = pygame.font.SysFont("monospace", 75)


def create_board():
    board = np.zeros((6, 7))
    board = np.flip(board, 0)
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    board = np.flip(board, 0)
    print(board)


def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    for c in range(3, COLUMN_COUNT):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def draw(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(SCREEN, BLACK, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(SCREEN, WHITE, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(SCREEN, BLUE, (int(c * SQUARESIZE + SQUARESIZE / 2), HIEGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(SCREEN, GREEN, (int(c * SQUARESIZE + SQUARESIZE / 2), HIEGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    pygame.display.update()


def blit_text(win, font, text, color):
    blit_text(win, font, text, color)

    pygame.display.update()


game_board = create_board()
game_over = False
turn = 0

draw(game_board)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, SQUARESIZE))
            posx = event.pos[0]

            if turn == 0:
                pygame.draw.circle(SCREEN, BLUE, (posx, int(SQUARESIZE / 2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(SCREEN, GREEN, (posx, int(SQUARESIZE / 2)), RADIUS)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(game_board, col):
                    row = get_next_open_row(game_board, col)
                    drop_piece(game_board, row, col, 1)

                    if winning_move(game_board, 1):
                        blit_text(SCREEN, myFont, "PLAYER 1 WINS", RED)
                        game_over = True
            elif turn == 1:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(game_board, col):
                    row = get_next_open_row(game_board, col)
                    drop_piece(game_board, row, col, 2)

                    if winning_move(game_board, 2):
                        blit_text(SCREEN, myFont, "PLAYER 2 WINS", RED)
                        game_over = True

            turn += 1
            turn = turn % 2

            draw(game_board)
            print_board(game_board)

    pygame.display.update()
