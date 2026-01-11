import pygame
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: pygame.version.ver")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS Limiting
    timer = pygame.time.Clock()
    dt = 0

    # Game loop starts here
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")

        dt = timer.tick(60) / 1000

        # Keep this at the end always
        pygame.display.flip()


if __name__ == "__main__":
    main()
