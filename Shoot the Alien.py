import pgzrun
import random 

WIDTH  = 500
HEIGHT = 500
TITLE  = "Shoot the Alien"

alien_al = Actor("alienal") #Actor is used to import the picture of the characters.
message = ""

def draw():
    screen.clear()
    screen.fill(color = (150,0,0))
    alien_al.draw()
    screen.draw.text(message,center= (400,10),fontsize = 25)

def place_alien():
    alien_al.x = random.randint(50,WIDTH-50)
    alien_al.y = random.randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien_al.collidepoint(pos):
        message = "Good Shot"
        place_alien()
    else:
        message = "Missed Shot"
place_alien()            

pgzrun.go()