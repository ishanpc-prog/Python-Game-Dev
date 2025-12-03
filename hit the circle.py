import pgzrun
import random 

WIDTH  = 500
HEIGHT = 500
TITLE  = "Hit the Circle"

circle = Actor("circle_small") #Actor is used to import the picture of the characters.
message = ""

def draw():
    screen.clear()
    screen.fill(color = (150,0,0))
    circle.draw()
    screen.draw.text(message,center= (400,10),fontsize = 25)

def place_circle():
    circle.x = random.randint(50,WIDTH-50)
    circle.y = random.randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if circle.collidepoint(pos):
        message = "Good Shot"
        place_circle()
    else:
        message = "Missed Shot"
place_circle()            

pgzrun.go()