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

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += BIRD_GRAVITY
        self.y += self.velocity

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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Update game objects
        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.x + PIPE_WIDTH < 0:
                pipes.pop(0)
                pipes.append(Pipe(SCREEN_WIDTH))

        # Check for collisions
        if bird.y <= 0 or bird.y >= SCREEN_HEIGHT - BIRD_HEIGHT:
            running = False
        for pipe in pipes:
            if (bird.x < pipe.top_pipe.right and bird.x + BIRD_WIDTH > pipe.top_pipe.left) or \
               (bird.x < pipe.bottom_pipe.right and bird.x + BIRD_WIDTH > pipe.bottom_pipe.left):
                if (bird.y < pipe.top_pipe.bottom or bird.y + BIRD_HEIGHT > pipe.bottom_pipe.top):
                    running = False

        # Draw everything
        screen.fill(WHITE)
        screen.blit(bird_img, (bird.x, bird.y))
        for pipe in pipes:
            pygame.draw.rect(screen, GREEN, pipe.top_pipe)
            pygame.draw.rect(screen, GREEN, pipe.bottom_pipe)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
