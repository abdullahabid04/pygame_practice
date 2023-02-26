import pygame


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width() * 0.5 - render.get_width() * 0.5, win.get_height() * 0.5 - render.get_height() * 0.5))


def blit_text(win, font, text, color):
    render = font.render(text, 1, color)
    win.blit(render, (win.get_width() * 0.5 - render.get_width() * 0.5, win.get_height() * 0.5 - render.get_height() * 0.5))
