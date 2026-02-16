import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 1000
TITLE = "The star connection!!!"

s1 = []
lines = []
next_star = 0
start_time = 0
end_time = 0
total_time = 0
number_stars = random.randint(5,16)

def create_star():
    global start_time
    for i in range(0,number_stars):
        star = Actor("tharealstar")
        star.pos = random.randint(50,750),random.randint(50,550)
        s1.append(star)
    start_time = time.time()

def draw():
    global total_time
    screen.blit("space",(0,0))
    number = 1
    for star in s1:
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+20))
        star.draw()
        number = number + 1 
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_star < number_stars:
        total_time = time.time() - start_time 
        screen.draw.text("Your time is " + str(total_time) + "!",topleft = (50,50))
    else:
        screen.draw.text("Your time is " + str(total_time) + "!",topleft = (50,50))

def on_mouse_down(pos):
    global next_star
    global lines
    if next_star < number_stars:
        if s1[next_star].collidepoint(pos):
            if next_star:
                lines.append((s1[next_star-1].pos,s1[next_star].pos))
            next_star = next_star + 1
    else:
        lines = []
        next_star = 0

create_star()

pgzrun.go()