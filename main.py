import pygame
import random
from sys import exit
from time import sleep


pygame.init()
pygame.display.set_caption('Project SNAKE')
size = width, height = (720, 480)
screen = pygame.display.set_mode(size)

UGLY_BACKGROUND_GREEN = pygame.Color('#8eb367')
SNAKE_COLOR = pygame.Color('#36381b')
SCORE_COLOR = pygame.Color('#aece8b')
BLACK = pygame.Color('black')

direction = 'RIGHT'
change_to = direction

speed = 20
fps_controller = pygame.time.Clock()

score = 0

pos = [100, 100]
body = [[100, 100], [90, 100], [80, 100]]

food_pos = [random.randrange(5, 66) * 10, random.randrange(5, 42) * 10]
food_spawn = True


def game_over():
    font = pygame.font.Font(None, 90)
    game_over_surface = font.render('GAME OVER', True, SNAKE_COLOR)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    screen.fill(UGLY_BACKGROUND_GREEN)
    screen.blit(game_over_surface, game_over_rect)
    show_score('dead', SNAKE_COLOR, 33)
    pygame.display.flip()
    sleep(1.5)
    pygame.quit()
    exit()


def show_score(dead_or_live, color, font_size):
    score_font = pygame.font.Font(None, font_size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if dead_or_live == 'live':
        pygame.draw.rect(screen, SCORE_COLOR, (0, 0, 720, 480), 95)
        score_rect.midtop = (width/10, 20)
    else:
        score_rect.midtop = (width/2, height/1.25)
    screen.blit(score_surface, score_rect)


running = True
font = pygame.font.SysFont('Open Sans Bold', 150)
intro = font.render('SNAKE', 1, BLACK, UGLY_BACKGROUND_GREEN)
clock = pygame.time.Clock()
x, y = 180, 0
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    if y == 180:
        sleep(1.5)
        running = False
    clock.tick(fps)
    screen.fill(UGLY_BACKGROUND_GREEN)
    screen.blit(intro, (x, y))
    y += 1
    pygame.display.update()


pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        pos[1] -= 10
    if direction == 'DOWN':
        pos[1] += 10
    if direction == 'LEFT':
        pos[0] -= 10
    if direction == 'RIGHT':
        pos[0] += 10

    body.insert(0, list(pos))
    if pos[0] == food_pos[0] and pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        body.pop()

    if not food_spawn:
        food_pos = [random.randrange(5, 66) * 10, random.randrange(5, 42) * 10]
    food_spawn = True

    screen.fill(UGLY_BACKGROUND_GREEN)
    for pos1 in body:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos1[0], pos1[1], 10, 10))

    pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if pos[0] < 50 or pos[0] > 660:
        pygame.mixer.music.set_volume(0)
        game_over()
    if pos[1] < 50 or pos[1] > 420:
        pygame.mixer.music.set_volume(0)
        game_over()

    for block in body[1:]:
        if pos[0] == block[0] and pos[1] == block[1]:
            pygame.mixer.music.set_volume(0)
            game_over()

    show_score('live', SNAKE_COLOR, 23)
    pygame.display.update()
    fps_controller.tick(speed)
