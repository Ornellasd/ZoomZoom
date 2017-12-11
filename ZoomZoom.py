import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

 
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Zoom Zoom Zoom')
clock = pygame.time.Clock()

tankImg = pygame.image.load('tank.png')


def car(x,y):
    gameDisplay.blit(tankImg,(x,y))
    
x = (display_width * 0.45)
y = (display_height * 0.65)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
   
