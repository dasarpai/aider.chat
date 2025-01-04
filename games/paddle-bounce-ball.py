import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Paddle properties
paddle_width, paddle_height = 100, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - paddle_height - 10
paddle_speed = 5

# Ball properties
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 3
ball_speed_y = 3

# Bricks properties
brick_width, brick_height = 60, 20
bricks = []
for i in range(5):
    for j in range(10):
        bricks.append(pygame.Rect(j * (brick_width + 5) + 30, i * (brick_height + 5) + 30, brick_width, brick_height))

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= width - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y
    if ball_y >= height - ball_radius:
        pygame.quit()
        sys.exit()

    # Ball collision with paddle
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle.colliderect(pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)):
        ball_speed_y = -ball_speed_y

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y

    # Clear screen
    screen.fill(black)

    # Draw paddle and ball
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
