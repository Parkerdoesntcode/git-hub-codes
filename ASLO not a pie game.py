import pygame
import os
x=10
y=10
speedX=4
speedY=4
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((1280, 720))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        x=x+speedX
        y=y+speedY
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('mario.gif'), (x,y,20, 20))
        screen.blit(get_image('mario.gif'), (x,y,18, 33))
        pygame.display.flip()
        clock.tick(60)


        if x<=0 or x>=1020:
                speedX=speedX*-1.1
        if y<=0 or y>=460:
                speedY=speedY*-1.1
