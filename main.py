import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # "delta time", specific for game dev
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)    
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()   # refreshes the screen
        dt = clock.tick(60) / 1000  # framerate to 60 FPS
        

if __name__ == "__main__":
    main()
