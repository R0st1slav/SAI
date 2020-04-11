"""Для распознавания предъявляется циферблат электронных часов,
который состоит из четырех позиций: две позиции для вывода часов и две
позиции для вывода минут (чч:мм). Каждая цифра представляется набором
пикселов из 9 строк по 6 пикселов в каждой строке. Каждый пиксел может
принимать одно из двух значений символов «*» или «.». Сочетания «*» и «.»
задают одну из 10 цифр. Образцы написания всех цифр имеются.
В идеале на циферблате часов показывается реальное время. Однако в
системе часов произошел сбой и некоторые пикселы приняли
«неправильные» значения. """

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
WIDTH = 672
HEIGHT = 384

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

verical_lines = []

running = True
while running:

    sc.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.line(sc, BLACK, (WIDTH//4, 0), (WIDTH//4, HEIGHT), 5)
    pygame.draw.line(sc, BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)
    pygame.draw.line(sc, BLACK, (WIDTH * 3/4, 0), (WIDTH * 3/4, HEIGHT), 5)

    x_offset = 0
    y_offset = 0
    while x_offset < WIDTH:
        pygame.draw.line(sc, BLACK, (0 + x_offset, 0), (0 + x_offset, HEIGHT))
        x_offset += 28

    while y_offset < HEIGHT:
        pygame.draw.line(sc, BLACK, (0, 0 + y_offset), (WIDTH, 0 + y_offset))
        y_offset += 48

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
