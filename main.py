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
  
    pygame.display.update()
    clock.tick(45)
