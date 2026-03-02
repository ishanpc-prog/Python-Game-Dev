import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = "The Recycling Games"

score = 0
items = ["paper2","wineglas","bulbli"]
item = Actor(random.choice(items))
item.pos = random.randint(50,550),0
trashbin = Actor("trashbin")
trashbin.pos = 300,550

def draw():
    screen.clear()
    screen.fill(color = (0,120,120))
    trashbin.draw()
    item.draw()
    screen.draw.text("The score is " + str(score), color = "black", topleft = (10,10))

def update():
    global item
    global score
    item.y = item.y + 4
    if keyboard.left:
        trashbin = trashbin - 2
    if keyboard.right:
        trashbin = trashbin + 2
    if trashbin.colliderect(item):
        if item.image == "paper2":
            score = score + 10 
        if item.image == "wineglas":
            score = score - 10
        if item.image == "bulbli":
            score = score - 10