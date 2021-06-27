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
pygame.display.set_caption('Hangman')

clock = pygame.time.Clock()

def makeGame():
    print("Game Initialised")
    gameDisplay.fill((0,0,0))
    pygame.display.update()

def textBox(text, size, position, color):
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, color, (255,255,255)) 
    textRect = text.get_rect()
    textRect.center = position
    gameDisplay.blit(text, textRect) 

mode = 0
gameDisplay.fill((255,255,255))
pygame.draw.line(gameDisplay, (0,0,0), (300,0), (300,600))
pygame.draw.line(gameDisplay, (0,0,0), (300,300), (340,300))
pygame.draw.line(gameDisplay, (0,0,0), (560,300), (600,300))

textBox('2 Player', 50, (150, 300), (0,0,0))
textBox('1 Player', 50, (450, 300), (0,0,0))
textBox('Quick Play', 30, (450, 150), (0,0,0))
textBox('Choose Category', 30, (450, 450), (0,0,0))

cont = False
gameMode = "quick"

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
            cont = True
            if mx < 300:
                mode = 1
            else:
                if my > 300:
                    gameMode = "choose"

    pygame.display.update()

gameDisplay.fill((255,255,255))
pygame.draw.line(gameDisplay, (0,0,0), (300,0), (300,600))
pygame.draw.line(gameDisplay, (0,0,0), (0,300), (600,300))
pygame.display.update()

