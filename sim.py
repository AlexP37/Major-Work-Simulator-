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
def makeMember():
    memSize = 15
    memColor = (0,0,0)
    memSpeed = 5
    memStamina = 1
    memSense = 100
    memXPos = random.randrange(15,950 - 15)
    memYPos = random.randrange(15,display_height - 15)
    memMemory = 50
    memIntelligence = 1

    species.append(Member(memSize, memColor, memSpeed, memStamina, memXPos, memYPos, memSense, memMemory, memIntelligence))

def makeFood():
    foodSize = 3
    foodColor = (0,0,255)
    foodXPos = random.randrange(15,950 - 15)
    foodYPos = random.randrange(15,display_height - 15)

    food.append(FoodPiece(foodSize, foodXPos, foodYPos, foodColor))

for i in range(1,10):
    makeMember()

foodCounter = 0

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
textBoxClear("Enter", 300, (display_width / 2, display_height / 2), (0,0,0))
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
            textBoxClear("Enter", 320, (display_width / 2, display_height / 2), (0,0,0))
            if event.type == pygame.MOUSEBUTTONDOWN or mouseDown == True:
                onPlayButton = True
                mouseDown = True
                gameDisplay.fill((255,255,255))
                textBoxClear("Enter", 320, (display_width / 2, display_height / 2), (0,100,0))
            if event.type == pygame.MOUSEBUTTONUP and mouseDown == True:
                if onPlayButton == True:
                    cont = True
                mouseDown = False
                gameDisplay.fill((255,255,255))
        else:
            gameDisplay.fill((255,255,255))
            textBoxClear("Enter", 300, (display_width / 2, display_height / 2), (0,0,0))
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
            if 150 < mx < 1090:
                if 215 < my < 300:
                    end = True
                    speciesSurvival = True
            if 150 < mx < 1090:
                if 365 < my < 445:
                    end = True
                    uVworld = True
            if 150 < mx < 1090:
                if 515 < my < 595:
                    end = True
                    creative = True

    pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))

    heading = TextBox("Species Simulator", 100, (50,100), (0,0,0), "l", "LemonMilk.otf")
    heading.display()


    title1 = TextBox("Species Survival", 100, (150,250), (50,50,50), "l", "LMLight.otf")
    title1.display()


    title2 = TextBox("U vs The World", 100, (150,400), (50,50,50), "l", "LMLight.otf")
    title2.display()


    title3 = TextBox("Creative Mode", 100, (150,550), (50,50,50), "l", "LMLight.otf")
    title3.display()

    pygame.display.update()



## -------------------------------------- Nameing --------------------------------------
naming = True
while naming == True:
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
                naming =true
                pygame.quit()
                pygame.font.quit()
                quit()
            if event.key == pygame.K_d:
                naming = True
                pygame.quit()
                pygame.font.quit()
                quit()

    heading = TextBox("Name", 100, (50,100), (0,0,0), "l", "LemonMilk.otf")

    pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))

    pygame.display.update()


## -------------------------------------- Creative --------------------------------------
cont = False
while cont == False and creative == True:
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

    

    for mem in species:

        # if mem.intelligence == 1:

        mem.foodInRange = []
        mem.dying += 0.05

        if mem.dying > 150:
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
    
    
    
    if foodCounter == 60:
        makeFood()
        foodCounter = 0

    pygame.display.update()


# Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()