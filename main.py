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


# Event listener loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_q
        ):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            # implement mouse handling here

    pygame.display.update()
    clock.tick(45)
