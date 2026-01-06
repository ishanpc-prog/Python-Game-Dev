import pgzrun
import random 

WIDTH = 500
HEIGHT = 500
TITLE = "The bumblebee and the flower."

bee = Actor("bee")
flower = Actor("flower")

flower.pos = 200,200
bee.pos = 400,400

score = 0
gameover = False

def draw():
    screen.blit("backround_1",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft = (10,10))
    if gameover == True:
        screen.fill("yellow")
        screen.draw.text("Times up.", color = "black", topleft = (10,10))
        screen.draw.text("Your score is " + str(score) + ". " + "Congratulations!!!", color = "black", topright = (350,110))

def flower_placement():
    flower.x = random.randint(70,430)
    flower.y = random.randint(70,430)

def times_up():
    global gameover 
    gameover = True

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2
    if keyboard.right:
        bee.x = bee.x + 2
    if keyboard.up:
        bee.y = bee.y - 2
    if keyboard.down:
        bee.y = bee.y + 2
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score = score + 10
        flower_placement()
clock.schedule(times_up,60.0)
pgzrun.go()