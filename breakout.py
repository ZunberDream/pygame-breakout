import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("breakout")
clock = pygame.time.Clock()

paddle = (0, 500)
paddle_speed = 10;
ball = [{"x": 100, "y": 200, "speed_x": 5, "speed_y": 5}]
brick_rows = 10          
brick_cols = 12
brick_w = 60          
brick_h = 20           
brick_gap = 5          
brick_offset_x = 10    
brick_offset_y = 10    

bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        x = brick_offset_x + col * (brick_w + brick_gap)
        y = brick_offset_y + row * (brick_h + brick_gap)
        bricks.append((x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    running = False
       
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle = (paddle[0] - paddle_speed, paddle[1])
    if keys[pygame.K_RIGHT]:
        paddle = (paddle[0] + paddle_speed, paddle[1])

    screen.fill((0, 0, 0))
    
    for brick in bricks:
        pygame.draw.rect(screen, (200, 200, 200), (brick[0], brick[1], brick_w, brick_h))

    
    pygame.draw.rect(screen, (255, 255, 255), (paddle[0], paddle[1], 100, 20))

    for i in range(len(ball)):
        pygame.draw.circle(screen, (255, 0, 0), (ball[i]["x"], ball[i]["y"]), 10)
        ball[i]["x"] += ball[i]["speed_x"]
        ball[i]["y"] += ball[i]["speed_y"]

        if ball[i]["x"] <= 0 or ball[i]["x"] >= 800:
            ball[i]["speed_x"] = -ball[i]["speed_x"]
        if ball[i]["y"] <= 0:
            ball[i]["speed_y"] = -ball[i]["speed_y"]
        if ball[i]["y"] >= 600:
            running = False
        
        if (paddle[0] - 10 <= ball[i]["x"] <= paddle[0] + 100 + 10 and paddle[1] - 10 <= ball[i]["y"] + 10 <= paddle[1] + 5):
            ball[i]["speed_y"] = -abs(ball[i]["speed_y"])
            ball[i]["y"] = paddle[1] - 10

        for brick in bricks[:]:
            if (brick[0] <= ball[i]["x"] <= brick[0] + brick_w and
                brick[1] <= ball[i]["y"] <= brick[1] + brick_h):
                bricks.remove(brick)
                ball[i]["speed_y"] = -ball[i]["speed_y"]
                break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()