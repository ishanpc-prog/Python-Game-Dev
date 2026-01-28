import pgzero
import random
import time

WIDTH = 800
HEIGHT = 600
TITLE = "Connecting the satelites!!!"

s1 = []
lines = []
next_satelite = 0
start_time = 0
end_time = 0
total_time = 0
number_satelites = random.randint(5,16)

def create_satelite():
    global start_time
    for i in range(0,number_satelites):
        satelite = Actor("satelite")
        satelite.pos = random.randint(50,750),random.randint(50,550)
        s1.append(satelite)
    start_time = time.time()

def draw():
    global total_time
    screen.blit("space",(0,0))
    number = 1
    for satelite in s1:
        screen.draw.text(str(number),(satelite.pos[0],satelite.pos[1]+20))
        satelite.draw()
        number = number + 1 
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_satelite < number_satelites:
        total_time = time.time() - start_time