#!/usr/bin/python3

import pygame
import random

pygame.init()


greenl=(64,224,208)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,128,0)
cyan=(0,255,255)
blue=(73,157,245)
yellow=(255,255,0)

screen_width = 1900
screen_height = 1000
gameWindow = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Rizwan Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)








def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.ellipse(gameWindow, color, [x, y, snake_size, snake_size])



def gameloop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    cheat=0
    snk_length = 1
    with open("high.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    c=1
    bp=0
    score = 0
    init_velocity = 2
    snake_size = 30
    fps = 120
    rb=0
    ub=0
    lb=0
    db=0
    with open("high.txt", "r") as f:
        hiscore = f.read()


    while not exit_game:
        if game_over:
            with open("high.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("      Game Over  !", red, 690, 350)
            text_screen("Press Enter To Continue", red, 650, 450)
            text_screen("Developed By RIZWAN" ,cyan,680,700)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:


                    if event.key == pygame.K_RETURN:

                        gameloop()




        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and lb!=1:
                        velocity_x = init_velocity
                        velocity_y = 0
                        rb=1
                        lb=0
                        db=0
                        ub=0
                        bp+=1

                    if event.key == pygame.K_LEFT and rb!=1:
                        velocity_x = - init_velocity
                        velocity_y = 0
                        lb=1
                        rb=0
                        db=0
                        ub=0
                        bp+=1

                    if event.key == pygame.K_UP and db!=1:
                        velocity_y = - init_velocity
                        velocity_x = 0
                        ub = 1
                        db = 0
                        lb=0
                        rb=0
                        bp+=1

                    if event.key == pygame.K_DOWN and ub!=1:
                        velocity_y = init_velocity
                        velocity_x = 0
                        db=1
                        ub=0
                        lb=0
                        rb=0
                        bp+=1

                    if event.key == pygame.K_i:
                        score+=20

                    if event.key == pygame.K_c:
                        cheat=1
                    if event.key == pygame.K_d:
                        cheat=0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if(init_velocity>7):
                init_velocity=7
            if abs(snake_x - food_x) < 40 and abs(snake_y - food_y) < 40:
                if(c%5==0):
                    score+=(8-bp)*10
                else:
                  score += (8-bp)*5
                init_velocity+=1
                c+=1
                bp=0
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score
            if(bp>7):
                if(c%5==0):
                  score-=150
                else:
                    score-=50
                init_velocity-=1
                c+=1
                bp=0
                food_x = random.randint(200, screen_width-250)
                food_y = random.randint(400, screen_height-300)


            gameWindow.fill(greenl)
            text_screen("Score: " + str(score), blue, 1500, 5)
            text_screen("Attempt: " + str(8-bp), yellow, 750, 5)
            text_screen("Hi Score: " + str(hiscore), green, 5, 5)

            print(c)
            if(c%5!=0):
             pygame.draw.ellipse(gameWindow, red, [food_x, food_y, snake_size+10, snake_size+10])

            else:
                color = [red, black, green, cyan,greenl,blue,yellow]
                pygame.draw.ellipse(gameWindow,random.choice(color), [food_x, food_y, snake_size + 40, snake_size + 40])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1] and cheat<=0:

                game_over = True

            if snake_x < 0 and cheat<=0 or snake_x > screen_width and cheat<=0 or snake_y < 0 and cheat<=0 or snake_y > screen_height and cheat<=0:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


gameloop()




