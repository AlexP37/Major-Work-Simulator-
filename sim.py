# Initialization of Game
import os
import pygame
import math
import random

os.system("clear")

pygame.init()
pygame.font.init()

cont = False
end = False
movementX = 0
movementY = 0

display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Simulator')
clock = pygame.time.Clock()
gameDisplay.fill((255,255,255))

def textBoxClear(text, size, position, color):
    font = pygame.font.Font('LemonMilk.otf', size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect)

class TextBox:
    def __init__(self, text, size, position, color, location, font):
        self.text = text
        self.size = size
        self.position = position
        self.color = color
        self.location = location
        self.font = font
        self.display()

    def display(self):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.color)
        textRect = text.get_rect()

        if self.location == "l":
            textRect.midleft = self.position
        elif self.location == "c":
            textRect.center = self.position
        elif self.location == "r":
            textRect.midright = self.position

        gameDisplay.blit(text, textRect)
        self.rect = textRect

# class HexImage:
#     def __init__(self, xPos, yPos, imageSrc):
#         self.xPos = xPos
#         self.yPos = yPos
#         self.image = pygame.image.load(iself.mageSrc)
#         gameDisplay.blit(self.image, (self.xPos, self.yPos + wobbleHex))

food = []
class FoodPiece:
    def __init__(self, size, xPos, yPos, color):
        self.size = size
        self.xPos = xPos
        self.yPos = yPos
        self.position = (self.xPos, self.yPos)
        self.color = color

class Member():
    def __init__(self, size, color, speed, stamina, xPos, yPos, sense, memory, intelligence):
        self.size = size
        self.color = color
        self.colorOG = color
        self.speed = speed
        self.stamina = stamina
        self.xPos = xPos
        self.yPos = yPos
        self.sense = sense
        self.foodInRange = []
        self.memory = memory
        self.memoryBank = []
        self.intelligence = intelligence
        self.memberFood = 0

        self.justEaten = 0
        self.dying = 0

species = []
def makeMember(speedIt, staminaIt, senseIt, memoryIt):
    memSize = 15
    memColor = (0,0,0)
    memSpeed = speedIt
    memStamina = staminaIt
    memSense = senseIt
    memXPos = random.randrange(15,950 - 15)
    memYPos = random.randrange(15,display_height - 15)
    memMemory = memoryIt
    memIntelligence = 1

    species.append(Member(memSize, memColor, memSpeed, memStamina, memXPos, memYPos, memSense, memMemory, memIntelligence))

def makeFood():
    foodSize = 3
    foodColor = (0,0,255)
    foodXPos = random.randrange(15,950 - 15)
    foodYPos = random.randrange(15,display_height - 15)

    food.append(FoodPiece(foodSize, foodXPos, foodYPos, foodColor))

foodCounter = 0

hard = False

## -------------------------------------- Intro --------------------------------------
introCounter = 0
while end == False:
    clock.tick(60)
    mx, my = pygame.mouse.get_pos()
    introCounter += 1

    if introCounter > 255:
        pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))
    else:
        pygame.draw.rect(gameDisplay, (introCounter,introCounter,introCounter), (0, 0, display_width, display_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.font.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
                cont = True
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.key == pygame.K_c:
                introCounter = 599
    
    if 300 < introCounter < 555:
        heading = TextBox("A Poping! Software Solution", 40, (600,400), (introCounter - 300,introCounter - 300,introCounter - 300), "c", "LemonMilk.otf")
    elif introCounter >= 555:
        heading = TextBox("A Poping! Software Solution", 40, (600,400), (255,255,255), "c", "LemonMilk.otf")
    else:
        heading = TextBox("A Poping! Software Solution", 40, (600,400), (0,0,0), "c", "LemonMilk.otf")

    
    heading.display()

    if introCounter > 600:
        end = True

    pygame.display.update()

## -------------------------------------- Startup Button --------------------------------------
cont = False
mouseDown = False
gameDisplay.fill((255,255,255))
textBoxClear("Begin", 300, (display_width / 2, display_height / 2), (0,0,0))
while cont == False:
    clock.tick(60)
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            cont = True
            end = True
            pygame.quit()
            pygame.font.quit()
            quit()
        if 245 < mx < 967 and 277 < my < 529:
            gameDisplay.fill((255,255,255))
            textBoxClear("Begin", 320, (display_width / 2, display_height / 2), (0,0,0))
            if event.type == pygame.MOUSEBUTTONDOWN or mouseDown == True:
                onPlayButton = True
                mouseDown = True
                gameDisplay.fill((255,255,255))
                textBoxClear("Begin", 320, (display_width / 2, display_height / 2), (0,100,0))
            if event.type == pygame.MOUSEBUTTONUP and mouseDown == True:
                if onPlayButton == True:
                    cont = True
                mouseDown = False
                gameDisplay.fill((255,255,255))
        else:
            gameDisplay.fill((255,255,255))
            textBoxClear("Begin", 300, (display_width / 2, display_height / 2), (0,0,0))
        if event.type == pygame.MOUSEBUTTONUP and mouseDown == True:
            onPlayButton = False
            mouseDown = False
    pygame.display.update()


## -------------------------------------- Main Menu --------------------------------------
end = False
speciesSurvival = False
creative = False
uVworld = False
while end == False:
    clock.tick(60)
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.font.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                cont = True
                pygame.quit()
                pygame.font.quit()
                quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 < mx < 1170:
                if 215 < my < 300:
                    end = True
                    speciesSurvival = True
            if 150 < mx < 1170:
                if 365 < my < 445:
                    end = True
                    uVworld = True
            if 150 < mx < 1170:
                if 515 < my < 595:
                    end = True
                    creative = True

    pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))

    heading = TextBox("Species Simulator", 100, (50,100), (0,0,0), "l", "LemonMilk.otf")
    heading.display()


    title1 = TextBox("- Species Survival", 100, (150,250), (50,50,50), "l", "LMLight.otf")
    title1.display()


    title2 = TextBox("- U vs The World", 100, (150,400), (50,50,50), "l", "LMLight.otf")
    title2.display()


    title3 = TextBox("- Creative Mode", 100, (150,550), (50,50,50), "l", "LMLight.otf")
    title3.display()

    pygame.display.update()



