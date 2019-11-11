import sys
import pygame

# Initialize game details
pygame.init()
displayInfo = pygame.display.Info()
screen = pygame.display.set_mode(
    (displayInfo.current_w, displayInfo.current_h), pygame.FULLSCREEN
)
pygame.display.set_caption("Muazzam Kekik")
clock = pygame.time.Clock()

# Set background color
screen.fill((35, 35, 35))

# Put a header to game
font = pygame.font.SysFont("papyrus", 192)
text = font.render("Muazzam Kekik", True, (255, 1, 0))
screen.blit(text, ((displayInfo.current_w - text.get_width()) // 2, 0))

# Draw the gameframe

# Draw the bricks
bricks = []
brick_color = (255, 255, 255)
row_num = 8
col_num = 5 
offset_x = (displayInfo.current_w - row_num * 120) / 2
offset_y = 20
for row in range(row_num):
    for col in range(col_num):
        bricks.append(pygame.Rect(row*120 + offset_x, col*35 + offset_y, 100, 30))

for brick in bricks:
    pygame.draw.rect(screen, brick_color, brick)

# Draw the paddle
paddle_color = (235, 235, 235) # Light Grey

    # Paddle sizes
x, y = 120, 40
vel = 5
x_start = 50
y_start = displayInfo.current_h - 75
pygame.draw.rect(screen, paddle_color, (x_start, y_start, x, y))

# Event listener loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_q
        ):
            pygame.quit()
            sys.exit()


    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        if(x_start + 170 < displayInfo.current_w):
            vel = 5
            x_start += vel
            
    if key[pygame.K_LEFT]:
        if(x_start > 50):  
            vel = -5
            x_start += vel
           
    
    screen.fill((35, 35, 35))
    pygame.draw.rect(screen, paddle_color, (x_start, y_start, x, y))
    for brick in bricks:
        pygame.draw.rect(screen, (255, 255, 255), brick)
  
    pygame.display.update()
    clock.tick(45)
