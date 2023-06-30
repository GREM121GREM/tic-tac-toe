import random

import pygame
pygame.init()

WIDTH = 300
HEIGHT = 300
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 8, 255)
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("крестики нолики")
field = [
    ["","",""],
    ["","",""],
    ["","",""]
]
def draw_grid():
    pygame.draw.line(screen, BLACK, (100,0),(100,300), 3)
    pygame.draw.line(screen, BLACK, (200,0),(200,300), 3)
    pygame.draw.line(screen, BLACK, (0,100),(300,100), 3)
    pygame.draw.line(screen, BLACK, (0,200),(300,200), 3)

def draw_item():
    for x in range(3):
        for y in range(3):
            if field[x][y] == "X":
                pygame.draw.line(screen, GREEN, (y*100+10,x*100+10),(y*100+90,x*100+90),3)
                pygame.draw.line(screen, GREEN, (y*100+90,x*100+10),(y*100+10,x*100+90),3)
            elif field[x][y] == "0":
                pygame.draw.circle(screen, RED, (y*100+50,x*100+50), 45, 3)
#noinspection PyGlobalUndefined
def check_win(symbol):
    flag_win = False
    global win
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            win = [[0,field.index(line)],[1,field.index(line)],[2,field.index(line)]]
    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] == symbol:
            flag_win = True
            win = [[column,0],[column,1],[column,2]]
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0,0],[1,1],[2,2]]
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0,2],[1,1],[2,0]]
    return flag_win

game_run = True
game_over =False

while game_run:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)
            if field[mouse_position[1]//100][mouse_position[0]//100] == "":
                field[mouse_position[1] // 100][mouse_position[0] // 100] = "X"
                x = random.randint(0,2)
                y = random.randint(0,2)
                while field[x][y] != "":
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                field[x][y] = "0"
            print(field)
        player_win = check_win("X")
        ai_win = check_win("0")
        items = field[0].count("X")+\
            field[0].count("0")+\
            field[1].count("X")+\
            field[1].count("0")+\
            field[2].count("X")+\
            field[2].count("0")

        if player_win or ai_win:
            game_over = True
            if player_win:
                pygame.display.set_caption("Вы выиграли")

            elif ai_win:
                pygame.display.set_caption("ИИ выиграл")

        elif items == 8:
            pygame.display.set_caption("Ничья")
    if game_over:
        pygame.draw.rect(screen, BLUE, (win[0][0]*100, win[0][1]*100,100,100))
        pygame.draw.rect(screen, BLUE, (win[1][0]*100, win[1][1]*100,100,100))
        pygame.draw.rect(screen, BLUE, (win[2][0]*100, win[2][1]*100,100,100))
    draw_grid()
    draw_item()
    pygame.display.flip()

pygame.quit()

