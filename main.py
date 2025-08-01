# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    

    

    #Object groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Assign containers to their classes
    Player.containers = (updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        
        updateable.update(dt)
        #Player.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        #Player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) /1000



    


if __name__ == "__main__":
    main()
