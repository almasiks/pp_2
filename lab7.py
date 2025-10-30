import pygame
import sys
import math
import time

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mickey Clock')

WHITE = (255, 255, 255)

mickey_face = pygame.image.load('base_micky.jpg')
mickey_face = pygame.transform.scale(mickey_face, (width, height))

right_hand = pygame.image.load('right_hand.png')
left_hand = pygame.image.load('left_hand.png')

right_hand = pygame.transform.scale(right_hand, (150, 150))
left_hand = pygame.transform.scale(left_hand, (150, 150))


right_hand = pygame.transform.rotate(right_hand, 180)
left_hand = pygame.transform.rotate(left_hand, 180)

clock = pygame.time.Clock()

def blit_rotate(surf, image, pos, angle):    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=pos).center)
    surf.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    screen.blit(mickey_face, (0, 0))

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    center = (width // 2, height // 2)

    
    left_angle = -seconds * 6  
    blit_rotate(screen, left_hand, center, left_angle)

    
    right_angle = -minutes * 6
    blit_rotate(screen, right_hand, center, right_angle)

    pygame.display.flip()
    clock.tick(60)