import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Pikachu is getting chased by Ash for some reason."

pika = Actor("pikachu")
ash = Actor("alienal")

pika.pos =  200,200
ash.pos = 400,400

score = 0
gameover = False

def draw():
    screen.blit("backround_1",(0,0))
    pika.draw()
    ash.draw()
    screen.draw.text("Score: " + str(score),color = "black",topright = (350,50))
    if gameover == True:
        screen.fill("yellow")
        screen.draw.text("Times up.", color = "black", topleft = (10,10))
        screen.draw.text("Your score is " + str(score) + ". " + "Congratulations!!!", color = "black", topright = (350,110))

def pika_placement():
    pika.x = random.randint(70,430)
    pika.y = random.randint(70,430)

def times_up():
    global gameover 
    gameover = True

def update():
    global score
    if keyboard.left:
        ash.x = ash.x - 2
    if keyboard.right:
        ash.x = ash.x + 2
    if keyboard.up:
        ash.y = ash.y - 2
    if keyboard.down:
        ash.y = ash.y + 2
    pika_found = ash.colliderect(pika)
    if pika_found:
        score = score + 10
        pika_placement()
clock.schedule(times_up,60.0)
pgzrun.go()