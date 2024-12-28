
import pygame
from guy import *

pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

guy_left = Guy()
guy_left.rect.x = 200
guy_left.rect.y = 500
guy_left_list = pygame.sprite.Group()
guy_left_list.add(guy_left)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("black")  # Fill the display with a solid color
   
    guy_left_list.draw(screen) # draw player
    
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)