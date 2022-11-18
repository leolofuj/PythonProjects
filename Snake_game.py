import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

victory = ""

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka@ implemented by Leonardo@')

clock = pygame.time.Clock()

snake_block = 10
snake_playerA = 10
snake_playerB = 5
snake_detour = 50
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)
text_font = pygame.font.SysFont("comicsansms", 12)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    value_2 = text_font.render("Try to eat the food 3 times faster to beat your opponent" + str(), True, black)
    value_3 = text_font.render("Game speed: press 1 - normal  press 2 - faster press 3 - much faster" + str(), True, yellow)
    dis.blit(value, [0, 0])
    dis.blit(value_2, [0, 35])
    dis.blit(value_3, [200, 380])

def Cpu_score(score):
    value = score_font.render("Player A  Score: " + str(score), True, red)
    dis.blit(value, [380, 0])



def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def our_snake_2(snake_block, snake_list_2):
    for x in snake_list_2:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    x2 = dis_width / 4
    y2 = dis_height / 4

    x2_change = 0
    y2_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_List_2 = []
    Length_of_snake_2 = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You {}! Press C-Play Again or Q-Quit".format(victory), red)
            Your_score(Length_of_snake - 1)
            Cpu_score(Length_of_snake_2 - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        

        # Player 2 controls
        if foody < y2 and foodx > x2:
            x2_change += snake_playerB
            y2_change = 0
            if x2 > foodx - snake_detour:
                x2_change = 0
                y2_change -= snake_playerB
                if y2 <= foody + snake_detour:
                    y2_change = 0
                    x2_change += snake_playerB

        if foody < y2 and foodx < x2:
            x2_change -= snake_playerB
            y2_change = 0
            if x2 < foodx + snake_detour:
                x2_change = 0
                y2_change -= snake_playerB
                if y2 <= foody + snake_detour:
                    y2_change = 0
                    x2_change -= snake_playerB

        if foody > y2 and foodx < x2:
            x2_change -= snake_playerB
            y2_change = 0
            if x2 < foodx + snake_detour:
                x2_change = 0
                y2_change += snake_playerB
                if y2 >= foody - snake_detour:
                    y2_change = 0
                    x2_change -= snake_playerB

        if foody > y2 and foodx > x2:
            x2_change += snake_playerB
            y2_change = 0
            if x2 > foodx - snake_detour:
                x2_change = 0
                y2_change += snake_playerB
                if y2 >= foody - snake_detour:
                    y2_change = 0
                    x2_change += snake_playerB
                    
        if foody == y2 and foodx > x2:
            x2_change += snake_playerB
            y2_change = 0
            
        if foody == y2 and foodx < x2:
            x2_change -= snake_playerB
            y2_change = 0
           
        if foodx == x2 and foody < y2:
            y2_change -= snake_playerB
            x2_change = 0
            
        if foodx == x2 and foody > y2:
            y2_change += snake_playerB
            x2_change = 0

        # your player controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_playerA
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_playerA
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_playerA
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_playerA
                    x1_change = 0
                # game speed
                if event.key == pygame.K_1:
                    snake_speed = 10
                    print(snake_speed)
                elif event.key == pygame.K_2:
                    snake_speed = 20
                    print(snake_speed)
                elif event.key == pygame.K_3:
                    snake_speed = 30
                    print(snake_speed)

                

        # TODO Fix the players eating moment
        if foody == y2 and foodx == x2:
            y2_change = 0
            x2_change = 0
            foodx = None
            foody = None
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_2 += 1
            if Length_of_snake_2 == 4:
                victory = "Lost"
                game_close = True
                
        # TODO Fix the players eating moment
        if foody == y1 and foodx == x1:
            y1_change = 0
            x1_change = 0
            foodx = None
            foody = None
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            if Length_of_snake == 4:
                victory = "Won"
                game_close = True

        # control the movement over the boundaries
        if y2 < 0 or x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            x2 = dis_width/2
            y2 = dis_height/2

        if y1 < 0 or x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            x1 = dis_width/2
            y1 = dis_height/2

        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change

        dis.fill(blue)
        # draw the obj in scene
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head_2 = []
        snake_Head_2.append(x2)
        snake_Head_2.append(y2)
        snake_List_2.append(snake_Head_2)
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if len(snake_List_2) > Length_of_snake_2:
            del snake_List_2[0]

        our_snake(snake_block, snake_List)
        our_snake_2(snake_block, snake_List_2)
        Your_score(Length_of_snake - 1)
        Cpu_score(Length_of_snake_2 - 1)

            
        pygame.display.update()

        clock.tick(snake_speed)
       

    pygame.quit()
    quit()


gameLoop()