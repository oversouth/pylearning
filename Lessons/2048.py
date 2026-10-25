import pygame

class Block:
    WIDTH = 100
    HEIGHT = 1000
    def __init__(self,):
        self.value = self.value
        @properry
        def value(self):
            return self.value

        def can_merge(self, other):
            return self.value == other.value
        def merge(self, other):
            return Block(self.value + other.value)

HEIGHT = 600
WIDTH = 800
RESOLUTION = (WIDTH, HEIGHT)
MATRIX = (
    ((100,300), (200, 300), (300, 300), (400, 300)),
    ((100,400), (200, 400), (300, 400), (400, 400)),
    ((100,500), (200, 500), (300, 500), (400, 500)),
    ((100,600), (200, 600), (300, 600), (400, 600)),
)
BACKGROUND_COLOR = (187, 173, 160)
TILES_COLOR = {
    0: (205, 193, 180),
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
    2048: (237, 194, 46)
}
BLOCKS =[
    [Block(0), Block(0), Block(0), Block(0)],
    [Block(0), Block(0), Block(0), Block(0)],
    [Block(0), Block(0), Block(0), Block(0)],
    [Block(0), Block(0), Block(0), Block(0)]
]
pygame.init()

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption("2048")

is_started = True
while is_started:
    for evet in pygame.event.get():
        if evet.type == pygame.QUIT or (event.type == pygame.KEYDOWN and evet.key == pygame.K_ESCAPE):
            is_started = False
    print("hello from 2048.py")
clock.tick(240)
pygame.quit()

