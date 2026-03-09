import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = "Tha healthy eating"

score = 0
items = ["burger1","apple1","pizza1"]
item = Actor(random.choice(items))
item.pos = random.randint(50,550),0
basket = Actor("basket1")
basket.pos = 300,550

def draw():
    screen.clear()
    screen.fill(color = (0,120,120))
    basket.draw()
    item.draw()
    screen.draw.text("The score is " + str(score), color = "black", topleft = (10,10))

def update():
    global item
    global score
    item.y = item.y + 4
    if keyboard.left:
        basket = basket - 2
    if keyboard.right:
        basket = basket + 2
    if basket.colliderect(item):
        if item.image == "apple1":
            score = score + 10 
        if item.image == "pizza1":
            score = score - 10
        if item.image == "burger1":
            score = score - 10