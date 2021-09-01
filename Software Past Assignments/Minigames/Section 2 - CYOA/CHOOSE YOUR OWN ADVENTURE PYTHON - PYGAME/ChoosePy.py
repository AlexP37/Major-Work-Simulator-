#Initialization
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
pygame.display.set_caption('Choose Your Own Adventure')
clock = pygame.time.Clock()
gameDisplay.fill((255,255,255))
#Functions
def textBoxBlack(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

def textBoxWhite(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (255,255,255)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

def makeGame():
    print("Game Initialised")
    gameDisplay.fill((0,0,0))
    pygame.display.update()










class Room:

    # this section sets up what happens when we create a new room
    def __init__(self, id, story, opt1_id, opt1_txt, opt2_id, opt2_txt, opt3_id, opt3_txt):
        self.id = id
        self.story = story
        self.opt1_id = opt1_id
        self.opt1_txt = opt1_txt
        self.opt2_id = opt2_id
        self.opt2_txt = opt2_txt
        self.opt3_id = opt3_id
        self.opt3_txt = opt3_txt

rooms = []

f = open("story.txt")

# read in each line of the file
for l in f:
    # split the file on the pipes "|"
    line = l.split("|")

    # create a new instance of the Room class
    room = Room(
        int(line[0]), line[1],
        int(line[2]), line[3],
        int(line[4]), line[5],
        int(line[6]), line[7])

    # add the room to the array of rooms
    rooms.append(room)

count = 1

def load_room(room_id):
    global rooms
    global count

    img = pygame.image.load(str(room_id) + '.png')
    gameDisplay.blit(img, (15,0))
    gameDisplay.blit(img, (485,0))

    storyText = rooms[room_id].story
    storyText2 = ""
    heightOfText = 25
    textInc = 1
    storyText3 = ""
    storyTextList = []
    newI = 0
    current = 0
    for i in range (0, len(storyText)):
        storyTextList.append(storyText[i])
        if i % 45 in range(0,20):
            if storyTextList[i] == " ":
                if i - newI not in range(0,10):
                    textBoxWhite(storyText[newI:i], 15, (300,heightOfText), (0,0,0))
                    newI = i
                    heightOfText = heightOfText + 25

    textBoxWhite(storyText[newI:-1] + storyText[-1], 15, (300,heightOfText), (0,0,0))

    # This section checks if we will print all the options or not.
    # If the opt_txt is only a "-" we don't print the option.
    count = 3

    if rooms[room_id].opt3_txt.strip() == "-":
        count = 2
    if rooms[room_id].opt2_txt.strip() == "-":
        count = 1
    
    if rooms[room_id].opt1_txt.strip() != "-":
        textBoxWhite((rooms[room_id].opt1_txt).replace("\n", ""), 10, ((300/count),500), (0,0,0))
    if rooms[room_id].opt2_txt.strip() != "-":
        textBoxWhite((rooms[room_id].opt2_txt).replace("\n", ""), 10, ((900/count),500), (0,0,0))
    if rooms[room_id].opt3_txt.strip() != "-":
        textBoxWhite((rooms[room_id].opt3_txt).replace("\n", ""), 10, ((1500/count),500), (0,0,0))


# set the starting room to 0
room_id = 0

ethicScore = 0
completedRoomId = 0
ethicalColor = (0,0,0)
# run the whole game
while room_id != -1:
    clock.tick(60)
    gameDisplay.fill((255,255,255))
    load_room(room_id)
    pygame.draw.line(gameDisplay, (0,0,0), (0,400), (600,400))
    pygame.draw.line(gameDisplay, (0,0,0), ((600/count),400), ((600/count),600))
    pygame.draw.line(gameDisplay, (0,0,0), (((600/count) * 2),400), (((600/count) * 2),600))
    if room_id == 13:
        ethicScore = 60
    elif room_id == 12:
        ethicScore = 80
    elif room_id == 10:
        ethicScore = 100
    elif room_id == 2:
        ethicScore = 50
    elif room_id == 3:
        ethicScore = 70
    elif room_id == 3:
        ethicScore = 70
    elif room_id == 5:
        ethicScore = 30
    elif room_id == 1:
        ethicScore = 30
    elif room_id == 6:
        completedRoomId = 6
        ethicScore = 15
    elif room_id == 8:
        ethicScore = 10
        completedRoomId = 8
    if room_id == 4:
        if completedRoomId == 6:
            ethicScore = 25
        if completedRoomId == 8:
            ethicScore = 20
    if 0 < ethicScore < 36:
        ethicalColor = (255,0,0)
    elif 36 < ethicScore < 56:
        ethicalColor = (255,255,0)
    elif 56 < ethicScore < 76:
        ethicalColor = (0,0,255)
    elif ethicScore > 76:
        ethicalColor = (0,255,0)
    if room_id == 7:
        textBoxWhite(("Your Ethics Score: " + str(ethicScore)), 50, (300,200), (ethicalColor))
    print(ethicScore)
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
            if 400 < my < 600:
                if count == 1:
                    room_id = rooms[room_id].opt1_id
                if count == 2:
                    if 0 < mx < 300:
                        room_id = rooms[room_id].opt1_id
                    else:
                        room_id = rooms[room_id].opt2_id
                if count == 3:
                    if 0 < mx < 200:
                        room_id = rooms[room_id].opt1_id
                    elif 200 < mx < 400:
                        room_id = rooms[room_id].opt2_id
                    else:
                        room_id = rooms[room_id].opt3_id
    pygame.display.update()

print("Awaiting End")
pygame.quit()
pygame.font.quit()
quit()