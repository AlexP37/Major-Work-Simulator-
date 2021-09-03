import pygame
import math
import random

pygame.init()
pygame.font.init()

display_width = 600
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

def textBox(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

def textBoxWhiteBackground(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (255,255,255)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

flash = True

def flashModeChoice():
    global flash
    if flash == False:
        flash = True
    else:
        flash = False
    print(flash)
    pygame.draw.rect(gameDisplay, (255,255,255), (0, 15, 600, 60))
    textBoxWhiteBackground('The Flash Mode', 25, (300, 25), (0,0,0))
    savOn = pygame.image.load('savOn.png')
    savOff = pygame.image.load('savOff.png')
    if flash == False:
        gameDisplay.blit(savOff, (270, 40))
    else:
        gameDisplay.blit(savOn, (270, 40))

mode = 0
gameDisplay.fill((255,255,255))
pygame.draw.line(gameDisplay, (0,0,0), (300,0), (300,600))

textBoxWhiteBackground('2 Player', 50, (150, 300), (0,0,0))
textBoxWhiteBackground('1 Player', 50, (450, 300), (0,0,0))
flashModeChoice()

cont = False
gameMode = 2

while cont == False:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.font.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
                pygame.quit()
                pygame.font.quit()
                quit()
        #CHECKS FOR MOUSE CLICK POSITION INSTEAD OF KEY PRESS
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 30 < my < 80:
                    if 270 < mx < 330:
                        if 40 < my < 70:
                            flashModeChoice()
                    elif mx > 340:
                        mode = 1
                        cont = True
                    elif mx < 260:
                        mode = 2
                        cont = True
            elif mx < 300:
                mode = 2
                cont = True
            else:
                mode = 1
                cont = True

    pygame.display.update()

gameDisplay.fill((255,255,255))
pygame.draw.line(gameDisplay, (0,0,0), (0,200), (600,200))
pygame.draw.line(gameDisplay, (0,0,0), (0,400), (600,400))

textBoxWhiteBackground('Easy', 50, (300, 100), (0,0,0))
textBoxWhiteBackground('Intermediate', 50, (300, 300), (0,0,0))
textBoxWhiteBackground('Hard', 50, (300, 500), (0,0,0))

cont = False
dif = 0
difSpeed = 4
if mode == 1:
    while cont == False:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
            #CHECKS FOR MOUSE CLICK POSITION INSTEAD OF KEY PRESS
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if my < 200:
                    dif = 0
                    difSpeed = 2
                elif my < 400:
                    dif = 1
                    difSpeed = 4
                else:
                    dif = 2
                    difSpeed = 6
                cont = True
        print(dif)
        pygame.display.update()

yLoc = 0
def centLine():
    global yLoc
    yLoc = 0
    while yLoc < 600:
        pygame.draw.rect(gameDisplay, (255,255,255), (297, yLoc, 6, 15))
        yLoc = yLoc + 30
    pygame.display.update()

def makeGame():
    print("Game Initialised")
    gameDisplay.fill((0,0,0))
    pygame.display.update()

makeGame()
end = False
y = 225
x =  0
mov = 0
movd = 0
movB = 0
movBd = 0
brickLen = 150
centLine()
recent = "up"
recentB = "up"
bx = 400
by = 100
cx = -4
cy = -4
speed = 4
score1 = 0
score2 = 0
oy = 225
ballSize = 8

if flash == True:
    speed = 10
    difSpeed = 10

while end == False:
    clock.tick(60)
    if mode == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
                if event.key == pygame.K_UP:
                    mov = 1
                    recent = "up"
                if event.key == pygame.K_DOWN:
                    movd = 2
                    recent = "down"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mov = 0
                if event.key == pygame.K_DOWN:
                    movd = 0
        if recent == "up":
            if mov == 1:
                if y > 0:
                    y = y - difSpeed
            elif movd == 2:
                if y < 600 - brickLen:
                    y = y + difSpeed
        else:
            if movd == 2:
                if y < 600 - brickLen:
                    y = y + difSpeed
            elif mov == 1:
                if y > 0:
                    y = y - difSpeed
        if by < 0:
            cy = (cy * -1)
        if by > 600:
            cy = (cy * -1)
        if bx <= 15:
            speed = speed + 0.4
            print("")
            print(y)
            print(by)
            if (y - ballSize) <= by <= (y + brickLen + ballSize):
                if -8 <= (by - y) <= 15:
                    cy = -8
                    if flash == True:
                        cy = -14
                elif 15 <= (by - y) <= 30:
                    cy = -4
                    if flash == True:
                        cy = -12
                elif 30 <= (by - y) <= 45:
                    cy = -2
                elif 45 <= (by - y) <= 60:
                    cy = -1
                elif 60 <= (by - y) <= 75:
                    cy = -0.5
                elif 75 <= (by - y) <= 90:
                    cy = 0.5
                elif 90 <= (by - y) <= 105:
                    cy = 1
                elif 105 <= (by - y) <= 125:
                    cy = 2
                elif 125 <= (by - y) <= 140:
                    cy = 4
                    if flash == True:
                        cy = 10
                elif 140 <= (by - y) <= 158:
                    cy = 8
                    if flash == True:
                        cy = 14
                cx = speed
            else:
                print("OUT")
                score2 = score2 + 1
                bx = 400
                by = 100
                cx = -4
                cy = -4
                speed = 4
                if flash == True:
                    speed = 10
                y = 225
                oy = 225
        elif bx >= 585:
            speed = speed + 0.4
            print("")
            print(oy)
            print(by)
            if (oy - ballSize) <= by <= (oy + brickLen):
                if (0 - ballSize) <= (by - oy) <= 15:
                    cy = -8
                    if flash == True:
                        cy = -14
                elif 15 <= (by - oy) <= 30:
                    cy = -4
                    if flash == True:
                        cy = -12
                elif 30 <= (by - oy) <= 45:
                    cy = -2
                elif 45 <= (by - oy) <= 60:
                    cy = -1
                elif 60 <= (by - oy) <= 75:
                    cy = -0.5
                elif 75 <= (by - oy) <= 90:
                    cy = 0.5
                elif 90 <= (by - oy) <= 105:
                    cy = 1
                elif 105 <= (by - oy) <= 125:
                    cy = 2
                elif 125 <= (by - oy) <= 140:
                    cy = 4
                    if flash == True:
                        cy = 10
                elif 140 <= (by - oy) <= 150:
                    cy = 8
                    if flash == True:
                        cy = 14
                cx = (-1 * speed)
            else:
                print("OUT")
                score1 = score1 + 1
                bx = 400
                by = 100
                cx = -4
                cy = -4
                speed = 4
                if flash == True:
                    speed = 10
                y = 225
                oy = 225
        if cx > 20:
            cx = 20

        bx = bx + cx
        by = by + cy
        if dif == 0:
            ##print("Easy")
            if (oy + 50) <= by <= (oy + 100):
                oy = oy
            elif by > (oy + 75):
                if (oy + brickLen) <= 600:
                    oy = oy + difSpeed
            elif by < (oy + 75):
                if oy >= 0:
                    oy = oy - difSpeed
        elif dif == 1:
            ##print("Intermediate")
            if oy <= by <= (oy + 10):
                oy = oy
            elif by < oy:
                if oy > 0:
                    oy = oy - difSpeed
            else:
                if (oy + brickLen) < 600:
                    oy = oy + difSpeed
        else:
            ##print("Hard")
            if (-1.1) <= cy <= (1.1):
                if (oy) <= by <= (oy + brickLen):
                    if oy <= by <= (oy + 12):
                        oy = oy
                    if (oy + brickLen - 12) <= by <= (oy + brickLen):
                        oy = oy
                    if (oy + brickLen - 12) >= by >= (oy + (brickLen / 2)):
                        oy = oy - difSpeed
                    if (oy + 12) <= by <= (oy + (brickLen / 2)):
                        oy = oy + difSpeed
                elif by > (oy + 75):
                    if (oy + brickLen) <= 600:
                        oy = oy + difSpeed
                elif by < (oy + 75):
                    if oy >= 0:
                        oy = oy - difSpeed
                if oy < 0:
                    oy = oy + difSpeed
                if oy > 600:
                    oy = oy - difSpeed
            elif (-2.1) <= cy <= (2.1):
                if (oy) <= by <= (oy + brickLen):
                    if oy <= by <= (oy + 25):
                        oy = oy
                    if (oy + brickLen - 25) <= by <= (oy + brickLen):
                        oy = oy
                    if (oy + brickLen - 25) >= by >= (oy + (brickLen / 2)):
                        oy = oy - difSpeed
                    if (oy + 25) <= by <= (oy + (brickLen / 2)):
                        oy = oy + difSpeed
                elif by > (oy + 75):
                    if (oy + brickLen) <= 600:
                        oy = oy + difSpeed
                elif by < (oy + 75):
                    if oy >= 0:
                        oy = oy - difSpeed
            else:
                if (oy + 50) <= by <= (oy + 100):
                    oy = oy
                elif by > (oy + 75):
                    if (oy + brickLen) <= 600:
                        oy = oy + difSpeed
                elif by < (oy + 75):
                    if oy >= 0:
                        oy = oy - difSpeed
    if mode == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
                if event.key == pygame.K_UP:
                    mov = 1
                    recent = "up"
                if event.key == pygame.K_DOWN:
                    movd = 2
                    recent = "down"
                if event.key == pygame.K_w:
                    movB = 1
                    recentB = "up"
                if event.key == pygame.K_s:
                    movBd = 2
                    recentB = "down"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mov = 0
                if event.key == pygame.K_DOWN:
                    movd = 0
                if event.key == pygame.K_w:
                    movB = 0
                if event.key == pygame.K_s:
                    movBd = 0
                    
        if recentB == "up":
            if movB == 1:
                if y > 0:
                    y = y - difSpeed
            elif movBd == 2:
                if y < 600 - brickLen:
                    y = y + difSpeed
        else:
            if movBd == 2:
                if y < 600 - brickLen:
                    y = y + difSpeed
            elif movB == 1:
                if y > 0:
                    y = y - difSpeed

        if recent == "up":
            if mov == 1:
                if oy > 0:
                    oy = oy - difSpeed
            elif movd == 2:
                if oy < 600 - brickLen:
                    oy = oy + difSpeed
        else:
            if movd == 2:
                if oy < 600 - brickLen:
                    oy = oy + difSpeed
            elif mov == 1:
                if oy > 0:
                    oy = oy - difSpeed
        if by < 0:
            cy = (cy * -1)
        if by > 600:
            cy = (cy * -1)
        if bx <= 15:
            speed = speed + 0.4
            print("")
            print(y)
            print(by)
            if (y - ballSize) <= by <= (y + brickLen + ballSize):
                if -8 <= (by - y) <= 15:
                    cy = -8
                    if flash == True:
                        cy = -14
                elif 15 <= (by - y) <= 30:
                    cy = -4
                    if flash == True:
                        cy = -12
                elif 30 <= (by - y) <= 45:
                    cy = -2
                elif 45 <= (by - y) <= 60:
                    cy = -1
                elif 60 <= (by - y) <= 75:
                    cy = -0.5
                elif 75 <= (by - y) <= 90:
                    cy = 0.5
                elif 90 <= (by - y) <= 105:
                    cy = 1
                elif 105 <= (by - y) <= 125:
                    cy = 2
                elif 125 <= (by - y) <= 140:
                    cy = 4
                    if flash == True:
                        cy = 10
                elif 140 <= (by - y) <= 158:
                    cy = 8
                    if flash == True:
                        cy = 14
                cx = speed
            else:
                print("OUT")
                score2 = score2 + 1
                bx = 400
                by = 100
                cx = -4
                cy = -4
                speed = 4
                if flash == True:
                    speed = 10
                y = 225
                oy = 225
        elif bx >= 585:
            speed = speed + 0.4
            print("")
            print(oy)
            print(by)
            if (oy - ballSize) <= by <= (oy + brickLen):
                if (0 - ballSize) <= (by - oy) <= 15:
                    cy = -8
                    if flash == True:
                        cy = -14
                elif 15 <= (by - oy) <= 30:
                    cy = -4
                    if flash == True:
                        cy = -12
                elif 30 <= (by - oy) <= 45:
                    cy = -2
                elif 45 <= (by - oy) <= 60:
                    cy = -1
                elif 60 <= (by - oy) <= 75:
                    cy = -0.5
                elif 75 <= (by - oy) <= 90:
                    cy = 0.5
                elif 90 <= (by - oy) <= 105:
                    cy = 1
                elif 105 <= (by - oy) <= 125:
                    cy = 2
                elif 125 <= (by - oy) <= 140:
                    cy = 4
                    if flash == True:
                        cy = 10
                elif 140 <= (by - oy) <= 150:
                    cy = 8
                    if flash == True:
                        cy = 14
                cx = (-1 * speed)
            else:
                print("OUT")
                score1 = score1 + 1
                bx = 400
                by = 100
                cx = -4
                cy = -4
                speed = 4
                if flash == True:
                    speed = 10
                y = 225
                oy = 225
        if cx > 20:
            cx = 20

        bx = bx + cx
        by = by + cy

    if (oy + brickLen) > 600:
        oy = (600 - brickLen)
    if oy < 0:
        oy = 0

    gameDisplay.fill((0,0,0))
    centLine()
    pygame.draw.rect(gameDisplay, (255,255,255), (585, oy, 15, brickLen))
    pygame.draw.rect(gameDisplay, (255,255,255), (x, y, 15, brickLen))
    textBox(str(score1), 50, (250,50), (255,255,255))
    textBox(str(score2), 50, (350,50), (255,255,255))
    pygame.draw.rect(gameDisplay, (255,255,255), (bx, by, ballSize, ballSize))
    pygame.display.update()

    if score1 == 11:
        end = True
        textBox("Player 1 Wins", 75, (300,300), (0,0,255))
    if score2 == 11:
        end = True
        textBox("Player 2 Wins", 75, (300,300), (0,0,255))

pygame.display.update()

while end == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    end = False

print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()
