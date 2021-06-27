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

class Member:
    def __init__(self, color, xPos, yPos, radius, shapeType):
        self.color = color
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.shapeType = shapeType

        self.speed = 1
    
    def display(self):
        if self.shapeType == "c":
            pygame.draw.circle(gameDisplay, self.color, (self.xPos, self.yPos), self.radius)
            TextBox("Speed: " + str(self.speed), 20, (1190,18), (0,0,0), "r", "LMLight.otf")
            TextBox("Stamina: " + str(self.speed), 20, (1190,42), (0,0,0), "r", "LMLight.otf")
        elif self.shapeType == "h":
            self.location = [((self.xPos + (self.radius * math.sin(math.pi/6))), (self.yPos - (self.radius * math.cos(math.pi/6)))), ((self.xPos + self.radius), self.yPos), ((self.xPos + (self.radius * math.sin(math.pi/6))), (self.yPos + (self.radius * math.cos(math.pi/6)))), ((self.xPos - (self.radius * math.sin(math.pi/6))), (self.yPos + (self.radius * math.cos(math.pi/6)))), ((self.xPos - self.radius), self.yPos), ((self.xPos - (self.radius * math.sin(math.pi/6))), (self.yPos - (self.radius * math.cos(math.pi/6))))]
            pygame.draw.polygon(gameDisplay, self.color, self.location)
        elif self.shapeType == "t":
            self.location = [(self.xPos, (self.yPos - self.radius)),((self.xPos + (self.radius * math.sin(math.pi/3))),(self.yPos + (self.radius * math.cos(math.pi/3)))),((self.xPos - (self.radius * math.sin(math.pi/3))),(self.yPos + (self.radius * math.cos(math.pi/3))))]
            pygame.draw.polygon(gameDisplay, self.color, self.location)

foodItems = [Member((0,175,0), random.randint(200, 1000), random.randint(100, 700), 5, "t")]
for i in range(1,20):
    xFoodLoc = random.randint(100, 1100)
    yFoodLoc = random.randint(50, 750)
    for i in foodItems:
        while (i.xPos - 40 > xFoodLoc > i.xPos - 40) & (i.yPos - 40 > yFoodLoc > i.yPos - 40):
            xFoodLoc = random.randint(200, 1000)
            yFoodLoc = random.randint(100, 700)

    food = Member((0,175,0), xFoodLoc, yFoodLoc, 5, "t")
    foodItems.append(food)

population1 = [Member((0,0,255), 20, 20, 10, "c")]
population1Scanners = [Member((200,200,255), 20, 20, 50, "c")]

# for i in range(1,11):
#     populi = Member((0,0,255), 20, (20 + 76*i), 10, "c")
#     populiScanner = Member((200,200,255), 20, (20 + 76*i), 50, "c")
#     population1.append(populi)
#     population1Scanners.append(populiScanner)

populiScanner = Member((200,200,255), 20, 20, 50, "c")
populi = Member((0,0,255), 20, 20, 10, "c")

while cont == False:
    clock.tick(60)
    print(str(int(clock.get_fps())))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            cont = True
            end = True
            pygame.quit()
            pygame.font.quit()
            quit()
        mx, my = pygame.mouse.get_pos()

        if 1000 < mx < 1080 and 160 < my < 175 and event.type == pygame.MOUSEBUTTONUP:
            print("placeholder")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                movementX += 1
            if event.key == pygame.K_s:
                movementY += 1
            if event.key == pygame.K_a:
                movementX += -1
            if event.key == pygame.K_w:
                movementY += -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movementX -= 1
            if event.key == pygame.K_s:
                movementY -= 1
            if event.key == pygame.K_a:
                movementX -= -1
            if event.key == pygame.K_w:
                movementY -= -1
    populi.xPos += movementX
    populi.yPos += movementY


    gameDisplay.fill((255,255,255))

    populiScanner.xPos = populi.xPos
    populiScanner.yPos = populi.yPos
    populiScanner.display()
    populi.display()
    # for i in population1Scanners:
    #     i.xPos = population1[population1Scanners.index(i)].xPos
    #     i.yPos = population1[population1Scanners.index(i)].yPos
    #     i.display()
    # for i in population1:
    #     i.display()
    for i in foodItems:
        i.display()

    pygame.display.update()

# Game Over
print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()