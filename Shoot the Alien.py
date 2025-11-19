import pgzrun
import random 

WIDTH  = 500
HEIGHT = 500
TITLE  = "Shoot the Alien"

alien_al = Actor("AlienAl") #Actor is used to import the picture of the characters.
message = ""

def draw():
    screen.clear()
    screen.fill(color = (150,0,0))
pgzrun.go()    