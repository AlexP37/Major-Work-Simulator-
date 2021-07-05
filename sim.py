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

species = []
def makeMember():
    memSize = 15
    memColor = (0,0,0)
    memSpeed = 1
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

while cont == False:
    clock.tick(60)
    foodCounter += 1


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
            if 250 < mx < 350:
                if 250 < my < 350:
                    cont = True

    


    for mem in species:

        if mem.intelligence == 1:

            mem.foodInRange = []

            for storedFoodItem in mem.memoryBank:
                if storedFoodItem not in food:
                    mem.memoryBank.remove(storedFoodItem)
                else:
                    mem.foodInRange.append(storedFoodItem)

            for f in food:
                distance = (((mem.xPos - f.xPos)**2) + ((mem.yPos - f.yPos)**2))**(1/2)

                if distance <= mem.size:
                    food.remove(f)
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
                mem.xPos += (closest.xPos - mem.xPos)/closestDistance
                mem.yPos += (closest.yPos - mem.yPos)/closestDistance
            
            if mem.memory > 0:
                for item in mem.foodInRange:
                    if len(mem.memoryBank) < mem.memory:
                        if item not in mem.memoryBank:
                            mem.memoryBank.append(item)

                



    pygame.draw.rect(gameDisplay, (255,255,255), (0, 0, display_width, display_height))
    pygame.draw.rect(gameDisplay, (0,0,0), (949, 0, 2, display_height))
    for mem in species:
        pygame.draw.circle(gameDisplay, mem.color, (mem.xPos, mem.yPos), mem.size)
    for f in food:
        pygame.draw.circle(gameDisplay, f.color, f.position, f.size)
    if foodCounter == 60:
        makeFood()
        foodCounter = 0

    pygame.display.update()


# Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()