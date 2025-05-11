import pygame as p 
p.init()
red = (255,0,0)

clock = p.time.Clock()

screen = p.display.set_mode((800,600))

p.display.set_caption("YUDHA JEET")

image = p.image.load("ChatGPT Image May 9, 2025, 11_54_31 AM.png")

ds = (500,300)
P = (200,200)

image = p.transform.scale(image,ds)

while True:
    screen.fill(red)
    screen.blit(image,P)

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

    p.display.flip()
    clock.tick(10)