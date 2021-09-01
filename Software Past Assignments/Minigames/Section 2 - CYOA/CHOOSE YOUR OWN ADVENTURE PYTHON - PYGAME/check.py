f = open("story.txt")
p = 0
maxP = 0
line = ""

for l in f:
    line = line + l

for i in range(0,len(line)):
    p = p + 1
    if maxP < p:
        maxP = p
    if line[i] == " ":
        p = 0
    if line[i] == "|":
        p = 0
    if line[i] == "\n":
        p = 0

print(maxP)