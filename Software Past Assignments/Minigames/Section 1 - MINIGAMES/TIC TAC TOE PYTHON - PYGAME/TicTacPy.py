
#GAME INITIALISATION

import pygame
import math
import random

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

display_width = 600
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

x = 40
y = 40
width = 20
height = 20
vel = 20
mode = 0

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')

gameDisplay.fill((255,255,255))
pygame.draw.line(gameDisplay, (0,0,0), (300,0), (300,600))
pygame.draw.line(gameDisplay, (0,0,0), (300,300), (340,300))
pygame.draw.line(gameDisplay, (0,0,0), (560,300), (600,300))

font = pygame.font.Font('freesansbold.ttf', 50) 
text = font.render('2 Player', True, (0, 0, 0)) 
textRect = text.get_rect()
textRect.center = (150, 300)
gameDisplay.blit(text, textRect) 

font = pygame.font.Font('freesansbold.ttf', 50) 
text = font.render('1 Player', True, (0, 0, 0)) 
textRect = text.get_rect()
textRect.center = (450, 300)
gameDisplay.blit(text, textRect) 

font = pygame.font.Font('freesansbold.ttf', 30) 
text = font.render('Easy', True, (0, 0, 0)) 
textRect = text.get_rect()
textRect.center = (450, 150)
gameDisplay.blit(text, textRect) 

font = pygame.font.Font('freesansbold.ttf', 30) 
text = font.render('Hard', True, (0, 0, 0)) 
textRect = text.get_rect()
textRect.center = (450, 450)
gameDisplay.blit(text, textRect) 

cont = False
gameMode = "easy"

while cont == False:
    clock.tick(60)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.font.quit()
                    quit()
                #CHECKS FOR MOUSE CLICK POSITION INSTEAD OF KEY PRESS
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    cont = True
                    if mx < 300:
                        mode = 1
                    else:
                        if my > 300:
                            gameMode = "hard"

    pygame.display.update()

end = False

x2 = 0
y2 = 0
rows = 3



#GAME DISPLAY SETUP

def makeGame():
    gameDisplay.fill((0,0,0))
    global x2
    global y2
    global rows
    for i in range(rows):
        x2 = x2 + 200
        y2 = y2 + 200

        pygame.draw.line(gameDisplay, (255,255,255), (x2,0), (x2,600))
        pygame.draw.line(gameDisplay, (255,255,255), (0,y2), (600,y2))
        pygame.display.update()

