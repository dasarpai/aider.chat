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
BIRD_JUMP_STRENGTH = -10

# Pipe properties
PIPE_WIDTH = 75
PIPE_GAP = 150
PIPE_SPEED = 3

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird Game")

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
        self.velocity = BIRD_JUMP_STRENGTH

    def update(self):
        self.velocity += BIRD_GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.top_pipe = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_pipe = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

    def draw(self):
        screen.blit(pipe_img, (self.top_pipe.x, self.top_pipe.y))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (self.bottom_pipe.x, self.bottom_pipe.y))

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0

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

        # Check for collisions
        if bird.y + BIRD_HEIGHT >= SCREEN_HEIGHT or bird.y <= 0:
            running = False

        for pipe in pipes:
            if (bird.x < pipe.top_pipe.right and bird.x > pipe.top_pipe.left) or \
               (bird.x < pipe.bottom_pipe.right and bird.x > pipe.bottom_pipe.left):
                if (bird.y < pipe.top_pipe.bottom or bird.y + BIRD_HEIGHT > pipe.bottom_pipe.top):
                    running = False

        # Check for scoring
        if pipes[0].x + PIPE_WIDTH < bird.x:
            score += 1
            pipes.pop(0)
            pipes.append(Pipe())

        # Draw everything
        screen.fill(WHITE)
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
