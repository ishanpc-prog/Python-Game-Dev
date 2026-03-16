import pgzrun
import random
WIDTH = 1200
HEIGHT = 700
TITLE = "Tha healthy eating"

score = 0
items = ["bee","appleed","isopizza"]
item = Actor(random.choice(items))
item.pos = random.randint(50,1050),0
basket = Actor("alienal")
basket.pos = 300,550

def draw():
    screen.clear()
    basket.draw()
    item.draw()
    screen.draw.text("The score is " + str(score), color = "white", topleft = (10,10))

def update():
    global item
    global score
    item.y = item.y + 7
    if keyboard.left:
        basket.x = basket.x - 20
    if keyboard.right:
        basket.x = basket.x + 20

    if basket.colliderect(item):
        if item.image == "appleed":
            score = score + 10 
        if item.image == "bee":
            score = score - 10
        if item.image == "isopizza":
            score = score - 10
        item = Actor(random.choice(items))
        item.pos = random.randint(50,1050),0
    if item.y > HEIGHT:
        item = Actor(random.choice(items))
        item.pos = random.randint(50,1050),0
pgzrun.go()