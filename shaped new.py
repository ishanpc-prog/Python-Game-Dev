import pgzrun 

WIDTH = 500
HEIGHT= 500

def draw():
    screen.clear()
    screen.draw.line((50,50),(350,50),"red")
    screen.draw.line((50,50),(50,350),"green")
    rect = Rect((100,100),(200,80))
    screen.draw.rect(rect,"red")
    screen.draw.filled_rect(rect,"red")
    screen.draw.circle((200,150),20,"green")
    screen.draw.filled_circle((200,150),20,"green")
pgzrun.go()    