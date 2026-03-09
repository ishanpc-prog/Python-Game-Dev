import pgzrun
import random

WIDTH = 800
HEIGHT = 800
TITLE = "The Recycling Games"

score = 0
items = ["bee","satellite","flower"]
item = Actor(random.choice(items))
item.pos = random.randint(50,550),0
trashbin = Actor("alienal")
trashbin.pos = 300,550

def draw():
    screen.clear()
    trashbin.draw()
    item.draw()
    screen.draw.text("The score is " + str(score), color = "white", topleft = (10,10))

def update():
    global item
    global score
    item.y = item.y + 4
    if keyboard.left:
        trashbin.x = trashbin.x - 2
    if keyboard.right:
        trashbin.x = trashbin.x + 2
    if trashbin.colliderect(item):
        if item.image == "bee":
            score = score + 10 
        if item.image == "satellite":
            score = score - 10
        if item.image == "flower":
            score = score - 10
        item = Actor(random.choice(items))
        item.pos = random.randint(50,550),0
    if item.y > HEIGHT:
        item = Actor(random.choice(items))
        item.pos =random.randint(50,550),0   
pgzrun.go()