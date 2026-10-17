import pygame

class Orb:
    gravity = 9.8

    def __init__(self, x, y):
        self.position = (x, y)
        self.velocity = (0.0, 0.0)
        self.acceleration = (0.0, 0.0)

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.acceleration[1] -= gravity


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()