def ct(text, loc):
    font = pygame.font.Font('freesansbold.ttf', 50) 
    text = font.render(text, True, (0, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (loc)
    gameDisplay.blit(text, textRect) 

ct("Animals", (150, 150))
ct("Places", (450, 150))
ct("Food", (150, 450))
ct("Movies", (450, 450))

cont = False
Animals = ["Monkey", "Cat", "Dog", "Cow", "Sheep", "Lion", "Tiger", "Lizard", "Rhino", "Hippo", "Birds", "Horse", "Leopard", "Snake", "Possum", "Ant", "Frog", "Python", "Crocodile", "Kangaroo", "Piglet", "Lamb", "Gorilla", "Fish", "Shark", "Whale", "Turtle", "Salmon", "Tuna", "Dolphin", "Seal", "Duck", "Cicada", "Cricket", "Echidna", "Anteater", "Sloth", "Zebra", "Deer", "Elephant", "Platypus", "Wombat", "Beaver", "Emu", "Eagle", "Rabbit", "Mosquito", "Aardvark"]
Food = ["Banana", "Apple", "Pizza", "Pie", "Steak", "Sausage", "Tomatoes", "Beetroot", "Letus", "Cabbage", "Sushi", "Seafood", "Pork", "Curry", "Chicken", "Burger", "Cookie", "Pasta", "Lasagne", "Linguine", "Yogurt", "Sandwich", "Cheese", "Avocado", "Chips", "Egg", "Pretzel", "Orange", "Mango", "Carrot", "Berries", "Chocolate", "Taco", "Salad", "Salsa", "Onion", "Nuts", "Potatoes", "Nachos", "Fig", "Tofu", "Rice", "Dip", "Toast", "Bread", "Honey", "Cake", "Calzone", "Penut", "Schnitzel"]
Places = ["London", "Sydney", "York", "Paris", "China", "Russia", "Hollywood", "Seattle", "Europe", "Asia", "Brazil", "Melbourne", "Perth", "Denver", "Virginia", "Shanghai", "Berlin", "Dublin", "Austria", "Australia", "Spain", "Wellington", "Tokyo", "Geneva", "Sweeden", "Switzerland", "Manchester", "Belgium", "Holand", "Disneyland", "Disneyworld", "India", "France", "Montana", "Darwin", "Canada", "Pyramids", "Colosseum", "Kyiv", "Ukraine", "Moscow", "Antarctica", "Greenland", "Iceland", "Chernobyl"]
Movies = ["Avengers", "Gladiator", "Braveheart", "Parasite", "Inception", "Titanic", "Avitar", "Thor", "Psycho", "Fargo", "Jaws", "Batmna", "Mulan", "Tag", "Ted", "Deadpool", "Aladdin", "Frozen", "Alien", "Argo", "Maleficent", "Cars", "Jumanji", "Gravity", "Skyfall", "Cinderella", "Divergent", "Ratatouille", "Madagascar", "Interstellar", "Oblivion", "Transformers", "It", "Ghostbusters", "Rocky", "Up", "Irishman", "Cats", "Incredibles", "Lorax", "Robocop", "Venom", "Sonic", "Wolverine", "Pixels", "Hulk", "Superman", "Rambo", "Taken"]
words = ["Chair", "Brick", "Plant", "Window", "Fence", "Speaker", "Light", "Laptop", "Keyboard", "Pineapple", "Bag", "Book", "Glasses", "Watch", "Keychain", "Phone", "Wallet", "Pencil", "Eraser", "Dogs", "Cats", "Lizard", "Magpie", "Muppets", "Application", "Folder", "Door", "Calculator", "Australia", "India", "Python", "Alphabet", "Coffee", "Liberty", "Statue", "Mountain", "Page", "Google", "Cardboard", "Program", "White", "Lemon", "Blueberry", "Magnet", "Science", "Bin", "Musical", "Movie", "Atlas", "Clock", "London", "Plane", "Robbery", "Heist", "Christmas", "Mars", "Neptune", "Mesh", "Tarp", "Poem", "Medieval", "Crossbow", "Cricket", "Furniture", "Bagpipes", "Banjo", "Jazz", "Myth", "Rhythmic", "gymnast", "International", "Germany", "United", "Shelf", "Beer", "Bear", "Lion", "Ape", "April", "March", "Drummer", "Beetroot", "Dune", "Deer", "Muffler" "Paper", "Company", "Snake", "Spain", "Tree", "Wooden", "School", "Team", "Dream", "Experiment", "Royal", "Leaf", "Icicle", "Banana", "Assess", "Scissors", "Extraterrestrial", "Eyelevel", "Fox", "Exercise"]

if gameMode == "choose":
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
                cont = True
                if mx < 300:
                    words = Animals
                    if my > 300:
                        words = Food
                else:
                    words = Places
                    if my > 300:
                        words = Movies
        pygame.display.update()

makeGame()

def twoPlayerI():
    global word
    cont = False
    word = ""
    lnEx = False
    font = pygame.font.Font('freesansbold.ttf', 50) 
    text = font.render("Please Type Word", True, (255, 255, 255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (300, 100)
    gameDisplay.blit(text, textRect)

    font = pygame.font.Font('freesansbold.ttf', 20) 
    text = font.render("Press 'Enter' When Complete (Maximum 10 Letters)", True, (255, 255, 255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (300, 160)
    gameDisplay.blit(text, textRect)

    def tp(size, text):
        font = pygame.font.Font('freesansbold.ttf', size) 
        text = font.render(text, True, (255, 255, 255), (0,0,0)) 
        textRect = text.get_rect()
        textRect.center = (300, 500)
        gameDisplay.blit(text, textRect)

    tp(40, "Your Word: " + word + "|")
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
                if event.key == pygame.K_RETURN:
                    if word == "":
                        font = pygame.font.Font('freesansbold.ttf', 15) 
                        text = font.render("Your Word Must Have at Least 1 Letter", True, (255, 0, 0), (0,0,0)) 
                        textRect = text.get_rect()
                        textRect.center = (300, 200)
                        gameDisplay.blit(text, textRect)
                    else:
                        with open('search.txt') as file:
                            contents = file.read()
                            if word in contents:
                                print ('word found')
                                cont = True
                            else:
                                print ('word not found')
                                font = pygame.font.Font('freesansbold.ttf', 15) 
                                text = font.render("Word not found in Dictionary", True, (255, 0, 0), (0,0,0)) 
                                textRect = text.get_rect()
                                textRect.center = (300, 240)
                                gameDisplay.blit(text, textRect)
                elif event.key == pygame.K_BACKSPACE:
                    word = word[:-1]
                else:
                    if chr(event.key) in alphabet:
                        if len(word) != 10:
                            letter = chr(event.key)
                            word = word + letter
                        else:
                            font = pygame.font.Font('freesansbold.ttf', 15) 
                            text = font.render("Letter Limit Reached", True, (255, 0, 0), (0,0,0)) 
                            textRect = text.get_rect()
                            textRect.center = (300, 220)
                            gameDisplay.blit(text, textRect)
                pygame.draw.rect(gameDisplay, (0,0,0), (0,400,600,200))
                tp(40, "Your Word: " + word + "|")
        pygame.display.update()

            
rem = 7

def incor():
    font = pygame.font.Font('freesansbold.ttf', 100) 
    text = font.render("Lives: " + str(rem), True, (255, 255, 255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (300, 100)
    gameDisplay.blit(text, textRect)

end = False

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guesses = []
random.shuffle(words)
word = words[5]
if mode == 1:
    twoPlayerI()
    makeGame()
chars = list(word.lower())
print(chars)
rev = []

characters = 0

for i in chars:
    characters = characters + 1
    rev.append("_ ")

def dashes():
    size = 50
    if word == "Extraterrestrial":
        size = 40
    pygame.draw.rect(gameDisplay, (0,0,0), (0,450,600,100))
    text = " "
    for i in rev:
        text = text + i
    font = pygame.font.Font('freesansbold.ttf', size) 
    text = font.render(text, True, (255, 255, 255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (300, 500)
    gameDisplay.blit(text, textRect)

dashes()
incor()
finished = False
guessed = ""

def g():
    font = pygame.font.Font('freesansbold.ttf', 20) 
    text = font.render("Guesses: " + guessed, True, (255, 255, 255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (300, 175)
    gameDisplay.blit(text, textRect)

g()

while end == False:
    clock.tick(60)
    draw = False
    fin = True
    for i in rev:
        if i == "_ ":
            fin = False

    if fin == True and finished == False:
        finished = True
        font = pygame.font.Font('freesansbold.ttf', 100) 
        text = font.render('You Win!', True, (0, 0, 255)) 
        textRect = text.get_rect()
        textRect.center = (300, 300)
        gameDisplay.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            pygame.quit()
            pygame.font.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
                pygame.quit()
                pygame.font.quit()
                quit()
            if finished == False:
                choice = chr(event.key)
                print(choice)
                if choice in alphabet:
                    if choice not in guesses:
                        guesses.append(choice)
                        print(guesses)
                        guessed = ""
                        for i in guesses:
                            guessed = guessed + i + ", "
                        g()
                        if choice not in chars:
                            draw = True
                            rem = rem - 1
                            print(rem)
                        if choice in chars:
                            for i in range(0, characters):
                                if chars[i] == choice:
                                    rev[i] = choice + " "
                            dashes()
                    incor()
    if rem == 0 and finished == False:
        finished = True
        font = pygame.font.Font('freesansbold.ttf', 100) 
        text = font.render('You Loose', True, (255, 0, 0)) 
        textRect = text.get_rect()
        textRect.center = (300, 300)
        gameDisplay.blit(text, textRect)
        
        font = pygame.font.Font('freesansbold.ttf', 25) 
        text = font.render("The word was: " + word, True, (0, 0, 255)) 
        textRect = text.get_rect()
        textRect.center = (300, 360)
        gameDisplay.blit(text, textRect)

    pygame.display.update()

print("Awaiting End")

while end == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    end = True
                    pygame.quit()
                    pygame.font.quit()
                    quit()

pygame.quit()
pygame.font.quit()
quit()