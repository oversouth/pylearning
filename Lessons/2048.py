import random

import pygame


class Block:
    WIDTH = 100
    HEIGHT = 100

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def can_merge(self, other):
        return self.value == other.value

    def merge(self, other):
        return Block(self.value + other.value)


def init_area():
    area = pygame.Rect(100, 300, 400, 400)
    pygame.draw.rect(screen, AREA_COLOR, area, border_radius=10)

    for row in MATRIX:
        for cell in row:
            rect = pygame.Rect(cell[0] + 10, cell[1] + 10, 80, 80)
            pygame.draw.rect(screen, CELL_COLOR, rect, border_radius=5)


def spawn_new():
    empty_blocks = []
    for ROW in BLOCKS:
        for block in ROW:
            if block.value == 0:
                empty_blocks.append(block)
    res = random.choice(empty_blocks)
    res.value = 2


def proceed_blocks():
    font = pygame.font.SysFont("Arial", 48)

    for i in range(4):
        for j in range(4):
            if BLOCKS[i][j].value == 0:
                continue
            surface = font.render(str(BLOCKS[i][j].value), True, (0, 0, 0))
            screen.blit(surface, (MATRIX[i][j][0] + 25, MATRIX[i][j][1] + 25))


HEIGHT = 800
WIDTH = 600
RESOLUTION = (WIDTH, HEIGHT)
MATRIX = (
    ((100, 300), (200, 300), (300, 300), (400, 300)),
    ((100, 400), (200, 400), (300, 400), (400, 400)),
    ((100, 500), (200, 500), (300, 500), (400, 500)),
    ((100, 600), (200, 600), (300, 600), (400, 600)),
)
AREA_COLOR = (187, 173, 160)
CELL_COLOR = (205, 193, 180)
BACKGROUND_COLOR = (204, 192, 179)
DIGIT_COLOR = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

pygame.init()

screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

pygame.display.set_caption("2048")

BLOCKS = [
    [Block(0), Block(0), Block(0), Block(0)],
    [Block(0), Block(0), Block(0), Block(0)],
    [Block(0), Block(0), Block(0), Block(0)],
    [Block(0), Block(0), Block(0), Block(0)],
]

is_started = True
while is_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            is_started = False
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spawn_new()

    screen.fill(BACKGROUND_COLOR)
    init_area()
    proceed_blocks()
    pygame.display.flip()
    clock.tick(24)

pygame.quit()
