import pgzrun 

WIDTH = 500
HEIGHT= 500

def draw():
    screen.clear()
    rect = Rect((0,0),(500,500))
    screen.draw.filled_rect(rect,"blue")
    screen.draw.circle((250,250),150,"black")
    screen.draw.circle((180,180),20,"black")
    screen.draw.circle((325,180),20,"black")
    screen.draw.line((180,285),(325,285),"black")
pgzrun.go()    