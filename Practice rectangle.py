import pygame 
pygame.init()
screen = pygame.display.set_mode([500,500])
running = True
while running:
    screen.fill((255,0,255))
    pygame.draw.rect(screen,(65,175,230),(120,200,100,200),30)
    pygame.draw.line(screen,(30,255,70),(120,200),(300,150),20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
# The screen shall be filled but with two round brackets