locx = 0
locy = 0
turn = 0
used = {1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
winner = "O"
done = False
won = False

downwards = [1,4,7]
sideways = [1,2,3]



#CHECK WIN FUNCTION

def checkWin():
    global used
    global winner

    #INSTEAD OF LISTING EVERY POSSIBLE WIN COMBINATION, 2 FOR LOOPS ARE USED TO CHECK ALL THE COMBINATIONS

    for i in sideways:
        if used[i] == used[i + 3]:
            if used[i] == used[i + 6]:
                if used[i] == "o":
                    pygame.draw.line(gameDisplay, (255,0,0), (((i * 200) - 100),50), (((i * 200) - 100),550), (10))
                    win()
                if used[i] == "x":
                    pygame.draw.line(gameDisplay, (255,0,0), (((i * 200) - 100),50), (((i * 200) - 100),550), (10))
                    winner = "X"
                    win()
    for i in downwards:
        if used[i] == used[i + 1]:
            if used[i] == used[i + 2]:
                if used[i] == "o":
                    pygame.draw.line(gameDisplay, (255,0,0), (50,(((2 * i) + 1) * (100 / 3))), (550,(((2 * i) + 1) * (100 / 3))), (10))
                    win()
                if used[i] == "x":
                    pygame.draw.line(gameDisplay, (255,0,0), (50,(((2 * i) + 1) * (100 / 3))), (550,(((2 * i) + 1) * (100 / 3))), (10))
                    winner = "X"
                    win()
    if used[1] == used[5]:
        if used[1] == used[9]:
            if used[1] == "o": 
                pygame.draw.line(gameDisplay, (255,0,0), (50,50), (550,550), (10))
                win()
            if used[1] == "x":
                pygame.draw.line(gameDisplay, (255,0,0), (50,50), (550,550), (10))
                winner = "X"
                win()
    if used[3] == used[5]:
        if used[3] == used[7]:
            if used[3] == "o":
                pygame.draw.line(gameDisplay, (255,0,0), (550,50), (50,550), (10))
                win()
            if used[3] == "x":
                pygame.draw.line(gameDisplay, (255,0,0), (550,50), (50,550), (10))
                winner = "X"
                win()
    if used[1] != "-" and used[2] != "-" and used[3] != "-" and used[4] != "-" and used[5] != "-" and used[6] != "-" and used[7] != "-" and used[8] != "-" and used[9] != "-":
        if won == False:
            draw()



#GAME WON AND DRAWN FUNCTION

def win():
    global won
    won = True
    font = pygame.font.Font('freesansbold.ttf', 132) 
    text = font.render(winner + ' Wins!', True, (0, 0, 255)) 
    textRect = text.get_rect()
    textRect.center = (300, 300)
    gameDisplay.blit(text, textRect) 

def draw():
    global won
    won = True
    font = pygame.font.Font('freesansbold.ttf', 132) 
    text = font.render("Draw!", True, (0, 0, 255)) 
    textRect = text.get_rect()
    textRect.center = (300, 300)
    gameDisplay.blit(text, textRect) 



#SET UP GAME BOARD AND INITIALISE GAME

makeGame()
first = True

while end == False:

    clock.tick(60)

    xImg = pygame.image.load('x.png')
    oImg = pygame.image.load('o.png')
    print(done)
    print("     " + str(done))
    go = False
    aiTurn = False
    turnMade = False
    square = 0



    #TWO PLAYER MODE

    if mode == 1:
        if done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.font.quit()
                    quit()

                #CHECKS FOR MOUSE CLICK POSITION INSTEAD OF KEY PRESS

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx < 200:
                        if my < 200:
                            if used[1] == "-":
                                locx = 0
                                locy = 0
                                go = True
                                if turn == 0:
                                    used[1] = "x"
                                else:
                                    used[1] = "o"
                        elif my < 400:
                            if used[4] == "-":
                                locx = 0
                                locy = 2
                                go = True
                                if turn == 0:
                                    used[4] = "x"
                                else:
                                    used[4] = "o"
                        else:
                            if used[7] == "-":
                                locx = 0
                                locy = 4
                                go = True
                                if turn == 0:
                                    used[7] = "x"
                                else:
                                    used[7] = "o"
                    elif mx < 400:
                        if my < 200:
                            if used[2] == "-":
                                locx = 2
                                locy = 0
                                go = True
                                if turn == 0:
                                    used[2] = "x"
                                else:
                                    used[2] = "o"
                        elif my < 400:
                            if used[5] == "-":
                                locx = 2
                                locy = 2
                                go = True
                                if turn == 0:
                                    used[5] = "x"
                                else:
                                    used[5] = "o"
                        else:
                            if used[8] == "-":
                                locx = 2
                                locy = 4
                                go = True
                                if turn == 0:
                                    used[8] = "x"
                                else:
                                    used[8] = "o"
                    else:
                        if my < 200:
                            if used[3] == "-":
                                locx = 4
                                locy = 0
                                go = True
                                if turn == 0:
                                    used[3] = "x"
                                else:
                                    used[3] = "o"
                        elif my < 400:
                            if used[6] == "-":
                                locx = 4
                                locy = 2
                                go = True
                                if turn == 0:
                                    used[6] = "x"
                                else:
                                    used[6] = "o"
                        else:
                            if used[9] == "-":
                                locx = 4
                                locy = 4
                                go = True
                                if turn == 0:
                                    used[9] = "x"
                                else:
                                    used[9] = "o"

                    #BASED ON CLICK POSSITION, I ASSIGN 2 VARIABLES THAT DETERMIN THE VISUAL REPERASENTATION OF THE MOVE

                    if go == True:
                        if turn == 0:
                            turn = 1
                            gameDisplay.blit(xImg, ((locx * 100), (locy * 100)))
                        else:
                            turn = 0
                            gameDisplay.blit(oImg, ((locx * 100), (locy * 100)))
                print(used)
                print(event)
            
            if won == True:
                done = True
                end = True

            checkWin()


    #SINGLE PLAYER MODE

    
    else:
        if done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.font.quit()
                    quit()
                #CHECKS FOR MOUSE CLICK POSITION INSTEAD OF KEY PRESS
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx < 200:
                        if my < 200:
                            if used[1] == "-":
                                locx = 0
                                locy = 0
                                go = True
                                used[1] = "x"
                        elif my < 400:
                            if used[4] == "-":
                                locx = 0
                                locy = 2
                                go = True
                                used[4] = "x"
                        else:
                            if used[7] == "-":
                                locx = 0
                                locy = 4
                                go = True
                                used[7] = "x"
                    elif mx < 400:
                        if my < 200:
                            if used[2] == "-":
                                locx = 2
                                locy = 0
                                go = True
                                used[2] = "x"
                        elif my < 400:
                            if used[5] == "-":
                                locx = 2
                                locy = 2
                                go = True
                                used[5] = "x"
                        else:
                            if used[8] == "-":
                                locx = 2
                                locy = 4
                                go = True
                                used[8] = "x"
                    else:
                        if my < 200:
                            if used[3] == "-":
                                locx = 4
                                locy = 0
                                go = True
                                used[3] = "x"
                        elif my < 400:
                            if used[6] == "-":
                                locx = 4
                                locy = 2
                                go = True
                                used[6] = "x"
                        else:
                            if used[9] == "-":
                                locx = 4
                                locy = 4
                                go = True
                                used[9] = "x"

                    aiTurn = False

                    #BASED ON CLICK POSSITION, I ASSIGN 2 VARIABLES THAT DETERMIN THE VISUAL REPERASENTATION OF THE MOVE

                    if go == True:
                        aiTurn = True
                        gameDisplay.blit(xImg, ((locx * 100), (locy * 100)))
                    
            spotsX5 = [1, 2, 3, 4, 6, 7, 8, 9]
            spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            random.shuffle(spotsX5)
            random.shuffle(spots)

            checkWin()
            if won == False:
                if aiTurn == True:

                    #AI FIRST TURN WILL PLAY MIDDLE IF NOT TAKEN, THEN CORNER IF MIDDLE IS TAKEN
                    
                    if first == True:
                        turnMade = True
                        if used[5] == "-":
                            locx = 2
                            locy = 2
                            used[5] = "o"
                            gameDisplay.blit(oImg, ((locx * 100), (locy * 100))) 
                        elif used[3] == "-":
                            locx = 4
                            locy = 0
                            used[3] = "o"
                            gameDisplay.blit(oImg, ((locx * 100), (locy * 100))) 
                        first = False



                    #AI "EASY DIFFUCULTY" 

    
                    if gameMode == "easy":

                        #EASY AI USES RANDOM MOVES

                        for i in spotsX5:
                            if turnMade == False:
                                if used[i] == "-":
                                    turnMade = True
                                    if i == 1:
                                        locx = 0
                                        locy = 0
                                    if i == 2:
                                        locx = 2
                                        locy = 0
                                    if i == 3:
                                        locx = 4
                                        locy = 0
                                    if i == 4:
                                        locx = 0
                                        locy = 2
                                    if i == 6:
                                        locx = 4
                                        locy = 2
                                    if i == 7:
                                        locx = 0
                                        locy = 4
                                    if i == 8:
                                        locx = 2
                                        locy = 4
                                    if i == 9:
                                        locx = 4
                                        locy = 4    
                                    used[i] = "o"
                                    #BASED ON AI RANDOM POSITION, I ASSIGN 2 VARIABLES THAT DETERMIN THE VISUAL REPERASENTATION OF THE MOVE
                                    gameDisplay.blit(oImg, ((locx * 100), (locy * 100)))


                    #AI "HARD DIFFUCULTY" 
    
                    else:

                        #HARD AI USES FOR LOOPS TO INITIALLY DETECT WINS AND THEN
                        for i in downwards:
                            if used[i] == used[i + 1]:
                                if used[i + 2] == "-" and used[i] == "o" and turnMade == False:
                                    turnMade = True
                                    square = i + 2
                            if used[i] == used[i + 2]:
                                if used[i + 1] == "-" and used[i] == "o" and turnMade == False:
                                    turnMade = True
                                    square = i + 1
                            if used[i + 1] == used[i + 2]:
                                if used[i] == "-" and used[i + 1] == "o" and turnMade == False:
                                    turnMade = True
                                    square = i

                        for i in sideways:
                            if used[i] == used[i + 3]:
                                if used[i + 6] == "-" and used[i] == "o" and turnMade == False:
                                    turnMade = True
                                    square = i + 6
                            if used[i] == used[i + 6]:
                                if used[i + 3] == "-" and used[i] == "o" and turnMade == False:
                                    turnMade = True
                                    square = i + 3
                            if used[i + 3] == used[i + 6]:
                                if used[i] == "-" and used[i + 3] == "o" and turnMade == False:
                                    turnMade = True
                                    square = i
                        if used[1] == used[9]:
                            if used[1] == "o"and used[5] == "-" and turnMade == False:
                                turnMade = True
                                square = 5
                        if used[1] == used[5]:
                            if used[1] == "o" and used[9] == "-" and turnMade == False:
                                turnMade = True
                                square = 9
                        if used[9] == used[5]:
                            if used[9] == "o" and used[1] == "-" and turnMade == False:
                                turnMade = True
                                square = 1
                        if used[3] == used[7]:
                            if used[3] == "o" and used[5] == "-" and turnMade == False:
                                turnMade = True
                                square = 5
                        if used[3] == used[5]:
                            if used[3] == "o" and used[7] == "-" and turnMade == False:
                                turnMade = True
                                square = 7
                        if used[7] == used[5]:
                            if used[7] == "o" and used[3] == "-" and turnMade == False:
                                turnMade = True
                                square = 3

                        for i in downwards:
                            if used[i] == used[i + 1]:
                                if used[i + 2] == "-" and used[i] == "x" and turnMade == False:
                                    turnMade = True
                                    square = i + 2
                            if used[i] == used[i + 2]:
                                if used[i + 1] == "-" and used[i] == "x" and turnMade == False:
                                    turnMade = True
                                    square = i + 1
                            if used[i + 1] == used[i + 2]:
                                if used[i] == "-" and used[i + 1] == "x" and turnMade == False:
                                    turnMade = True
                                    square = i

                        for i in sideways:
                            if used[i] == used[i + 3]:
                                if used[i + 6] == "-" and used[i] == "x" and turnMade == False:
                                    turnMade = True
                                    square = i + 6
                            if used[i] == used[i + 6]:
                                if used[i + 3] == "-" and used[i] == "x" and turnMade == False:
                                    turnMade = True
                                    square = i + 3
                            if used[i + 3] == used[i + 6]:
                                if used[i] == "-" and used[i + 3] == "x" and turnMade == False:
                                    turnMade = True
                                    square = i
                        if used[1] == used[9]:
                            if used[1] == "x" and used[5] == "-" and turnMade == False:
                                turnMade = True
                                square = 5
                        if used[1] == used[5]:
                            if used[1] == "x" and used[9] == "-" and turnMade == False:
                                turnMade = True
                                square = 9
                        if used[9] == used[5]:
                            if used[9] == "x" and used[1] == "-" and turnMade == False:
                                turnMade = True
                                square = 1
                        if used[3] == used[7]:
                            if used[3] == "x" and used[5] == "-" and turnMade == False:
                                turnMade = True
                                square = 5
                        if used[3] == used[5]:
                            if used[3] == "x" and used[7] == "-" and turnMade == False:
                                turnMade = True
                                square = 7
                        if used[7] == used[5]:
                            if used[7] == "x" and used[3] == "-" and turnMade == False:
                                turnMade = True
                                square = 3
                                
                        if turnMade == True:
                            if square == 1:
                                locx = 0
                                locy = 0
                            if square == 2:
                                locx = 2
                                locy = 0
                            if square == 3:
                                locx = 4
                                locy = 0
                            if square == 4:
                                locx = 0
                                locy = 2
                            if square == 5:
                                locx = 2
                                locy = 2
                            if square == 6:
                                locx = 4
                                locy = 2
                            if square == 7:
                                locx = 0
                                locy = 4
                            if square == 8:
                                locx = 2
                                locy = 4
                            if square == 9:
                                locx = 4
                                locy = 4   
                            used[square] = "o"
                        if turnMade == False:
                            for i in spots:
                                if turnMade == False:
                                    if used[i] == "-":
                                        #BASED ON AI RANDOM POSITION, I ASSIGN 2 VARIABLES THAT DETERMIN THE VISUAL REPERASENTATION OF THE MOVE
                                        turnMade = True
                                        if i == 1:
                                            locx = 0
                                            locy = 0
                                        if i == 2:
                                            locx = 2
                                            locy = 0
                                        if i == 3:
                                            locx = 4
                                            locy = 0
                                        if i == 4:
                                            locx = 0
                                            locy = 2
                                        if i == 5:
                                            locx = 2
                                            locy = 2
                                        if i == 6:
                                            locx = 4
                                            locy = 2
                                        if i == 7:
                                            locx = 0
                                            locy = 4
                                        if i == 8:
                                            locx = 2
                                            locy = 4
                                        if i == 9:
                                            locx = 4
                                            locy = 4    
                                        used[i] = "o"
                        gameDisplay.blit(oImg, ((locx * 100), (locy * 100)))

                print(used)
                print(event)
            
            if won == True:
                done = True
                end = True
    
    pygame.display.update()




# GAME ENED

print("Awaiting End")

while end == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False

pygame.quit()
pygame.font.quit()
quit()