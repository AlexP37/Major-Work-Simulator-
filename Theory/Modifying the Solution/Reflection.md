# Reflection

This major work is a program that I am extremely proud of. Every subtle UI choice was made with specific intent. The choices made with regards to how I display content to the screen in the most lag-free, pygame-friendly way are all precise. Further, the use of a modular programming with a hybrid of object oriented programming and sequential programming has allowed me to stick to my strengths and test the limits of what is possible. I feel that I have taken pygame to its extreme whilst staying in its comfort zone of stability, and have built a program thats intense level of comuptation, analysis and efficiency in the back-end is something that I can say I am proud of. Through this experience of the major work, and of developing a vast portfolio of programs, both python pygame and not, I feel that I have forged into a solid possition for progressing to the next stage in university. Some highlights of this specific project are outlined in-depth in the 'Justification of Coding' section, which i will imbed below for easy of reading. These highlights are my use of consistancy in terms of variables, line-saving measures with classes and functions, the use of modules and efficiency with classes and functions / modules.

--

<details>
  <summary>Justification of Coding (Click to Expand)</summary>
  
### Justification of Coding

Throughout this assignment a healthy combination of object oriented programing and sequential programing has been achieved in a way that allows pygame to run at its most efficient and for the user to experience engaging with the application in a seamless fashion. The use of members of the species as classes allows for the code to be maintained far easier and also saves on lines of code. It also allowed for the species to interact with the world themselfs and for their interaction to alter them. They too can alter themselves with this object oriented approach. Additionally, this approach allowed for the program to not worry about the number of members in a species nor the attributes they posses. All members function in the same way and the code treats them as 1 not as a million, allowing for pygame to process their information and display it in an efficient manor, whilst python's back-end takes care of the indivigual components and manorisms. Similarly, having food be a class allowed for the same simplicity of code design to occur for pygame, whilst all the data analysis and hevy lifting is handled by python, and even so, some of that heavy lifting is too aleviated. Having such complex classes and sub-routines means that from the players approach, the processes and display is simple, but behind the scenes, numerous decisions, calculations and complex bi-variat decisions are being made by the classes. The use of these classes reduces the complexity of the program from a maintainability perspective. "mem" is used to denote a single member of the species / Member() class (consistant through whole program) within for loops such as "for mem in species: " where mem can be used as "mem.dying" and "mem.speed" (other such consistant variables can also be found). The use of "mem" in this fashion occurs over 450 times in the code and thus saves thousands of lines of repeted code to access and change members had they not been a class. The member class as well as the function used to make the members and its implimentation within a for loop to create 9 members of the same species can be seen below.


```
species = []

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
        self.newLocationX = xPos
        self.newLocationY = yPos

        self.justEaten = 0
        self.dying = 0
      
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

for i in range(1,10):
    makeMember(speciesSpeed, speciesStamina, speciesSense, speciesMemory)
```


Beyond the classes, the use of functions / sub-routines / methods simplifies the code. At all places where proccesses such as displaying a text box or creating a species or food occurs, the sub-routine can be called. Common processes are found in only one place thus saving on lines of code and reducing the  complexity of the program from a maintainability perspective. For example, the display(self) function within the TextBox class is called each time a text box is used, which is extremely often. The display(self) function the only way of simplifying that process, a dedicated class exists for text box's so that they can be induvigually altered with ease. The class and function within relating to text box's can be seen bellow as well as a line of code with uses that implimentation. The implementation of the class TextBox and its imbeded function occur over 70 times throguh the program, saving over 1200 lines of code, and allowing for one small change to the way text box's display with a new update of pygame to be apply to all with ease.

```
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

heading = TextBox("Species Information", 100, (50,100), (0,0,0), "l", "LemonMilk.otf")
```

Further, the use of the pygame.draw sub-routine to display circles, lines, rectangles and more to the screen as well as pygame.font to render text to the screen is used prominantly in this program. This is to reduce the load times assosiated with images and the massive lag spikes. Adapting the the pygame library is an essential part of the code, as otherwise exesive delays in loading and lag that would cause the program to be unplayable would occur. Menu's, members, and more could all be displayed as images, but this has been reduced as much as possible in favour of the *in-house* pygame display functions. This has also made the resoultion and pixel smoothness hightened compared to images and the toll that many images being *blitted* to the screen can cause. The code below uses the pygame.draw fucntionality to render to the screen the scanners, members bodies and the food pellets to the screen without the need for image processing *blitting*. The pygame.Rect and pygame.Surface sub-routines are also taken advantage of the format the locations with ease and allow for lag-free RGBA (use of alpha to have transparency of objects, in this case the sensor circle which is semi-transparent at a factor of 100/255). Further, the use of the Member() class returns with the "mem" reperesenting a Member (object) in the list of members "species". Similarly, but with food we see "f" which is a Food object in the list of all food pellet objects "food".


```
for mem in species:
    circleRectangle = pygame.Rect((mem.xPos, mem.yPos), (0, 0)).inflate((mem.sense * 2, mem.sense * 2))
    circleSurface = pygame.Surface(circleRectangle.size, pygame.SRCALPHA)
    pygame.draw.circle(circleSurface, (200,200,200,100), (mem.sense, mem.sense), mem.sense)
    gameDisplay.blit(circleSurface, circleRectangle)

for mem in species:
    pygame.draw.circle(gameDisplay, mem.color, (mem.xPos, mem.yPos), mem.size)

for f in food:
    pygame.draw.circle(gameDisplay, f.color, f.position, f.size)
```

</details>

--

As this project is a prototype development, there is always things that could have been dont better, such as the inclusiong of inter-member communication and another fresh and different gamemode. Perhaps these are some tasks I can tackle in reminisce one day. Other things I would improve upon is some time managment. I feel compared to some other projects, my time managment was slightly below my expectation of myself although this could be a result of the lockdowns and the uncertnty surrounding many aspects of school life at the current time.

Overall, I am very pleased with the engaging level of my program and feel that it has capabilities to be further expaneded upon in the areas I set out for it to; research, education and entertainment. I am also very proud of the complexity of the back-end and how that translates to a clean and ellegant front-end user experience.

To many more projects to come!