## -------------------------------------- Nameing --------------------------------------
def namer():
    global naming
    naming = True
    global name
    name = ""
    flasher = 0
    limitReacher = 1000

    charsAllowed = [45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

    while naming == True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        flasher += 1
        limitReacher += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cont = True
                    naming = False
                    pygame.quit()
                    pygame.font.quit()
                    quit()
                if event.key == 13: ## 13 is return
                    if len(name) > 1:
                        naming = False

                if event.key in charsAllowed:
                    if len(name) < 12:
                        name = name + chr(event.key)
                    else:
                        limitReacher = 0

                if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]


        pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))

        heading = TextBox("Species Information", 100, (50,100), (0,0,0), "l", "LemonMilk.otf")

        nameHeading = TextBox("Name: ", 75, (50,225), (0,0,0), "l", "LemonMilk.otf")

        if flasher > 40 or len(name) > 11:
            nameDisplayer = TextBox(name, 75, (315,225), (0,0,0), "l", "LMLight.otf")
        else:
            nameDisplayer = TextBox(name + "|", 75, (315,225), (0,0,0), "l", "LMLight.otf")

        if flasher > 80:
            flasher = 0

        if limitReacher < 100:
            messageDisplayer = TextBox("Name length limit reached", 20, (50,180), (125,0,0), "l", "LMLight.otf")
        elif len(name) > 1:
            messageDisplayer = TextBox("Press Enter to sumbit name", 20, (50,180), (0,125,0), "l", "LMLight.otf")

        if len(name) < 12:
            limitReacher = 1000

        pygame.display.update()

namer()

## -------------------------------------- DNA Config --------------------------------------
DNAing = True

mouseButtonIsDown = False

