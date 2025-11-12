import pgzrun 
WIDTH = 500
HEIGHT = 500
def draw():
    screen.clear()
    screen.draw.line((50,50),(250,50),"red")
    screen.draw.line((50,50),(50,250),"red")
    screen.draw.line((50,250),(250,250),"red")
    screen.draw.line((250,250),(250,50),"red")
pgzrun.go()