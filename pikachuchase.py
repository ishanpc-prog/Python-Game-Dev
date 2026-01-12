import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Pikachu is getting chased by Ash for some reason."

pika = Actor("pikachu")
ash = Actor("bee")

pika.pos =  200,200
ash.pos = 400,400

score = 0
gameover = False

def draw():
    screen.blit("backround_1",(0,0))
    pika.draw()
    ash.draw()
    screen.draw.text("Score: " + str(score),color = "black",topright = (350,50))

pgzrun.go()