charsAllowed = [45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

wobbleHexVar = 0
wobbleHex = math.sin(wobbleHexVar) * 5


hexMemoryXpos = 240
hexSpeedXpos = 453
hexStaminaXpos = 666
hexSenseXpos = 880

hexMemoryYpos = 650
hexSpeedYpos = 650
hexStaminaYpos = 650
hexSenseYpos = 650

hexMemoryXposOG = 240
hexSpeedXposOG = 453
hexStaminaXposOG = 666
hexSenseXposOG = 880

hexMemoryYposOG = 650
hexSpeedYposOG = 650
hexStaminaYposOG = 650
hexSenseYposOG = 650

downXpos = 0
downYpos = 0

DNAslot1 = 'null'
DNAslot2 = 'null'

mosueButtonReleased = False

downOnSense = False
downOnSpeed = False
downOnStamina = False
downOnMemory = False

while DNAing == True:
    clock.tick(60)
    mx, my = pygame.mouse.get_pos()
    mosueButtonReleased = False

    wobbleHexVar += 0.1
    wobbleHex = math.sin(wobbleHexVar) * 5

    pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))

    heading = TextBox("Species Information", 100, (50,100), (0,0,0), "l", "LemonMilk.otf")

    nameHeading = TextBox("Name: ", 75, (50,225), (0,0,0), "l", "LemonMilk.otf")
    nameDisplayer = TextBox(name, 75, (315,225), (0,0,0), "l", "LMLight.otf")

    dnaImg = pygame.image.load('dna.png')
    gameDisplay.blit(dnaImg, (200, 400))

    hexImg1 = pygame.image.load('hex.png')
    gameDisplay.blit(hexImg1, (452, 372))

    hexImg2 = pygame.image.load('hex.png')
    gameDisplay.blit(hexImg2, (674, 372))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.font.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                cont = True
                naming = False
                pygame.quit()
                pygame.font.quit()
                quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonIsDown = True
            downXpos = mx
            downYpos = my

        if event.type == pygame.MOUSEBUTTONUP:
            mouseButtonIsDown = False
            mosueButtonReleased = True
            downOnSense = False
            downOnSpeed = False
            downOnStamina = False
            downOnMemory = False

    tick = pygame.image.load('tick.png')
    gameDisplay.blit(tick, (1025, 441))
    if mx in range(1025,1150) and my in range(441,566):
        if downXpos == mx and downYpos == my:
            DNAing = False

    arrow = pygame.image.load('arrow.png')
    gameDisplay.blit(arrow, (50, 441))
    if mx in range(50,175) and my in range(441,566):
        if downXpos == mx and downYpos == my:
            namer()

            DNAing = True
            mouseButtonIsDown = False
            charsAllowed = [45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 12]
            wobbleHexVar = 0
            wobbleHex = math.sin(wobbleHexVar) * 5
            hexMemoryXpos = 240
            hexSpeedXpos = 453
            hexStaminaXpos = 666
            hexSenseXpos = 880
            hexMemoryYpos = 650
            hexSpeedYpos = 650
            hexStaminaYpos = 650
            hexSenseYpos = 650
            hexMemoryXposOG = 240
            hexSpeedXposOG = 453
            hexStaminaXposOG = 666
            hexSenseXposOG = 880
            hexMemoryYposOG = 650
            hexSpeedYposOG = 650
            hexStaminaYposOG = 650
            hexSenseYposOG = 650
            downXpos = 0
            downYpos = 0
            DNAslot1 = 'null'
            DNAslot2 = 'null'
            mosueButtonReleased = False
            downOnSense = False
            downOnSpeed = False
            downOnStamina = False
            downOnMemory = False


    if my in range(int(hexMemoryYpos), int(hexMemoryYpos) + 80):
        if mx in range(hexMemoryXpos, hexMemoryXpos + 80):
            if mouseButtonIsDown == False:
                hoverTxt = TextBox("Memory: Increases species ability to remember food location", 11, (hexMemoryXpos + 40, hexMemoryYpos - 10), (0,0,125), "c", "LMLight.otf")
            elif downOnSense == False and downOnSpeed == False and downOnStamina == False:
                downOnMemory = True
                if DNAslot1 == 'memory':
                    DNAslot1 = 'null'
                elif DNAslot2 == 'memory':
                    DNAslot2 = 'null'
                
            if mosueButtonReleased == True:
                if mx in range(452, 452 + 80) and my in range(372, 372 +80) and DNAslot1 == 'null':
                    hexMemoryXpos = 452
                    hexMemoryYpos = 372
                    DNAslot1 = 'memory'
                elif mx in range(674, 674 + 80) and my in range(372, 372 +80) and DNAslot2 == 'null':
                    hexMemoryXpos = 674
                    hexMemoryYpos = 372
                    DNAslot2 = 'memory'
                else:
                    hexMemoryXpos = hexMemoryXposOG
                    hexMemoryYpos = hexMemoryYposOG
                    if DNAslot1 == 'memory':
                        DNAslot1 = 'null'
                    elif DNAslot2 == 'memory':
                        DNAslot2 = 'null'
    if downOnMemory == True:
        hexMemoryXpos = hexMemoryXposOG - (downXpos - mx) 
        hexMemoryYpos = hexMemoryYposOG - (downYpos - my) - wobbleHex
        if (hexMemoryYpos - my) > 80 or (hexMemoryYpos - my) < -80:
            hexMemoryYpos = my - 40
        if (hexMemoryXpos - mx) > 80 or (hexMemoryXpos - mx) < -80:
            hexMemoryXpos = mx - 40
    hexMem = pygame.image.load('hexMemory.png')          
    if DNAslot1 == 'memory' or DNAslot2 == 'memory':
        gameDisplay.blit(hexMem, (hexMemoryXpos, hexMemoryYpos))
    else:
        gameDisplay.blit(hexMem, (hexMemoryXpos, hexMemoryYpos + wobbleHex))


    if my in range(int(hexSpeedYpos), int(hexSpeedYpos) + 80):
        if mx in range(hexSpeedXpos, hexSpeedXpos + 80):
            if mouseButtonIsDown == False:
                hoverTxt = TextBox("Speed: Increases speed of species", 11, (hexSpeedXpos + 40, hexSpeedYpos - 10), (0,0,125), "c", "LMLight.otf")
            elif downOnSense == False and downOnMemory == False and downOnStamina == False:
                downOnSpeed = True
                if DNAslot1 == 'speed':
                    DNAslot1 = 'null'
                elif DNAslot2 == 'speed':
                    DNAslot2 = 'null'
                
            if mosueButtonReleased == True:
                if mx in range(452, 452 + 80) and my in range(372, 372 +80) and DNAslot1 == 'null':
                    hexSpeedXpos = 452
                    hexSpeedYpos = 372
                    DNAslot1 = 'speed'
                elif mx in range(674, 674 + 80) and my in range(372, 372 +80) and DNAslot2 == 'null':
                    hexSpeedXpos = 674
                    hexSpeedYpos = 372
                    DNAslot2 = 'speed'
                else:
                    hexSpeedXpos = hexSpeedXposOG
                    hexSpeedYpos = hexSpeedYposOG
                    if DNAslot1 == 'speed':
                        DNAslot1 = 'null'
                    elif DNAslot2 == 'speed':
                        DNAslot2 = 'null'
    if downOnSpeed == True:
        hexSpeedXpos = hexSpeedXposOG - (downXpos - mx) 
        hexSpeedYpos = hexSpeedYposOG - (downYpos - my) - wobbleHex
        if (hexSpeedYpos - my) > 80 or (hexSpeedYpos - my) < -80:
            hexSpeedYpos = my - 40
        if (hexSpeedXpos - mx) > 80 or (hexSpeedXpos - mx) < -80:
            hexSpeedXpos = mx - 40
    hexSpe = pygame.image.load('hexSpeed.png')
    if DNAslot1 == 'speed' or DNAslot2 == 'speed':
        gameDisplay.blit(hexSpe, (hexSpeedXpos, hexSpeedYpos))
    else:
        gameDisplay.blit(hexSpe, (hexSpeedXpos, hexSpeedYpos + wobbleHex))
    


    if my in range(int(hexStaminaYpos), int(hexStaminaYpos) + 80):
        if mx in range(hexStaminaXpos, hexStaminaXpos + 80):
            if mouseButtonIsDown == False:
                hoverTxt = TextBox("Stamina: Increases species total health allowing for longer without food", 11, (hexStaminaXpos + 40, hexStaminaYpos - 10), (0,0,125), "c", "LMLight.otf")
            elif downOnSense == False and downOnSpeed == False and downOnMemory == False:
                downOnStamina = True
                if DNAslot1 == 'stamina':
                    DNAslot1 = 'null'
                elif DNAslot2 == 'stamina':
                    DNAslot2 = 'null'
                
            if mosueButtonReleased == True:
                if mx in range(452, 452 + 80) and my in range(372, 372 +80) and DNAslot1 == 'null':
                    hexStaminaXpos = 452
                    hexStaminaYpos = 372
                    DNAslot1 = 'stamina'
                elif mx in range(674, 674 + 80) and my in range(372, 372 +80) and DNAslot2 == 'null':
                    hexStaminaXpos = 674
                    hexStaminaYpos = 372
                    DNAslot2 = 'stamina'
                else:
                    hexStaminaXpos = hexStaminaXposOG
                    hexStaminaYpos = hexStaminaYposOG
                    if DNAslot1 == 'stamina':
                        DNAslot1 = 'null'
                    elif DNAslot2 == 'stamina':
                        DNAslot2 = 'null'
    if downOnStamina == True:
        hexStaminaXpos = hexStaminaXposOG - (downXpos - mx) 
        hexStaminaYpos = hexStaminaYposOG - (downYpos - my) - wobbleHex
        if (hexStaminaYpos - my) > 80 or (hexStaminaYpos - my) < -80:
            hexStaminaYpos = my - 40
        if (hexStaminaXpos - mx) > 80 or (hexStaminaXpos - mx) < -80:
            hexStaminaXpos = mx - 40
    hexSta = pygame.image.load('hexStamina.png')
    if DNAslot1 == 'stamina' or DNAslot2 == 'stamina':
        gameDisplay.blit(hexSta, (hexStaminaXpos, hexStaminaYpos))
    else:
        gameDisplay.blit(hexSta, (hexStaminaXpos, hexStaminaYpos + wobbleHex))
    
            

    if my in range(int(hexSenseYpos), int(hexSenseYpos) + 80):
        if mx in range(hexSenseXpos, hexSenseXpos + 80):
            if mouseButtonIsDown == False:
                hoverTxt = TextBox("Sense: Increases species ability to sense food from a further distance", 11, (hexSenseXpos + 40, hexSenseYpos - 10), (0,0,125), "c", "LMLight.otf")
            elif downOnMemory == False and downOnSpeed == False and downOnStamina == False:
                downOnSense = True
                if DNAslot1 == 'sense':
                    DNAslot1 = 'null'
                elif DNAslot2 == 'sense':
                    DNAslot2 = 'null'
                
            if mosueButtonReleased == True:
                if mx in range(452, 452 + 80) and my in range(372, 372 +80) and DNAslot1 == 'null':
                    hexSenseXpos = 452
                    hexSenseYpos = 372
                    DNAslot1 = 'sense'
                elif mx in range(674, 674 + 80) and my in range(372, 372 +80) and DNAslot2 == 'null':
                    hexSenseXpos = 674
                    hexSenseYpos = 372
                    DNAslot2 = 'sense'
                else:
                    hexSenseXpos = hexSenseXposOG
                    hexSenseYpos = hexSenseYposOG
                    if DNAslot1 == 'sense':
                        DNAslot1 = 'null'
                    elif DNAslot2 == 'sense':
                        DNAslot2 = 'null'
    if downOnSense == True:
        hexSenseXpos = hexSenseXposOG - (downXpos - mx) 
        hexSenseYpos = hexSenseYposOG - (downYpos - my) - wobbleHex
        if (hexSenseYpos - my) > 80 or (hexSenseYpos - my) < -80:
            hexSenseYpos = my - 40
        if (hexSenseXpos - mx) > 80 or (hexSenseXpos - mx) < -80:
            hexSenseXpos = mx - 40
    hexSen = pygame.image.load('hexSense.png')
    if DNAslot1 == 'sense' or DNAslot2 == 'sense':
        gameDisplay.blit(hexSen, (hexSenseXpos, hexSenseYpos))
    else:
        gameDisplay.blit(hexSen, (hexSenseXpos, hexSenseYpos + wobbleHex))

    pygame.display.update()



