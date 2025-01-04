import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Bird properties
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
BIRD_X = 100
BIRD_Y = SCREEN_HEIGHT // 2
BIRD_GRAVITY = 1
BIRD_JUMP = -10

# Pipe properties
PIPE_WIDTH = 75
PIPE_HEIGHT = 600
PIPE_GAP = 200

# Load images
bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_img.fill(BLUE)
pipe_img = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
pipe_img.fill(GREEN)

# Bird class
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.velocity = 0
        self.top_pipe = pygame.Rect(self.x, self.y - BIRD_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT)
        self.bottom_pipe = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += BIRD_GRAVITY
        self.y += self.velocity
        self.top_pipe = pygame.Rect(self.x, self.y - BIRD_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT)
        self.bottom_pipe = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 450)
        self.top_pipe = pygame.Rect(x, 0, PIPE_WIDTH, self.height)
        self.bottom_pipe = pygame.Rect(x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= 5
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

# Game loop
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird.jump()

        screen.fill(WHITE)
        bird.update()
        for pipe in pipes:
            pipe.update()
            screen.blit(pipe_img, (pipe.x, 0))
            screen.blit(pipe_img, (pipe.x, pipe.bottom_pipe.y + PIPE_GAP))

        pygame.draw.rect(screen, BLUE, bird.top_pipe)
        pygame.draw.rect(screen, BLUE, bird.bottom_pipe)

        if bird.top_pipe.colliderect(pipe.top_pipe) or bird.bottom_pipe.colliderect(pipe.bottom_pipe):
            print("Collision detected!")
            break

        pygame.display.flip()
        clock.tick(30)  # Limit the frame rate to 30 FPS

if __name__ == "__main__":
    game_loop()
