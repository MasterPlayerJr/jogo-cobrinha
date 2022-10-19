import pygame
import random
from time import sleep
pygame.init() # Inicia o programa

# Cores:

red, green, blue = (255,0,0), (0,255,0), (0,0,255)
white, black = (255,255,255), (0,0,0)
gray = (80,80,80)
dark_green = (0,155,0)
brown = (128,0,0)
orange = (255,69,0)
yellow = (255, 255, 102)

dis_width = 800
dis_height = 600

display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Jogo da cobrinha')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
score_number = 0

font = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont('comicsansms',35)

def pause():
    paused = True
    pause_msg = font.render("Pausado", True, black)
    display.fill(gray)
    display.blit(pause_msg, [dis_width / 2.28, dis_height / 2.4])
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
        display.fill(white)
    sleep(0.2)

def score(score):
    try:
        score_file = open("best_scores.txt",'r')
        best_score = score_file.readline()
    except FileNotFoundError:
        best_score = "0"
    value = font.render((f"Pontuação:{score}(Melhor:{best_score})"),True, black)
    display.blit(value, [0,0])

def save_score(score):
    try:
        with open('best_scores.txt', 'r') as score_file:
            score_value_old = score_file.read()
    except FileNotFoundError:
        with open('best_scores.txt','w') as score_file:
            score_value_old = "0"
    if score > score_value_old:
        score_value_old = score_value_old.replace(str(score_value_old),str(score))
    with open('best_scores.txt', 'w') as score_file:
        score_file.write(score_value_old)
        

def snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(display,brown, [i[0], i[1], snake_block, snake_block])

def message(msg,color):
    message = font.render(msg, True, color)
    display.blit(message,[dis_width / 12, dis_height / 2.5])                     

def main_game():
    game_over = False
    game_close = False

    x1 = round(dis_width / 2)
    y1 = round(dis_height / 2)

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_lengh = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    direction = "NONE"

    while not game_over:
        while game_close == True:
            display.fill(dark_green)
            message("Você perdeu! Aperta ESC-Sair or C-Jogar denovo",black)
            score(snake_lengh - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                        save_score(str(snake_lengh - 1))
                    if event.key == pygame.K_c:
                        save_score(str(snake_lengh - 1))
                        main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                if event.key == pygame.K_r:
                    main_game()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if direction != "RIGHT":
                        x1_change = -10
                        y1_change = 0
                        direction = "LEFT"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if direction != "LEFT":
                        x1_change = 10
                        y1_change = 0
                        direction = "RIGHT"
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if direction != "DOWN":
                        x1_change = 0
                        y1_change = -10
                        direction = "UP"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if direction != "UP":
                        x1_change = 0
                        y1_change = 10
                        direction = "DOWN"

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(dark_green)
        pygame.draw.rect(display,orange,[foodx, foody, snake_block, snake_block]) # Cria a comida

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_lengh:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:  # Verifica se a minhoca se acertou
                game_close = True

        snake(snake_block, snake_list)
        score(snake_lengh - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0,dis_height - snake_block) / 10) * 10
            snake_lengh += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

## Programa

main_game()