## -------------------------------------- Initialising --------------------------------------
cont = False
foodItemPoints = 0

## -------------------------------------- Creative --------------------------------------
if creative == True:

    speciesSpeed = 1
    speciesStamina = 150
    speciesSense = 100
    speciesMemory = 1

    if DNAslot1 == 'speed' or DNAslot2 == 'speed':
        speciesSpeed = 3
    if DNAslot1 == 'stamina' or DNAslot2 == 'stamina':
        speciesStamina = 250
    if DNAslot1 == 'sense' or DNAslot2 == 'sense':
        speciesSense = 125
    if DNAslot1 == 'memory' or DNAslot2 == 'memory':
        speciesMemory = 5

    for i in range(1,10):
        makeMember(speciesSpeed, speciesStamina, speciesSense, speciesMemory)
        
    while cont == False:
        clock.tick(60)
        foodCounter += 1
        foodItemPoints = 1000
        mx, my = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cont = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx in range(965,1005) and my in range(165,205):
                    if speciesSpeed > 1:
                        speciesSpeed -= 0.5
                if mx in range(965 + 175,1005 + 175) and my in range(165,205):
                    if foodItemPoints > 0:
                        speciesSpeed += 0.5
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(265,305):
                    if speciesStamina > 1:
                        speciesStamina -= 5
                if mx in range(965 + 175,1005 + 175) and my in range(265,305):
                    if foodItemPoints > 0:
                        speciesStamina += 5
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(365,405):
                    if speciesSense > 1:
                        speciesSense -= 1
                if mx in range(965 + 175,1005 + 175) and my in range(365,405):
                    if foodItemPoints > 0:
                        speciesSense += 1
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(465,505):
                    if speciesMemory > 1:
                        speciesMemory -= 1
                if mx in range(965 + 175,1005 + 175) and my in range(465,505):
                    if foodItemPoints > 0:
                        speciesMemory += 1
                        foodItemPoints -= 1

        

        for mem in species:

            mem.speed = speciesSpeed
            mem.sense = speciesSense
            mem.stamina = speciesStamina
            mem.memory = speciesMemory

            # if mem.intelligence == 1:

            mem.foodInRange = []
            mem.dying += 0.05

            if mem.dying > mem.stamina:
                species.remove(mem)

            else:
                if mem.justEaten != 0:
                    mem.justEaten -= 5
                
                mem.color = (0 + mem.dying, 0 + mem.dying + mem.justEaten, 0 + mem.dying)

                for storedFoodItem in mem.memoryBank:
                    distanceFromItem = (((mem.xPos - storedFoodItem.xPos)**2) + ((mem.yPos - storedFoodItem.yPos)**2))**(1/2)

                    if distanceFromItem <= mem.sense:
                        if storedFoodItem not in food:
                            mem.memoryBank.remove(storedFoodItem)
                    else:
                        mem.foodInRange.append(storedFoodItem)

                for f in food:
                    distance = (((mem.xPos - f.xPos)**2) + ((mem.yPos - f.yPos)**2))**(1/2)

                    if distance <= mem.size:
                        food.remove(f)
                        foodItemPoints += 1
                        mem.memberFood += 1
                        mem.justEaten = 100
                        mem.dying -= 100
                        if mem.dying < 0:
                            mem.dying = 0
                    elif distance <= mem.sense:
                        mem.foodInRange.append(f)
                
                if mem.foodInRange != []:
                    closest = mem.foodInRange[0]
                    closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)

                    for item in range(1, len(mem.foodInRange)):
                        itemDistance = (((mem.xPos - mem.foodInRange[item].xPos)**2) + ((mem.yPos - mem.foodInRange[item].yPos)**2))**(1/2)
                        if itemDistance < closestDistance:
                            closest = mem.foodInRange[item]   
                            closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)  

                    mem.xPos += ((closest.xPos - mem.xPos)/closestDistance)*((mem.speed)**(1/2))
                    mem.yPos += ((closest.yPos - mem.yPos)/closestDistance)*((mem.speed)**(1/2))

                    mem.dying += mem.speed*0.01
                
                if mem.memory > 0:
                    for item in mem.foodInRange:
                        if len(mem.memoryBank) < mem.memory:
                            if item not in mem.memoryBank:
                                mem.memoryBank.append(item)





        pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))
                    
        for mem in species:
            circleRectangle = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.sense * 2, mem.sense * 2))
            circleSurface = pygame.Surface(circleRectangle.size, pygame.SRCALPHA)
            pygame.draw.circle(circleSurface, (200,200,200,100), (mem.sense, mem.sense), mem.sense)
            gameDisplay.blit(circleSurface, circleRectangle)

        for mem in species:
            pygame.draw.circle(gameDisplay, mem.color, (mem.xPos, mem.yPos), mem.size)

        for f in food:
            pygame.draw.circle(gameDisplay, f.color, f.position, f.size)

        pygame.draw.rect(gameDisplay, (255,255,255), (949, 0, (display_width - 949), display_height))
        pygame.draw.rect(gameDisplay, (0,0,0), (949, 0, 2, display_height))

        gameModeTextBox = TextBox("creative", 10, (1075,20), (0,0,0), "c", "LMLight.otf")
        nameTextBox = TextBox(name, 20, (1075,40), (0,0,0), "c", "LemonMilk.otf")

        foodPointsTextBox = TextBox("Food Points: ", 15, (965,100), (0,0,0), "l", "LemonMilk.otf")
        foodPointsTextBoxNum = TextBox("Unlimited", 15, (1075,99), (0,0,0), "l", "LMLight.otf")



        traitTxt = TextBox("Speed", 15, (965,150), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 165))
        traitQntTxt = TextBox(str(speciesSpeed), 15, (1072,185), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Stamina", 15, (965,250), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 265))
        traitQntTxt = TextBox(str(speciesStamina), 15, (1072,285), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Sense", 15, (965,350), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 365))
        traitQntTxt = TextBox(str(speciesSense), 15, (1072,385), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Memory", 15, (965,450), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 465))
        traitQntTxt = TextBox(str(speciesMemory), 15, (1072,485), (0,0,0), "c", "LemonMilk.otf")
        
        
        if foodCounter == 60:
            makeFood()
            foodCounter = 0

        pygame.display.update()

## -------------------------------------- u V world Sub-Menu --------------------------------------
if uVworld == True:
    end = False
    while end == False:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cont = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < mx < 600:
                    hard = True
                    end = True
                else:
                    hard = False
                    end = True

        pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))

        heading = TextBox("Hard", 100, (300,display_height/2), (0,0,0), "c", "LemonMilk.otf")
        heading.display()

        pygame.draw.rect(gameDisplay, (0,0,0), (595, 0, 10, display_height))

        heading = TextBox("Easy", 100, (900,display_height/2), (0,0,0), "c", "LemonMilk.otf")
        heading.display()

        pygame.display.update()

## -------------------------------------- u V world --------------------------------------
if uVworld == True:

    wIsDown = False
    sIsDown = False
    aIsDown = False
    dIsDown = False

    speciesSpeed = 1
    speciesStamina = 150
    speciesSense = 100
    speciesMemory = 1

    if DNAslot1 == 'speed' or DNAslot2 == 'speed':
        speciesSpeed = 3
    if DNAslot1 == 'stamina' or DNAslot2 == 'stamina':
        speciesStamina = 250
    if DNAslot1 == 'sense' or DNAslot2 == 'sense':
        speciesSense = 125
    if DNAslot1 == 'memory' or DNAslot2 == 'memory':
        speciesMemory = 5
    
    memSize = 15
    memColor = (0,0,0)
    memSpeed = speciesSpeed
    memStamina = speciesStamina
    memSense = speciesSense
    memXPos = random.randrange(15,950 - 15)
    memYPos = random.randrange(15,display_height - 15)
    memMemory = speciesMemory
    memIntelligence = 1

    uSpecies = [Member(memSize, memColor, memSpeed, memStamina, memXPos, memYPos, memSense, memMemory, memIntelligence)]

    for i in range(1,12):
        memSize = 15
        memColor = (random.randrange(1,254),random.randrange(1,254),random.randrange(1,254))
        memSpeed = 1
        memStamina = 150
        memSense = 100
        memXPos = random.randrange(15,950 - 15)
        memYPos = random.randrange(15,display_height - 15)
        memMemory = 1
        memIntelligence = 1

        species.append(Member(memSize, memColor, memSpeed, memStamina, memXPos, memYPos, memSense, memMemory, memIntelligence))
        
    while cont == False:
        clock.tick(60)
        foodCounter += 1
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cont = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()

                if event.key == pygame.K_w:
                    wIsDown = True
                if event.key == pygame.K_s:
                    sIsDown = True
                if event.key == pygame.K_a:
                    aIsDown = True
                if event.key == pygame.K_d:
                    dIsDown = True
            
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_w:
                    wIsDown = False
                if event.key == pygame.K_s:
                    sIsDown = False
                if event.key == pygame.K_a:
                    aIsDown = False
                if event.key == pygame.K_d:
                    dIsDown = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx in range(965,1005) and my in range(165,205):
                    if speciesSpeed > 1:
                        speciesSpeed -= 0.5
                if mx in range(965 + 175,1005 + 175) and my in range(165,205):
                    if foodItemPoints > 0:
                        speciesSpeed += 0.5
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(265,305):
                    if speciesStamina > 1:
                        speciesStamina -= 5
                if mx in range(965 + 175,1005 + 175) and my in range(265,305):
                    if foodItemPoints > 0:
                        speciesStamina += 5
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(365,405):
                    if speciesSense > 1:
                        speciesSense -= 1
                if mx in range(965 + 175,1005 + 175) and my in range(365,405):
                    if foodItemPoints > 0:
                        speciesSense += 1
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(465,505):
                    if speciesMemory > 1:
                        speciesMemory -= 1
                if mx in range(965 + 175,1005 + 175) and my in range(465,505):
                    if foodItemPoints > 0:
                        speciesMemory += 1
                        foodItemPoints -= 1

        for mem in uSpecies: 
            if wIsDown == True and mem.yPos - (1 * (mem.speed*0.6)**(1/2)) > (mem.size *2)/2 and sIsDown == False:
                mem.yPos -= 1 * (mem.speed*0.6)**(1/2)
                mem.dying += mem.speed*0.01
            
            if sIsDown == True  and mem.yPos + (1 * (mem.speed*0.6)**(1/2)) < display_height - (mem.size *2)/2 and wIsDown == False:
                mem.yPos += 1 * (mem.speed*0.6)**(1/2)
                mem.dying += mem.speed*0.01

            if aIsDown == True  and mem.xPos - (1 * (mem.speed*0.6)**(1/2)) > (mem.size *2)/2 and dIsDown == False:
                mem.xPos -= 1 * (mem.speed*0.6)**(1/2)
                mem.dying += mem.speed*0.01
            
            if dIsDown == True  and mem.xPos + (1 * (mem.speed*0.6)**(1/2)) < 950 - (mem.size *2)/2 and aIsDown == False:
                mem.xPos += 1 * (mem.speed*0.6)**(1/2)
                mem.dying += mem.speed*0.01

        for mem in species:

            # if mem.intelligence == 1:

            mem.foodInRange = []
            mem.dying += 0.05

            if mem.memberFood > 1:
                picker = random.randrange(1,4)

                if picker == 1:
                    mem.speed += 0.5
                    mem.memberFood -= 1
                elif picker == 2:
                    mem.stamina += 5
                    mem.memberFood -= 1
                elif picker == 3:
                    mem.sense += 1
                    mem.memberFood -= 1
                else:
                    mem.memory += 1
                    mem.memberFood -= 1

            if mem.dying > mem.stamina:
                species.remove(mem)

            else:
                if mem.justEaten != 0:
                    mem.justEaten -= 5
                
                mem.color = (0 + mem.dying, 0 + mem.dying + mem.justEaten, 0 + mem.dying)

                for storedFoodItem in mem.memoryBank:
                    distanceFromItem = (((mem.xPos - storedFoodItem.xPos)**2) + ((mem.yPos - storedFoodItem.yPos)**2))**(1/2)

                    if distanceFromItem <= mem.sense:
                        if storedFoodItem not in food:
                            mem.memoryBank.remove(storedFoodItem)
                    else:
                        mem.foodInRange.append(storedFoodItem)

                for f in food:
                    distance = (((mem.xPos - f.xPos)**2) + ((mem.yPos - f.yPos)**2))**(1/2)

                    if distance <= mem.size:
                        food.remove(f)
                        mem.memberFood += 1
                        mem.justEaten = 100
                        mem.dying -= 100
                        if mem.dying < 0:
                            mem.dying = 0
                    elif distance <= mem.sense:
                        mem.foodInRange.append(f)
                
                if mem.foodInRange != []:
                    closest = mem.foodInRange[0]
                    closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)

                    for item in range(1, len(mem.foodInRange)):
                        itemDistance = (((mem.xPos - mem.foodInRange[item].xPos)**2) + ((mem.yPos - mem.foodInRange[item].yPos)**2))**(1/2)
                        if itemDistance < closestDistance:
                            closest = mem.foodInRange[item]   
                            closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)  

                    mem.xPos += ((closest.xPos - mem.xPos)/closestDistance)*((mem.speed)**(1/2))
                    mem.yPos += ((closest.yPos - mem.yPos)/closestDistance)*((mem.speed)**(1/2))

                    mem.dying += mem.speed*0.01
                
                if mem.memory > 0:
                    for item in mem.foodInRange:
                        if len(mem.memoryBank) < mem.memory:
                            if item not in mem.memoryBank:
                                mem.memoryBank.append(item)
        
        for mem in uSpecies:

            mem.speed = speciesSpeed
            mem.sense = speciesSense
            mem.stamina = speciesStamina
            mem.memory = speciesMemory

            # if mem.intelligence == 1:

            mem.foodInRange = []
            mem.dying += 0.05

            if mem.dying > mem.stamina:
                uSpecies.remove(mem)

            else:
                if mem.justEaten != 0:
                    mem.justEaten -= 5
                
                mem.color = (0 + mem.dying, 0 + mem.dying + mem.justEaten, 0 + mem.dying)

                for storedFoodItem in mem.memoryBank:
                    distanceFromItem = (((mem.xPos - storedFoodItem.xPos)**2) + ((mem.yPos - storedFoodItem.yPos)**2))**(1/2)

                    if distanceFromItem <= mem.sense:
                        if storedFoodItem not in food:
                            mem.memoryBank.remove(storedFoodItem)
                    else:
                        mem.foodInRange.append(storedFoodItem)

                for f in food:
                    distance = (((mem.xPos - f.xPos)**2) + ((mem.yPos - f.yPos)**2))**(1/2)

                    if distance <= mem.size:
                        food.remove(f)
                        foodItemPoints += 1
                        mem.memberFood += 1
                        mem.justEaten = 100
                        mem.dying -= 100
                        if mem.dying < 0:
                            mem.dying = 0
                    elif distance <= mem.sense:
                        mem.foodInRange.append(f)
                
                if mem.foodInRange != []:
                    closest = mem.foodInRange[0]
                    closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)

                    for item in range(1, len(mem.foodInRange)):
                        itemDistance = (((mem.xPos - mem.foodInRange[item].xPos)**2) + ((mem.yPos - mem.foodInRange[item].yPos)**2))**(1/2)
                        if itemDistance < closestDistance:
                            closest = mem.foodInRange[item]   
                            closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)  
                    
                    if aIsDown == False and dIsDown == False and wIsDown == False and sIsDown == False:
                        mem.xPos += ((closest.xPos - mem.xPos)/closestDistance)*((mem.speed)**(1/2))
                        mem.yPos += ((closest.yPos - mem.yPos)/closestDistance)*((mem.speed)**(1/2))

                        mem.dying += mem.speed*0.01
                
                if mem.memory > 0:
                    for item in mem.foodInRange:
                        if len(mem.memoryBank) < mem.memory:
                            if item not in mem.memoryBank:
                                mem.memoryBank.append(item)





        pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))
                    
        for mem in species:
            circleRectangle = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.sense * 2, mem.sense * 2))
            circleSurface = pygame.Surface(circleRectangle.size, pygame.SRCALPHA)
            pygame.draw.circle(circleSurface, (200,200,200,100), (mem.sense, mem.sense), mem.sense)
            gameDisplay.blit(circleSurface, circleRectangle)

        for mem in species:
            pygame.draw.circle(gameDisplay, mem.color, (mem.xPos, mem.yPos), mem.size)

            circleRectangle = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.size * 2, mem.size * 2))
            circleSurface = pygame.Surface(circleRectangle.size, pygame.SRCALPHA)
            pygame.draw.circle(circleSurface, (mem.colorOG[0],mem.colorOG[1],mem.colorOG[2],100), (mem.size, mem.size), mem.size)
            gameDisplay.blit(circleSurface, circleRectangle)
        
        for mem in uSpecies:
            if hard == True:
                circleRectangleHrd = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.sense * 2, mem.sense * 2))
                circleSurfaceHrd = pygame.Surface(circleRectangleHrd.size, pygame.SRCALPHA)

                pygame.draw.rect(circleSurfaceHrd, (126,126,126,255), (0, 0, display_width, display_height))

                pygame.draw.circle(circleSurfaceHrd, (0,0,220,10), (mem.sense, mem.sense), mem.sense)
    

            else:
                circleRectangle = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.sense * 2, mem.sense * 2))
                circleSurface = pygame.Surface(circleRectangle.size, pygame.SRCALPHA)
                pygame.draw.circle(circleSurface, (0,0,220,10), (mem.sense, mem.sense), mem.sense)
                gameDisplay.blit(circleSurface, circleRectangle)

        for mem in uSpecies:
            pygame.draw.circle(gameDisplay, mem.color, (mem.xPos, mem.yPos), mem.size)

        for f in food:
            pygame.draw.circle(gameDisplay, f.color, f.position, f.size)

        
        if hard == True:
            pygame.draw.rect(gameDisplay, (126,126,126), (0, 0, 950, mem.yPos - mem.sense))
            pygame.draw.rect(gameDisplay, (126,126,126), (0, mem.yPos + mem.sense, 950, display_height))
            pygame.draw.rect(gameDisplay, (126,126,126), (0, 0, mem.xPos - mem.sense, display_height))
            pygame.draw.rect(gameDisplay, (126,126,126), (mem.xPos + mem.sense, 0, 950, display_height))
            gameDisplay.blit(circleSurfaceHrd, circleRectangleHrd)

        pygame.draw.rect(gameDisplay, (255,255,255), (949, 0, (display_width - 949), display_height))
        pygame.draw.rect(gameDisplay, (0,0,0), (949, 0, 2, display_height))

        gameModeTextBox = TextBox("creative", 10, (1075,20), (0,0,0), "c", "LMLight.otf")
        nameTextBox = TextBox(name, 20, (1075,40), (0,0,0), "c", "LemonMilk.otf")

        foodPointsTextBox = TextBox("Food Points: ", 15, (965,100), (0,0,0), "l", "LemonMilk.otf")
        foodPointsTextBoxNum = TextBox(str(foodItemPoints), 15, (1075,99), (0,0,0), "l", "LMLight.otf")



        traitTxt = TextBox("Speed", 15, (965,150), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 165))
        traitQntTxt = TextBox(str(speciesSpeed), 15, (1072,185), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Stamina", 15, (965,250), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 265))
        traitQntTxt = TextBox(str(speciesStamina), 15, (1072,285), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Sense", 15, (965,350), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 365))
        traitQntTxt = TextBox(str(speciesSense), 15, (1072,385), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Memory", 15, (965,450), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 465))
        traitQntTxt = TextBox(str(speciesMemory), 15, (1072,485), (0,0,0), "c", "LemonMilk.otf")

        if len(uSpecies) > 0:
            traitTxt = TextBox("Health: " + str(int(uSpecies[0].stamina - uSpecies[0].dying)) + "/" + str(int(uSpecies[0].stamina)), 15, (965,550), (0,0,0), "l", "LemonMilk.otf")
        else:
            traitTxt = TextBox("Health: 0", 15, (965,550), (0,0,0), "l", "LemonMilk.otf")

        traitTxt = TextBox("Remaining: " + str(len(species) + len(uSpecies)) + "/12", 15, (965,600), (0,0,0), "l", "LemonMilk.otf")
        
        
        if foodCounter == 60:
            makeFood()
            foodCounter = 0

        pygame.display.update()

## -------------------------------------- Species Survival --------------------------------------
if speciesSurvival == True:

    speciesSpeed = 1
    speciesStamina = 150
    speciesSense = 100
    speciesMemory = 1

    if DNAslot1 == 'speed' or DNAslot2 == 'speed':
        speciesSpeed = 3
    if DNAslot1 == 'stamina' or DNAslot2 == 'stamina':
        speciesStamina = 250
    if DNAslot1 == 'sense' or DNAslot2 == 'sense':
        speciesSense = 125
    if DNAslot1 == 'memory' or DNAslot2 == 'memory':
        speciesMemory = 5

    for i in range(1,10):
        makeMember(speciesSpeed, speciesStamina, speciesSense, speciesMemory)
        
    while cont == False:
        clock.tick(60)
        foodCounter += 1
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cont = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx in range(965,1005) and my in range(165,205):
                    if speciesSpeed > 1:
                        speciesSpeed -= 0.5
                if mx in range(965 + 175,1005 + 175) and my in range(165,205):
                    if foodItemPoints > 0:
                        speciesSpeed += 0.5
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(265,305):
                    if speciesStamina > 1:
                        speciesStamina -= 5
                if mx in range(965 + 175,1005 + 175) and my in range(265,305):
                    if foodItemPoints > 0:
                        speciesStamina += 5
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(365,405):
                    if speciesSense > 1:
                        speciesSense -= 1
                if mx in range(965 + 175,1005 + 175) and my in range(365,405):
                    if foodItemPoints > 0:
                        speciesSense += 1
                        foodItemPoints -= 1


                if mx in range(965,1005) and my in range(465,505):
                    if speciesMemory > 1:
                        speciesMemory -= 1
                if mx in range(965 + 175,1005 + 175) and my in range(465,505):
                    if foodItemPoints > 0:
                        speciesMemory += 1
                        foodItemPoints -= 1

        

        for mem in species:

            mem.speed = speciesSpeed
            mem.sense = speciesSense
            mem.stamina = speciesStamina
            mem.memory = speciesMemory

            # if mem.intelligence == 1:

            mem.foodInRange = []
            mem.dying += 0.05

            if mem.dying > mem.stamina:
                species.remove(mem)

            else:
                if mem.justEaten != 0:
                    mem.justEaten -= 5
                
                mem.color = (0 + mem.dying, 0 + mem.dying + mem.justEaten, 0 + mem.dying)

                for storedFoodItem in mem.memoryBank:
                    distanceFromItem = (((mem.xPos - storedFoodItem.xPos)**2) + ((mem.yPos - storedFoodItem.yPos)**2))**(1/2)

                    if distanceFromItem <= mem.sense:
                        if storedFoodItem not in food:
                            mem.memoryBank.remove(storedFoodItem)
                    else:
                        mem.foodInRange.append(storedFoodItem)

                for f in food:
                    distance = (((mem.xPos - f.xPos)**2) + ((mem.yPos - f.yPos)**2))**(1/2)

                    if distance <= mem.size:
                        food.remove(f)
                        foodItemPoints += 1
                        mem.memberFood += 1
                        mem.justEaten = 100
                        mem.dying -= 100
                        if mem.dying < 0:
                            mem.dying = 0
                    elif distance <= mem.sense:
                        mem.foodInRange.append(f)
                
                if mem.foodInRange != []:
                    closest = mem.foodInRange[0]
                    closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)

                    for item in range(1, len(mem.foodInRange)):
                        itemDistance = (((mem.xPos - mem.foodInRange[item].xPos)**2) + ((mem.yPos - mem.foodInRange[item].yPos)**2))**(1/2)
                        if itemDistance < closestDistance:
                            closest = mem.foodInRange[item]   
                            closestDistance = (((mem.xPos - closest.xPos)**2) + ((mem.yPos - closest.yPos)**2))**(1/2)  

                    mem.xPos += ((closest.xPos - mem.xPos)/closestDistance)*((mem.speed)**(1/2))
                    mem.yPos += ((closest.yPos - mem.yPos)/closestDistance)*((mem.speed)**(1/2))

                    mem.dying += mem.speed*0.01
                
                if mem.memory > 0:
                    for item in mem.foodInRange:
                        if len(mem.memoryBank) < mem.memory:
                            if item not in mem.memoryBank:
                                mem.memoryBank.append(item)





        pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))
                    
        for mem in species:
            circleRectangle = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.sense * 2, mem.sense * 2))
            circleSurface = pygame.Surface(circleRectangle.size, pygame.SRCALPHA)
            pygame.draw.circle(circleSurface, (200,200,200,100), (mem.sense, mem.sense), mem.sense)
            gameDisplay.blit(circleSurface, circleRectangle)

        for mem in species:
            pygame.draw.circle(gameDisplay, mem.color, (mem.xPos, mem.yPos), mem.size)

        for f in food:
            pygame.draw.circle(gameDisplay, f.color, f.position, f.size)

        pygame.draw.rect(gameDisplay, (255,255,255), (949, 0, (display_width - 949), display_height))
        pygame.draw.rect(gameDisplay, (0,0,0), (949, 0, 2, display_height))

        gameModeTextBox = TextBox("creative", 10, (1075,20), (0,0,0), "c", "LMLight.otf")
        nameTextBox = TextBox(name, 20, (1075,40), (0,0,0), "c", "LemonMilk.otf")

        foodPointsTextBox = TextBox("Food Points: ", 15, (965,100), (0,0,0), "l", "LemonMilk.otf")
        foodPointsTextBoxNum = TextBox(str(foodItemPoints), 15, (1075,99), (0,0,0), "l", "LMLight.otf")



        traitTxt = TextBox("Speed", 15, (965,150), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 165))
        traitQntTxt = TextBox(str(speciesSpeed), 15, (1072,185), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Stamina", 15, (965,250), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 265))
        traitQntTxt = TextBox(str(speciesStamina), 15, (1072,285), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Sense", 15, (965,350), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 365))
        traitQntTxt = TextBox(str(speciesSense), 15, (1072,385), (0,0,0), "c", "LemonMilk.otf")

        traitTxt = TextBox("Memory", 15, (965,450), (0,0,0), "l", "LemonMilk.otf")
        traitImg = pygame.image.load('plusMinus.png')
        gameDisplay.blit(traitImg, (965, 465))
        traitQntTxt = TextBox(str(speciesMemory), 15, (1072,485), (0,0,0), "c", "LemonMilk.otf")
        
        
        if foodCounter == 60:
            makeFood()
            foodCounter = 0

        pygame.display.update()

# ------------------------------------------- Game Over Pygame Closer -----------------------------------------------
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()
