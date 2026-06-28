import random
import time

import pygame

WIDTH = 600
HEIGHT = 400
CELL_SIZE: int = 20
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DIRECTIONS = ("UP", "LEFT", "RIGHT", "DOWN")

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()


while True:
    font = pygame.font.SysFont("Arial", 24)
    fruit = (100, 100)
    snake = [(300, 300)]
    snake_speed = 1
    snake_direction = DIRECTIONS[0]
    running = True
    while running:
        size = len(snake)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if (size == 1) or (DIRECTIONS[3] != snake_direction):
                            snake_direction = DIRECTIONS[0]
                    case pygame.K_LEFT:
                        if (size == 1) or (DIRECTIONS[2] != snake_direction):
                            snake_direction = DIRECTIONS[1]
                    case pygame.K_RIGHT:
                        if (size == 1) or (DIRECTIONS[1] != snake_direction):
                            snake_direction = DIRECTIONS[2]
                    case pygame.K_DOWN:
                        if (size == 1) or (DIRECTIONS[0] != snake_direction):
                            snake_direction = DIRECTIONS[3]

        pos = snake[0]
        if snake_direction == DIRECTIONS[0]:
            new = (pos[0], pos[1] - CELL_SIZE)
        if snake_direction == DIRECTIONS[1]:
            new = (pos[0] - CELL_SIZE, pos[1])
        if snake_direction == DIRECTIONS[2]:
            new = (pos[0] + CELL_SIZE, pos[1])
        if snake_direction == DIRECTIONS[3]:
            new = (pos[0], pos[1] + CELL_SIZE)

        snake.insert(0, new)
        if (
            new in snake[1:]
            or (snake[0][0] < 0 or snake[0][0] >= WIDTH)
            or (snake[0][1] < 0 or snake[0][1] >= HEIGHT)
        ):
            running = False
        snake.pop(-1)

        if snake[0][0] == fruit[0] and snake[0][1] == fruit[1]:
            while fruit in snake:
                fruit = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE),
                )
            snake.append(pos)

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (fruit[0], fruit[1], CELL_SIZE, CELL_SIZE))

        for segment in snake:
            pygame.draw.rect(
                screen, GREEN, (segment[0], segment[1], CELL_SIZE - 1, CELL_SIZE - 1)
            )

        text = font.render(str(len(snake)), True, (255, 255, 255))
        text.set_alpha(90)
        screen.blit(text, (CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        clock.tick(5)

    screen.fill(WHITE)
    font = pygame.font.SysFont("Arial", 84)
    font.set_bold(True)

    text = font.render("GAME OVER", True, BLACK)
    screen.blit(text, (48, 48))
    pygame.display.flip()

    one_more = False
    second = 15
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    one_more = True
                    break
        if second == 0 or one_more:
            break
        time.sleep(1)
        second -= 1
    if not one_more:
        break

pygame.quit()
