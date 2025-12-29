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
        