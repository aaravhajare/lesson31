import pygame
pygame.init()
white = (225,225,225)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Image")

image = pygame.image.load("ChatGPT Image May 9, 2025, 11_54_31 AM.png")

ds = (200,200)
P = (150,150)
image = pygame.transform.scale(image,ds)

while True:
    screen.fill(white)
    screen.blit(image, P)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()


    pygame.display.flip()
    clock.tick(45)