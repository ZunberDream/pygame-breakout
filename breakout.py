import pygame
import sys
import random

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
powerups = []
powerups_speed = 5; 

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

    for p in powerups[:]:
        if (paddle[0] <= p["x"] <= paddle[0] + 100 and paddle[1] <= p["y"] + 20 <= paddle[1] + 20):
            ball.append({"x": p["x"], "y": paddle[1] - 20, "speed_x": random.choice([-5, 5]), "speed_y": -5})
            powerups.remove(p)
        pygame.draw.circle(screen, (30, 144, 255), (p["x"], p["y"]), 20)
        p["y"] += powerups_speed
        if p["y"] > 600:
            powerups.remove(p)

    
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
        
        if (ball[i]["speed_y"] > 0 and paddle[0] <= ball[i]["x"] <= paddle[0] + 100 and
            paddle[1] - 10 <= ball[i]["y"] + 10 <= paddle[1] + 10):
            ball[i]["speed_y"] = -abs(ball[i]["speed_y"])
            ball[i]["y"] = paddle[1] - 11

        for brick in bricks[:]:
            if (brick[0] <= ball[i]["x"] <= brick[0] + brick_w and
                brick[1] <= ball[i]["y"] <= brick[1] + brick_h):
                bricks.remove(brick)
                ball[i]["speed_y"] = -ball[i]["speed_y"]
                break

    if(random.randint(1, 1000) == 1):
        powerups.append({"x": random.randint(50, 750), "y": 0})  
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()