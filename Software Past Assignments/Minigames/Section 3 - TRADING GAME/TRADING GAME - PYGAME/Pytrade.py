#Initialization
import os
import pygame
import math
import random
pygame.init()
pygame.font.init()
display_width = 1000
display_height = 700
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Trading Game')
clock = pygame.time.Clock()
gameDisplay.fill((255,255,255))
img = pygame.image.load('intro.jpeg')
gameDisplay.blit(img, (0,0))

#Functions
def textBoxBlack(text, size, position, color):
    font = pygame.font.Font('air_mitalic.ttf', size)
    text = font.render(text, True, color, (0,0,0))
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect)

def textBoxGreen(text, size, position, color):
    font = pygame.font.Font('air_mitalic.ttf', size)
    text = font.render(text, True, color, (0,175,0))
    textRect = text.get_rect()
    textRect.midleft = position
    gameDisplay.blit(text, textRect)

def textBoxRed(text, size, position, color):
    font = pygame.font.Font('air_mitalic.ttf', size)
    text = font.render(text, True, color, (175,0,0))
    textRect = text.get_rect()
    textRect.midleft = position
    gameDisplay.blit(text, textRect)

def textBoxClear(text, size, position, color):
    font = pygame.font.Font('air_mitalic.ttf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect)

def textBoxClear2(text, size, position, color):
    font = pygame.font.Font('Serpentine-BoldOblique.otf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect)

def textBoxClear22(text, size, position, color):
    font = pygame.font.Font('Serpentine-BoldOblique.otf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.midleft = position
    gameDisplay.blit(text, textRect)

def textBoxClearL(text, size, position, color):
    font = pygame.font.Font('air_mitalic.ttf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.midleft = position
    gameDisplay.blit(text, textRect)

def textBoxClearL2(text, size, position, color):
    font = pygame.font.Font('Serpentine-BoldOblique.otf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.midleft = position
    gameDisplay.blit(text, textRect)

def textBoxClearR(text, size, position, color):
    font = pygame.font.Font('air_mitalic.ttf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.midright = position
    gameDisplay.blit(text, textRect)

def makeGame():
    print("Game Initialised")
    gameDisplay.fill((0,0,0))
    pygame.display.update()

#Opening Menu
cont = False
go = False
a = 0.0
b = 0
c = 0
spaceStone = False
realityStone = False
timeStone = False
soulStone = False
mindStone = False
powerStone = False
while cont == False:
    clock.tick(60)
    img = pygame.image.load('intro.jpeg')
    gameDisplay.blit(img, (0,0))
    textBoxClear("Fandom Trade", (100 + b), (500,75), (255, 232, 31))
    textBoxClear("Marvel Cinamatic Universe", int(30 + a), (500,140), (255, 232, 31))
    textBoxClear("Marvel Comics", int(30 + a), (500, 170), (255, 232, 31))
    textBoxClear("DC Comics", int(30 + a), (500,200), (255, 232, 31))
    textBoxClear("Arrowverse", int(30 + a), (500,230), (255, 232, 31))
    textBoxClear("Star Trek", int(30 + a), (500,260), (255, 232, 31))
    textBoxClear("Star Wars", int(30 + a), (500,290), (255, 232, 31))
    textBoxClear("Shurverse", int(30 + a), (500,320), (255, 232, 31))
    textBoxClear("and More!", int(30 + a), (500,350), (255, 232, 31))
    textBoxClear("Start", (250 + c), (500,540), (255,255,255))
    if go == True:
        a = a - 1.2
        if a < -30:
            a = -30
        b = b - 4
        c = c - 10
        print(c)
    if c == -290:
        cont = True
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 120 < mx < 785:
                if 450 < my < 630:
                    go = True
    pygame.display.update()

cont = False
go = False
newGame = False
c = 0
while cont == False:
    clock.tick(60)
    img = pygame.image.load('intro.jpeg')
    gameDisplay.blit(img, (0,0))
    txtSize = 200
    if go == True:
        c = c - 10
        print(c)
    if (txtSize - c) > 2:
        textBoxClear("New Game", (txtSize + c), (500,175), (255,255,255))
        textBoxClear("Load Game", (txtSize + c), (500,525), (255,255,255))
    if c == ((txtSize * -1) - 20):
        cont = True
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 40 < mx < 975:
                if 100 < my < 250:
                    go = True
                    newGame = True
                if 450 < my < 600:
                    go = True
    pygame.display.update()

#Begins Game
earth = 888
makeGame()
def mainMenu():
    end = False
    exp = False
    adj = 0
    global earth
    e47x = 0
    e47y = 0
    e366x = 0
    e366y = 0
    e48x = 0
    e48y = 0
    e1x = 0
    e1y = 0
    e12x = 0
    e12y = 0
    e1725x = 0
    e1725y = 0
    e0x = 0
    e0y = 0
    global e2187x
    global e2187y
    e616x = 0
    e616y = 0
    e2187x = 0
    e2187y = 0
    # e0i = pygame.image.load('Earth-0.png')
    # e0i = pygame.transform.scale(e0i, (250, 250))
    # gameDisplay.blit(e0i, (300 + e0x ,300 + e0y))
    # e616i = pygame.image.load('Earth-616.png')
    # e616i = pygame.transform.scale(e616i, (300, 300))
    # gameDisplay.blit(e616i, (30 + e616x,30 + e616y))
    # e1i = pygame.image.load('Earth-1.png')
    # e1i = pygame.transform.scale(e1i, (200, 200))
    # gameDisplay.blit(e1i, (400 + e1x,50 + e1y))
    # e47i = pygame.image.load('Earth-47.png')
    # e47i = pygame.transform.scale(e47i, (225, 225))
    # gameDisplay.blit(e47i, (720 + e47x,80 + e47y))
    # e12i = pygame.image.load('Earth-12.png')
    # e12i = pygame.transform.scale(e12i, (150, 150))
    # gameDisplay.blit(e12i, (600 + e12x,400 + e12y))
    # e1725i = pygame.image.load('Earth-1725.png')
    # e1725i = pygame.transform.scale(e1725i, (160, 160))
    # gameDisplay.blit(e1725i, (800 + e1725x,400 + e1725y))
    # e48i = pygame.image.load('Earth-48.png')
    # e48i = pygame.transform.scale(e48i, (140, 140))
    # gameDisplay.blit(e48i, (560 + e48x,220 + e48y))
    # e2187i = pygame.image.load('Earth-2187.png')
    # e2187i = pygame.transform.scale(e2187i, (150, 150))
    # gameDisplay.blit(e2187i, (100 + e2187x,400 + e2187y))
    while end == False:
        translationMove = [-1,0,1]
        random.shuffle(translationMove)
        translationMove2 = [-1,0,1]
        random.shuffle(translationMove2)
        img = pygame.image.load('intro.jpeg')
        gameDisplay.blit(img, (0,0))
        # img = pygame.image.load('Infinity Stones.png')
        # gameDisplay.blit(img, (680,620))
        print(e2187x)
        e366i = pygame.image.load('Earth-366.png')
        gameDisplay.blit(e366i, (840 + e366x ,560 + e366y))
        e0i = pygame.image.load('Earth-0.png')
        gameDisplay.blit(e0i, (300 + e0x ,300 + e0y))
        e616i = pygame.image.load('Earth-616.png')
        gameDisplay.blit(e616i, (30 + e616x,30 + e616y))
        e1i = pygame.image.load('Earth-1.png')
        gameDisplay.blit(e1i, (400 + e1x,50 + e1y))
        e47i = pygame.image.load('Earth-47.png')
        gameDisplay.blit(e47i, (720 + e47x,80 + e47y))
        e12i = pygame.image.load('Earth-12.png')
        gameDisplay.blit(e12i, (600 + e12x,400 + e12y))
        e1725i = pygame.image.load('Earth-1725.png')
        gameDisplay.blit(e1725i, (800 + e1725x,400 + e1725y))
        e48i = pygame.image.load('Earth-48.png')
        gameDisplay.blit(e48i, (560 + e48x,220 + e48y))
        e2187i = pygame.image.load('Earth-2187.png')
        gameDisplay.blit(e2187i, (100 + e2187x,400 + e2187y))
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        # EARTH 366 - Banking
        if 840 < mx < 990 and 560 < my < 690:
            textBoxClearL("Bank", 100, (10,640), (255,255,255))
            if -5 <= e366x <= 5:
                e366x = e366x - translationMove[1]
            if e366x > 5:
                e366x = e366x - 1
            if e366x < -5:
                e366x = e366x + 1
            if -5 <= e366y <= 5:
                e366y = e366y - translationMove2[1]
            if e366y > 5:
                e366y = e366y - 1
            if e366y < -5:
                e366y = e366y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 366
        # EARTH 48 - Parks and Recreation
        if 560 < mx < 700 and 220 < my < 360:
            textBoxClearL("Earth-48", 100, (10,640), (255,255,255))
            if -5 <= e48x <= 5:
                e48x = e48x - translationMove[1]
            if e48x > 5:
                e48x = e48x - 1
            if e48x < -5:
                e48x = e48x + 1
            if -5 <= e48y <= 5:
                e48y = e48y - translationMove2[1]
            if e48y > 5:
                e48y = e48y - 1
            if e48y < -5:
                e48y = e48y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 48
        # EARTH 47 - Star Trek
        elif 720 < mx < 945 and 80 < my < 305:
            textBoxClearL("Earth-47", 100, (10,640), (255,255,255))
            if -10 <= e47x <= 10:
                e47x = e47x - translationMove[1]
            if e47x > 10:
                e47x = e47x - 1
            if e47x < -10:
                e47x = e47x + 1
            if -10 <= e47y <= 10:
                e47y = e47y - translationMove2[1]
            if e47y > 10:
                e47y = e47y - 1
            if e47y < -10:
                e47y = e47y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 47
        # EARTH 1 - DC
        elif 400 < mx < 600 and 50 < my < 250:
            textBoxClearL("Earth-1", 100, (10,640), (255,255,255))
            if -5 <= e1x <= 5:
                e1x = e1x - translationMove[1]
            if e1x > 5:
                e1x = e1x - 1
            if e1x < -5:
                e1x = e1x + 1
            if -5 <= e1y <= 5:
                e1y = e1y - translationMove2[1]
            if e1y > 5:
                e1y = e1y - 1
            if e1y < -5:
                e1y = e1y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 1
        # EARTH 12 - MCU
        elif 600 < mx < 750 and 400 < my < 550:
            textBoxClearL("Earth-12", 100, (10,640), (255,255,255))
            if -5 <= e12x <= 5:
                e12x = e12x - translationMove[1]
            if e12x > 5:
                e12x = e12x - 1
            if e12x < -5:
                e12x = e12x + 1
            if -5 <= e12y <= 5:
                e12y = e12y - translationMove2[1]
            if e12y > 5:
                e12y = e12y - 1
            if e12y < -5:
                e12y = e12y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 12
        # EARTH 1725 - The Office
        elif 800 < mx < 960 and 400 < my < 560:
            textBoxClearL("Earth-1725", 100, (10,640), (255,255,255))
            if -5 <= e1725x <= 5:
                e1725x = e1725x - translationMove[1]
            if e1725x > 5:
                e1725x = e1725x - 1
            if e1725x < -5:
                e1725x = e1725x + 1
            if -5 <= e1725y <= 5:
                e1725y = e1725y - translationMove2[1]
            if e1725y > 5:
                e1725y = e1725y - 1
            if e1725y < -5:
                e1725y = e1725y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 1725
        # (EARTH) ALDERAAN 2187 - Star Wars
        elif 100 < mx < 250 and 400 < my < 550:
            textBoxClearL("Alderann-2187", 100, (10,640), (255,255,255))
            if -5 <= e2187x <= 5:
                e2187x = e2187x - translationMove[1]
            if e2187x > 5:
                e2187x = e2187x - 1
            if e2187x < -5:
                e2187x = e2187x + 1
            if -5 <= e2187y <= 5:
                e2187y = e2187y - translationMove2[1]
            if e2187y > 5:
                e2187y = e2187y - 1
            if e2187y < -5:
                e2187y = e2187y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 2187
        # EARTH Prime (0)- Arrowverse
        elif 300 < mx < 550 and 300 < my < 550:
            textBoxClearL("Earth-Prime", 100, (10,640), (255,255,255))
            if -5 <= e0x <= 5:
                e0x = e0x - translationMove[1]
            if e0x > 5:
                e0x = e0x - 1
            if e0x < -5:
                e0x = e0x + 1
            if -5 <= e0y <= 5:
                e0y = e0y - translationMove2[1]
            if e0y > 5:
                e0y = e0y - 1
            if e0y < -5:
                e0y = e0y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 0
        # EARTH 616 - Marvel
        elif 30 < mx < 330 and 30 < my < 330:
            textBoxClearL("Earth-616", 100, (10,640), (255,255,255))
            if -5 <= e616x <= 5:
                e616x = e616x - translationMove[1]
            if e616x > 5:
                e616x = e616x - 1
            if e616x < -5:
                e616x = e616x + 1
            if -5 <= e616y <= 5:
                e616y = e616y - translationMove2[1]
            if e616y > 5:
                e616y = e616y - 1
            if e616y < -5:
                e616y = e616y + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exp = True
                    earth = 616
        if exp == True:
            end = True
        
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
                    print("PLACEHOLDER")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print("PLACEHOLDER")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 400 < mx < 600:
                    if 50 < my < 250:
                        end = True
                        print(end)
        print(earth)
        pygame.display.update()

def bank():
    end = False
    global earth
    global credit
    global debt
    eligible = True
    clickSss = 0

    while end == False:
        clock.tick(60)
        img = pygame.image.load('layoutBank.png')
        gameDisplay.blit(img, (0,0))
        textBoxClearL2(("CREDITS: $" + str(credit)), 50, (50,55), (255,255,255))
        textBoxClearL2(("DEBT: $" + str(debt)), 70, (50,125), (255,255,255))

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 835 < mx < 950:
                    if 6 < my < 35:
                        end = True
                        earth = 888

                if debt < 1000000000.00:
                    if 245 < my < 305:
                        if 90 < mx < 340:
                            if ((credit - debt)/4) >= 10.00 and ((credit - debt)/4) > (debt + 10.00):
                                credit = credit + 10.00
                                debt = debt + 10.00
                                eligible = True
                            else:
                                eligible = False
                        if 375 < mx < 625:
                            if ((credit - debt)/4) >= 20.00 and ((credit - debt)/4) > (debt + 20.00):
                                credit = credit + 20.00
                                debt = debt + 20.00
                                eligible = True
                            else:
                                eligible = False
                        if 660 < mx < 910:
                            if ((credit - debt)/4) >= 50.00 and ((credit - debt)/4) > (debt + 50.00):
                                credit = credit + 50.00
                                debt = debt + 50.00
                                eligible = True
                            else:
                                eligible = False

                    if 322 < my < 382:
                        if 90 < mx < 340:
                            if ((credit - debt)/4) >= 100.00 and ((credit - debt)/4) > (debt + 100.00):
                                credit = credit + 100.00
                                debt = debt + 100.00
                                eligible = True
                            else:
                                eligible = False
                        if 375 < mx < 625:
                            if ((credit - debt)/4) >= 500.00 and ((credit - debt)/4) > (debt + 500.00):
                                credit = credit + 500.00
                                debt = debt + 500.00
                                eligible = True
                            else:
                                eligible = False
                        if 660 < mx < 910:
                            if ((credit - debt)/4) >= 5000.00 and ((credit - debt)/4) > (debt + 5000.00):
                                credit = credit + 5000.00
                                debt = debt + 5000.00
                                eligible = True
                            else:
                                eligible = False
                else:
                    eligible = False

                if 522 < my < 582:
                    if 90 < mx < 340:
                        if (debt - 10.00) >= 0.00:
                            if credit >= 10.00:
                                debt = debt - 10.00
                                credit = credit - 10.00
                    if 375 < mx < 625:
                        if credit - debt >= 0.00:
                            credit = credit - debt
                            debt = 0.00
                    if 660 < mx < 910:
                        if (debt - 50.00) >= 0.00:
                            if credit >= 50.00:
                                debt = debt - 50.00
                                credit = credit - 50.00

                if 593 < my < 635:
                    if 90 < mx < 340:
                        if (debt - 100.00) >= 0.00:
                            if credit >= 100.00:
                                debt = debt - 100.00
                                credit = credit - 100.00
                    if 375 < mx < 625:
                        if (debt - 500.00) >= 0.00:
                            if credit >= 500.00:
                                debt = debt - 500.00
                                credit = credit - 500.00
                    if 660 < mx < 910:
                        if (debt - 5000.00) >= 0.00:
                            if credit >= 5000.00:
                                debt = debt - 5000.00
                                credit = credit - 5000.00

        if eligible == False:
            clickSss = clickSss + 1
            textBoxClearL2(("INELIGIBLE FOR LOAN"), 30, (50,18), (176,0,0))
            if clickSss >= 50:
                clickSss = 0
                eligible = True
        
        fc = open("credits.txt", "w")
        fc.write(str(credit))
        fc.close()

        fd = open("debt.txt", "w")
        fd.write(str(debt))
        fd.close()

        pygame.display.update()

global credit
global debt

if newGame == True:
    fc = open("credits.txt", "w")
    fc.write(str(500.00))
    fc.close()

    fd = open("debt.txt", "w")
    fd.write(str(0.00))
    fd.close()

    fa = open("amount.txt", "w")
    fa.write("1|0|0|0|0|0|0|\n0|0|0|0|0|0|0|\n1725|0|0|0|0|0|0|\n48|0|0|0|0|0|0|\n12|0|0|0|0|0|0|\n2187|0|0|0|0|0|0|\n616|0|0|0|0|0|0|\n47|0|0|0|0|0|0|")
    fa.close()

    fp = open("prices.txt", "w")
    fp.write("0|21.89|56.44|54.22|77.11|34.33|33.29|\n1|67.01|5.21|46.67|21.22|19.78|12.01|\n12|89.22|36.78|43.11|66.56|6.31|12.55|\n47|2.32|88.72|88.23|22.32|66.54|92.72|\n48|2.34|4.34|12.31|3.31|2.92|45.23|\n616|77.23|12.21|89.23|54.32|22.12|23.34|\n1725|23.12|4.32|45.44|22.12|13.55|2.11|\n2187|33.23|22.43|10.12|33.33|91.11|78.12|")
    fp.close()

fc = open("credits.txt", "r")
credit = float(fc.read())
fc.close()

fd = open("debt.txt", "r")
debt = float(fd.read())
fd.close()

def earthZone(product1, product2, product3, product4, product5, product6):
    end = False
    global earth
    global spaceStone
    global realityStone
    global timeStone
    global soulStone
    global mindStone
    global powerStone
    global credit
    print('IT IS HERE!!')
    priceList = []
    amountList = []
    newPriceList = []
    spaceStoneUse = False
    timeStoneUse = True
    mindStoneUse = True
    soulStoneUse = True
    realityStoneUse = True
    powerStoneUse = True
    printNews = False
    txtNews = ''
    newsclicks = 0
    clicks = 0
    tsclicks = 0
    psclicks = 0
    rsclicks = 0
    ssclicks = 0
    soulsclicks = 0
    msclicks = 0
    pauseGo = 0
    pausePrices = False
    lowerPrices5 = False
    raisePrices5 = False
    oneFreeAll = False
    randomisePrices = False
    while end == False:
        clock.tick(60)
        newPriceList = []
        newAmountList = []

        f = open("prices.txt")
        for l in f:
            line = l.split("|")
            if line[0] == str(earth):
                priceList = line
            else:
                newPriceList.append(l)
        f.close()

        fi = open("amount.txt")
        for l in fi:
            line = l.split("|")
            if line[0] == str(earth):
                amountList = line
            else:
                newAmountList.append(l)
        fi.close()

        img = pygame.image.load(str(earth) + 'layout.png')
        gameDisplay.blit(img, (0,0))

        if spaceStone == True:
            if spaceStoneUse == False:
                img = pygame.image.load('spaceStoneDim.png')
            else:
                img = pygame.image.load('spaceStoneGlow.png')
            gameDisplay.blit(img, ((1000-58),630))
        if mindStone == True:
            if mindStoneUse == False:
                img = pygame.image.load('mindStoneDim.png')
            else:
                img = pygame.image.load('mindStoneGlow.png')
            gameDisplay.blit(img, ((1000-114),630))
        if soulStone == True:
            if soulStoneUse == False:
                img = pygame.image.load('soulStoneDim.png')
            else:
                img = pygame.image.load('soulStoneGlow.png')
            gameDisplay.blit(img, ((1000-157),630))
        if powerStone == True:
            if powerStoneUse == False:
                img = pygame.image.load('powerStoneDim.png')
            else:
                img = pygame.image.load('powerStoneGlow.png')
            gameDisplay.blit(img, ((1000-205),630))
        if timeStone == True:
            if timeStoneUse == False:
                img = pygame.image.load('timeStoneDim.png')
            else:
                img = pygame.image.load('timeStoneGlow.png')
            gameDisplay.blit(img, ((1000-265),630))
        if realityStone == True:
            if realityStoneUse == False:
                img = pygame.image.load('realityStoneDim.png')
            else:
                img = pygame.image.load('realityStoneGlow.png')
            gameDisplay.blit(img, ((1000-310),630))
        # img2 = pygame.image.load('InfinityStones.png')
        # gameDisplay.blit(img2, (690,630))
        textBoxClear22(('$' + str(credit)), 50, (251,30), (255,200,000))
        textBoxClear2(amountList[1], 60, (504,99), (255,255,255))
        textBoxClear2(amountList[2], 60, (504,199), (255,255,255))
        textBoxClear2(amountList[3], 60, (504,299), (255,255,255))
        textBoxClear2(amountList[4], 60, (504,399), (255,255,255))
        textBoxClear2(amountList[5], 60, (504,499), (255,255,255))
        textBoxClear2(amountList[6], 60, (504,599), (255,255,255))
        textBoxClear2(('$' + priceList[1]), 46, (867,99), (255,255,255))
        textBoxClear2(('$' + priceList[2]), 46, (867,199), (255,255,255))
        textBoxClear2(('$' + priceList[3]), 46, (867,299), (255,255,255))
        textBoxClear2(('$' + priceList[4]), 46, (867,399), (255,255,255))
        textBoxClear2(('$' + priceList[5]), 46, (867,499), (255,255,255))
        textBoxClear2(('$' + priceList[6]), 46, (867,599), (255,255,255))
        
        if credit > 750:
            spaceStone = True
        if credit > 2000:
            timeStone = True
        if credit > 20000:
            realityStone = True
        if earth == 616:
            soulStone = True
        if earth == 12:
            mindStone = True
        #POWER STONE CHECKED LATER

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
                    print("PLACEHOLDER")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print("PLACEHOLDER")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 1 < mx < 5:
                    if 1 < my < 5:
                        credit = credit + 1000
                if 251 < mx < 390:
                    if 70 < my < 130:
                        if credit >= round(float(priceList[1]), 2):
                            amountList[1] = str(int(amountList[1]) + 1)
                            credit = credit - round(float(priceList[1]), 2)
                    if 170 < my < 230:
                        if credit >= round(float(priceList[2]), 2):
                            amountList[2] = str(int(amountList[2]) + 1)
                            credit = credit - round(float(priceList[2]), 2)
                    if 270 < my < 330:
                        if credit >= round(float(priceList[3]), 2):
                           amountList[3] = str(int(amountList[3]) + 1)
                           credit = credit - round(float(priceList[3]), 2)
                    if 370 < my < 430:
                        if credit >= round(float(priceList[4]), 2):
                            amountList[4] = str(int(amountList[4]) + 1)
                            credit = credit - round(float(priceList[4]), 2)
                    if 470 < my < 530:
                        if credit >= round(float(priceList[5]), 2):
                            amountList[5] = str(int(amountList[5]) + 1)
                            credit = credit - round(float(priceList[5]), 2)
                    if 570 < my < 630:
                        if credit >= round(float(priceList[6]), 2):
                            amountList[6] = str(int(amountList[6]) + 1)
                            credit = credit - round(float(priceList[6]), 2)
                if 618 < mx < 758:
                    if 70 < my < 130:
                        if int(amountList[1]) > 0:
                            amountList[1] = str(int(amountList[1]) - 1)
                            credit = credit + round(float(priceList[1]), 2)
                    if 170 < my < 230:
                        if int(amountList[2]) > 0:
                            amountList[2] = str(int(amountList[2]) - 1)
                            credit = credit + round(float(priceList[2]), 2)
                    if 270 < my < 330:
                        if int(amountList[3]) > 0:
                            amountList[3] = str(int(amountList[3]) - 1)
                            credit = credit + round(float(priceList[3]), 2)
                    if 370 < my < 430:
                        if int(amountList[4]) > 0:
                            amountList[4] = str(int(amountList[4]) - 1)
                            credit = credit + round(float(priceList[4]), 2)
                    if 470 < my < 530:
                        if int(amountList[5]) > 0:
                            amountList[5] = str(int(amountList[5]) - 1)
                            credit = credit + round(float(priceList[5]), 2)
                    if 570 < my < 630:
                        if int(amountList[6]) > 0:
                            amountList[6] = str(int(amountList[6]) - 1)
                            credit = credit + round(float(priceList[6]), 2)
                credit = round(credit, 2)
                if 630 < my < 700:
                    if 942 < mx < 990:
                        if spaceStone == True:
                            if spaceStoneUse == True:
                                end = True
                    elif 886 < mx < 942:
                        if mindStone == True:
                            if mindStoneUse == True:
                                lowerPrices5 = True
                    elif 843 < mx < 886:
                        if soulStone == True:
                            if soulStoneUse == True:
                                raisePrices5 = True
                    elif 795 < mx < 843:
                        if powerStone == True:
                            if powerStoneUse == True:
                                powerStoneUse = False
                                psclicks = 0
                                oneFreeAll = True
                    elif 735 < mx < 795:
                        if timeStone == True:
                            if timeStoneUse == True:
                                timeStoneUse = False
                                tsclicks = 0
                                pausePrices = True
                    elif 690 < mx < 735:
                        if realityStone == True:
                            if realityStoneUse == True:
                                rsclicks = 0
                                randomisePrices = True
        
        if (int(amountList[1]) >= 50) or (int(amountList[2]) >= 50) or (int(amountList[3]) >= 50) or (int(amountList[4]) >= 50) or (int(amountList[5]) >= 50) or (int(amountList[6]) >= 50):
            powerStone = True

        if oneFreeAll == True:
            amountList[1] = str(int(amountList[1]) + 1)
            amountList[2] = str(int(amountList[2]) + 1)
            amountList[3] = str(int(amountList[3]) + 1)
            amountList[4] = str(int(amountList[4]) + 1)
            amountList[5] = str(int(amountList[5]) + 1)
            amountList[6] = str(int(amountList[6]) + 1)
            oneFreeAll = False

        finalTermNewAmountList = newAmountList[-1]

        if finalTermNewAmountList[-1] == "\n":
            chosenEarthNewAmount = str(earth) + "|"
        else:
            chosenEarthNewAmount = "\n" + str(earth) + "|"
        sixProductCounter = 0
        while sixProductCounter <= 5:
            sixProductCounter = sixProductCounter + 1
            chosenEarthNewAmount = chosenEarthNewAmount + str(amountList[sixProductCounter]) + "|"
    
        newAmountList.append(chosenEarthNewAmount)

        fi = open("amount.txt", "w")
        for i in newAmountList:
            fi.write(i)
        fi.close()
        print(str(newAmountList) + " Amount LIST\n\n\n\n")

        msclicks = msclicks + 1
        if msclicks > 315:
            msclicks = 0
            mindStoneUse = True

        psclicks = psclicks + 1
        if psclicks > 625:
            psclicks = 0
            powerStoneUse = True

        soulsclicks = soulsclicks + 1
        if soulsclicks > 315:
            soulsclicks = 0
            soulStoneUse = True

        tsclicks = tsclicks + 1
        if tsclicks > 190:
            tsclicks = 0
            timeStoneUse = True

        rsclicks = rsclicks + 1
        if rsclicks > 190:
            rsclicks = 0
            realityStoneUse = True
        

        if lowerPrices5 == True:
            mindStoneUse = False
            msclicks = 0
            paa = 0
            while paa < 6:
                paa = paa + 1
                priceList[paa] = str(round((float(priceList[paa]) - 5.00), 2))
                if float(priceList[paa]) < 0.01:
                    priceList[paa] = str(0.01)
            lowerPrices5 = False
        if raisePrices5 == True:
            soulStoneUse = False
            paa = 0
            while paa < 6:
                paa = paa + 1
                priceList[paa] = str(round((float(priceList[paa]) + 5.00), 2))
                if float(priceList[paa]) > 99.99:
                    priceList[paa] = str(99.99)
            raisePrices5 = False
        if randomisePrices == True:
            realityStoneUse = False
            paa = 0
            while paa < 6:
                paa = paa + 1
                rna2 = random.randrange(1000,9000)
                rna2 = rna2 / 100.00
                priceList[paa] = str(rna2)
            randomisePrices = False

        rna3 = random.randrange(0,500)
        if rna3 == 5 or rna3 == 6:
            rna4 = random.randrange(1,7)
            if rna4 == 1:
                if rna3 == 5:
                    if product1 == 'Wayne Enterprises':
                        txtNews = 'Wayne Enterprise CFO sued for malconduct'
                    if product1 == 'Queen Consolidated':
                        txtNews = 'New Queen Consolidated chips recalled'
                    if product1 == 'Stark Industries':
                        txtNews = 'Stark Industries mass recall'
                    if product1 == "Pym Technologies":
                        txtNews = 'Pym Tech bio suit release pushed back'
                    if product1 == 'Château Picard':
                        txtNews = 'Château Picard mass product recall'
                    if product1 == 'JJs Diner':
                        txtNews = 'JJs Diner annonces 2 week closure'
                    if product1 == 'Dunder Mifflin':
                        txtNews = 'Dunder Mifflin paper sent with obscene watermark'
                    if product1 == 'Correlian Engineering Corporation':
                        txtNews = 'Correlian Engineering Corporation shares drop'
                    priceList[1] = str(round((float(priceList[1]) * 0.92), 2))
                if rna3 == 6:
                    if product1 == 'Wayne Enterprises':
                        txtNews = 'Wayne Enterprise announces car line'
                    if product1 == 'Queen Consolidated':
                        txtNews = 'Queen Consolidated finds needed vaccine'
                    if product1 == 'Stark Industries':
                        txtNews = 'Stark Industries new weapons line released'
                    if product1 == "Pym Technologies":
                        txtNews = 'Pym Tech finds proof of another realm'
                    if product1 == 'Château Picard':
                        txtNews = 'A good reception for Château Picard new line'
                    if product1 == 'JJs Diner':
                        txtNews = 'JJs Diner annonces all day turkey leg'
                    if product1 == 'Dunder Mifflin':
                        txtNews = 'Dunder Mifflin add campaign goes well'
                    if product1 == 'Correlian Engineering Corporation':
                        txtNews = 'Correlian Engineering Corporation shares rise'
                    priceList[1] = str(round((float(priceList[1]) * 1.08), 2))
            if rna4 == 2:
                if rna3 == 5:
                    if product2 == 'Daily Planet':
                        txtNews = "Daily Planet accountant arrested for fraud"
                    if product2 == 'STAR Labs':
                        txtNews = "STAR Labs particle accelerator explodes"
                    if product2 == 'AIM':
                        txtNews = "AIM looses contract to Stark"
                    if product2 == "Xaviers School for Gifted Youngsters":
                        txtNews = "Xavier School looses government funding"
                    if product2 == 'United Federation of Planets':
                        txtNews = "Gas leak at United Federation of Planets"
                    if product2 == 'Entertainment 720':
                        txtNews = "Entertainment 720 being investigating by F.B.I"
                    if product2 == 'Prince Family Paper':
                        txtNews = "Prince Paper looses 5 major clients to DMI"
                    if product2 == 'Kuat Drive Yard':
                        txtNews = "Kuat Drive Yards stop production of Y-45"
                    priceList[2] = str(round((float(priceList[2]) * 0.93), 2))

                if rna3 == 6:
                    if product2 == 'Daily Planet':
                        txtNews = "Daily Planet unveils Lex Luthor corruption"
                    if product2 == 'STAR Labs':
                        txtNews = "STAR Labs opens new facility to research dark matter"
                    if product2 == 'AIM':
                        txtNews = "AIM unveils new exosuits"
                    if product2 == "Xaviers School for Gifted Youngsters":
                        txtNews = "Xavier School now open for tours"
                    if product2 == 'United Federation of Planets':
                        txtNews = "United Federation of Planets shares rise"
                    if product2 == 'Entertainment 720':
                        txtNews = "Entertainment 720 throws worlds best party"
                    if product2 == 'Prince Family Paper':
                        txtNews = "Prince Paper shares rise"
                    if product2 == 'Kuat Drive Yard':
                        txtNews = "Kuat Drive Yards begin mass production of new T-3"
                    priceList[2] = str(round((float(priceList[2]) * 1.07), 2))

            if rna4 == 3:
                if rna3 == 5:
                    if product3 == 'Kord Industries':
                        txtNews = "Kord Industries accountant arrested for fraud"
                    if product3 == 'Palmer Technologies':
                        txtNews = "Explosion at Palmer Technologies"
                    if product3 == 'Cross Technologies':
                        txtNews = "Cross Technologies reports mass layoffs"
                    if product3 == "Parker Technologies":
                        txtNews = "Parker Technologies looses government funding"
                    if product3 == 'Starfleet':
                        txtNews = "Explosion at Starfleet headquaters"
                    if product3 == 'Sweetums':
                        txtNews = "Sweetums being investigating by D.O.D"
                    if product3 == 'Sabre':
                        txtNews = "Mass Sabre printer recall"
                    if product3 == 'Mos Eisley Cantina':
                        txtNews = "Shots fired at the Mos Eisley Cantina"
                    priceList[3] = str(round((float(priceList[3]) * 0.94), 2))

                if rna3 == 6:
                    if product3 == 'Kord Industries':
                        txtNews = "Kord Industries discovers more alien artifacts"
                    if product3 == 'Palmer Technologies':
                        txtNews = "Palmer Technologies discovers new particle"
                    if product3 == 'Cross Technologies':
                        txtNews = "Cross Technologies releases new exo-suit"
                    if product3 == "Parker Technologies":
                        txtNews = "Parker Technologies discovers a new element"
                    if product3 == 'Starfleet':
                        txtNews = "Starfleet reports new ships ready for launch"
                    if product3 == 'Sweetums':
                        txtNews = "Sweetums shares rise"
                    if product3 == 'Sabre':
                        txtNews = "Sabre aquires small paper companies"
                    if product3 == 'Mos Eisley Cantina':
                        txtNews = "Mos Eisley Cantina opens new branch"
                    priceList[3] = str(round((float(priceList[3]) * 1.06), 2))

            if rna4 == 4:
                if rna3 == 5:
                    if product4 == 'Iceberg Lounge':
                        txtNews = "Iceberg Lounge flooded with fear toxin"
                    if product4 == 'Luthor Corp':
                        txtNews = "Luthor Corp investigation begins by D.O.D"
                    if product4 == 'Ten Rings':
                        txtNews = "High ranking Ten Rings members arrested"
                    if product4 == "Oscorp":
                        txtNews = "Oscorp investigatin begins by D.O.D"
                    if product4 == 'Romulan Ale':
                        txtNews = "Romulan Ale shares fall"
                    if product4 == 'Rent-A-Swag':
                        txtNews = "Rent-A-Swag announces weekly closure"
                    if product4 == 'Athleap':
                        txtNews = "Athleap share price falls"
                    if product4 == 'Rothana Heavy Engineering':
                        txtNews = "Rothana Heavy Engineering shares fall"
                    priceList[4] = str(round((float(priceList[4]) * 0.94), 2))

                if rna3 == 6:
                    if product4 == 'Iceberg Lounge':
                        txtNews = "Iceberg Lounge reports highly profitable quater"
                    if product4 == 'Luthor Corp':
                        txtNews = "Luthor Corp discovers new particle"
                    if product4 == 'Ten Rings':
                        txtNews = "Ten Rings investigations going nowhere"
                    if product4 == "Oscorp":
                        txtNews = "Oscorp discovers another alien symbiote"
                    if product4 == 'Romulan Ale':
                        txtNews = "Romulan Ale shares rise"
                    if product4 == 'Rent-A-Swag':
                        txtNews = "Rent-A-Swag opens new store"
                    if product4 == 'Athleap':
                        txtNews = "Athleap opens new branch in Texas"
                    if product4 == 'Rothana Heavy Engineering':
                        txtNews = "Rothana Heavy Engineering shares rise"
                    priceList[4] = str(round((float(priceList[4]) * 1.06), 2))

            if rna4 == 5:
                if rna3 == 5:
                    if product5 == 'Ferris Aircraft':
                        txtNews = "Ferris Aircraft attacked by Sinetro"
                    if product5 == 'CatCo Worldwide Media':
                        txtNews = "CatCo attacked by supervillain"
                    if product5 == 'X-Con Security Consultants':
                        txtNews = "X-Con revealed to have hired Ex-Convicts"
                    if product5 == "Rand Corporation":
                        txtNews = "Rand Corporation investigatin begins by D.O.D"
                    if product5 == 'Klingon Empire':
                        txtNews = "Klingon Empire looses territory"
                    if product5 == 'The Snakehole Lounge':
                        txtNews = "The Snakehole Lounge new house spirit fails"
                    if product5 == 'Vance Refrigeration':
                        txtNews = "Bob Vance, Vance Refrigeration crashes car"
                    if product5 == 'Galactic Republic':
                        txtNews = "Galactic Republic looses territory to the Huts"
                    priceList[5] = str(round((float(priceList[5]) * 0.94), 2))

                if rna3 == 6:
                    if product5 == 'Ferris Aircraft':
                        txtNews = "Ferris Aircraft builds new runway"
                    if product5 == 'CatCo Worldwide Media':
                        txtNews = "CatCo shares rise"
                    if product5 == 'X-Con Security Consultants':
                        txtNews = "Robbers fail to break into X-Con facility"
                    if product5 == "Rand Corporation":
                        txtNews = "Rand Corporation recieves government grant"
                    if product5 == 'Klingon Empire':
                        txtNews = "Klingon Empire gains territory"
                    if product5 == 'The Snakehole Lounge':
                        txtNews = "The Snakehole Lounge new house spirit is a hit"
                    if product5 == 'Vance Refrigeration':
                        txtNews = "Vance Refrigeration launches new eco-fridge"
                    if product5 == 'Galactic Republic':
                        txtNews = "Galactic Republic gains territory from the Huts"
                    priceList[5] = str(round((float(priceList[5]) * 1.06), 2))

            if rna4 == 6:
                if rna3 == 5:
                    if product6 == 'Ace Chemicals':
                        txtNews = "Ace Chemicals attacked by Harley Quinn"
                    if product6 == 'Mercury Labs':
                        txtNews = "Mercury Labs broken into by supervillain"
                    if product6 == 'Hammer Industries':
                        txtNews = "Hammer Industries looses contract to Stark"
                    if product6 == "The Daily Bugle":
                        txtNews = "The Daily Bugle investigatin begins by F.B.I"
                    if product6 == 'Deep Space Nine':
                        txtNews = "Deep Space Nine attacked by unknown threat"
                    if product6 == 'Paunch Burger':
                        txtNews = "A Paunch Burger outlet in Eagleton has closed"
                    if product6 == 'Serenity by Jan':
                        txtNews = "Serenity by Jan candles found to be harmful to smell"
                    if product6 == 'Death Watch':
                        txtNews = "Death Watch members killed"
                    priceList[6] = str(round((float(priceList[6]) * 0.95), 2))

                if rna3 == 6:
                    if product6 == 'Ace Chemicals':
                        txtNews = "Ace Chemicals recieves anonymous donation"
                    if product6 == 'Mercury Labs':
                        txtNews = "Mercury Labs discovers new particle"
                    if product6 == 'Hammer Industries':
                        txtNews = "Hammer Industries beats Stark to contract"
                    if product6 == "The Daily Bugle":
                        txtNews = "Daily Bugle photographs great photo of spider-menace"
                    if product6 == 'Deep Space Nine':
                        txtNews = "Deep Space Nine scientists begin dark matter research"
                    if product6 == 'Paunch Burger':
                        txtNews = "Paunch Burger announces a new larger burger"
                    if product6 == 'Serenity by Jan':
                        txtNews = "Serenity by Jan shares rise"
                    if product6 == 'Death Watch':
                        txtNews = "Death Watch unveils corruption in the senate"
                    priceList[6] = str(round((float(priceList[6]) * 1.05), 2))

            printNews = True
            newsclicks = 0

        if printNews == True:
            textBoxClearL(txtNews, 30, (10,670), (255,255,255))

        newsclicks = newsclicks + 1
        if newsclicks >= 90:
            printNews = False
            txtNews = ''


        ssclicks = ssclicks + 1
        if ssclicks == 50:
            spaceStoneUse = True
            ssclicks = 0

        clicks = clicks + 1
        if clicks == 30:
            clicks = 0
            app = 0
            if pausePrices == False:
                while app < 6:
                    app = app + 1
                    rna = random.randrange(95,106)
                    rna = rna / 100.00
                    value1234 = round(float(priceList[app]) * rna, 2)
                    if value1234 > 95.00:
                        value1234 = 94.84
                    if value1234 < 0.70:
                        value1234 = 0.93
                    priceList[app] = str(value1234)
            if pausePrices == True:
                pauseGo = pauseGo + 1
                if pauseGo > 3:
                    pausePrices = False
                    pauseGo = 0
        
        finalTermNewPriceList = newPriceList[-1]

        if finalTermNewPriceList[-1] == "\n":
            chosenEarthNewPrices = str(earth) + "|"
        else:
            chosenEarthNewPrices = "\n" + str(earth) + "|"
        sixProductCounter = 0
        while sixProductCounter <= 5:
            sixProductCounter = sixProductCounter + 1
            chosenEarthNewPrices = chosenEarthNewPrices + str(priceList[sixProductCounter]) + "|"
    
        newPriceList.append(chosenEarthNewPrices)

        f = open("prices.txt", "w")
        for i in newPriceList:
            f.write(i)
        f.close()
        print(str(newPriceList) + " PRICE LIST\n\n\n\n")

        fc = open("credits.txt", "w")
        fc.write(str(credit))
        fc.close()
        # print(str(chosenEarthNewPrices) + " IN FORM PRICE LIST\n\n\n\n")

        pygame.display.update()


def checkEarth():
    global earth
    if earth == 888:
        print("MAIN MENU")
        mainMenu()
    if earth == 366:
        bank()
    print(str(earth) + 'THIS IS THE CURRENT EARTH!')
    if earth == 1:
        print("EARTH-1")
        earthZone('Wayne Enterprises', 'Daily Planet', 'Kord Industries', 'Iceberg Lounge', 'Ferris Aircraft', 'Ace Chemicals')
        earth = 888
    if earth == 0:
        print("STEVE!!!")
        earthZone('Queen Consolidated', 'STAR Labs', 'Palmer Technologies', 'Luthor Corp', 'CatCo Worldwide Media', 'Mercury Labs')
        earth = 888
    if earth == 12:
        earthZone('Stark Industries', 'AIM', 'Cross Technologies', 'Ten Rings', 'X-Con Security Consultants', 'Hammer Industries')
        earth = 888
    if earth == 616:
        earthZone("Pym Technologies", "Xaviers School for Gifted Youngsters", "Parker Technologies", "Oscorp", "Rand Corporation", "The Daily Bugle")
        earth = 888
    if earth == 47:
        earthZone('Château Picard', 'United Federation of Planets', 'Starfleet', 'Romulan Ale', 'Klingon Empire', 'Deep Space Nine')
        earth = 888
    if earth == 48:
        earthZone('JJs Diner', 'Entertainment 720', 'Sweetums', 'Rent-A-Swag', 'The Snakehole Lounge', 'Paunch Burger')
        earth = 888
    if earth == 1725:
        earthZone('Dunder Mifflin', 'Prince Family Paper', 'Sabre', 'Athleap', 'Vance Refrigeration', 'Serenity by Jan')
        earth = 888
    if earth == 2187:
        earthZone('Correlian Engineering Corporation', 'Kuat Drive Yard', 'Mos Eisley Cantina', 'Rothana Heavy Engineering', 'Galactic Republic', 'Death Watch')
        earth = 888

finish = False
while finish == False:
    checkEarth()

#Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()

# Earth-Prime (0)
    # On this Earth, Heroes and Vigulantees protect humanity from villains on and off earth

    # Queen Consolidated
    # S.T.A.R Labs
    # Palmer Technologies
    # Luthor Corp
    # CatCo Worldwide Media
    # Obsidian North
# Earth-1
    # A league of heroes calls this earth home, but it seems that everyone is always trying to thwart them

    # Daily Planet
    # Wayne Enterprises
    # Kord Industries
    # Ferris Aircraft
    # Ace Chemicals
    # Iceberg Lounge
# Earth-12
    # On this Earth, a failed global security network is replaced by heroes using increadible technology and superpowers to protect humanity

    # Stark Industries
    # A.I.M
    # Cross Technologies
    # 10 Ring
    # X-Con Security Consultants
    # Hammer Industries
# Earth-616
    # Mutants, humans and aliens protect this Earth from those who try to destroy it

    # Pym Technologies
    # Xavier's School for Gifted Youngsters
    # Oscorp
    # Parker Technologies
    # Rand Corporation
    # The Daily Bugle
#Earth-1725
    # Are you out of paper, or out of stock, if so, this Earth is where you should be

    # Dunder Mifflin
    # Prince Family Paper
    # Sabre
    # Athleap
    # Vance Refrigeration
    # Serenity by Jan
# Earth-48
    # On this earth you find yourself in Pawnee Indiana where the only threats are Tammy, Jammy, or mini calzones

    # JJ's Diner
    # Entertainment 720
    # Sweetums
    # Rent-A-Swag
    # The Snakehole Lounge
    # Paunch Burger
# Earth-47
    # Centuries in the future, humanity has a galactic presense and releationship with civilisations from other planets

    # Château Picard
    # United Federation of Planets
    # Starfleet
    # Romulan Ale
    # Klingon Empire
    # Deep Space 9
# (Earth) Alderaan-2187
    # A long time ago in a galaxy far, far away...

    # Correlian Engineering Corporation
    # Kuat Drive Yard
    # Mos Eisley Cantina
    # Rothana Heavy Engineering
    # Galactic Republic
    # Death Watch