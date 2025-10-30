import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music Player')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)


music_folder = 'music'
if not os.path.exists(music_folder):
    os.makedirs(music_folder)

playlist = sorted([f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))])
current_index = 0
status = "Stopped"

def play():
    global status
    if playlist:
        pygame.mixer.music.load(os.path.join(music_folder, playlist[current_index]))
        pygame.mixer.music.play()
        status = "Playing"

def stop():
    global status
    pygame.mixer.music.stop()
    status = "Stopped"

def next_track():
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        if status == "Playing":
            play()

def prev_track():
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        if status == "Playing":
            play()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                prev_track()
    
    
    if status == "Playing" and not pygame.mixer.music.get_busy():
        next_track()
    
    
    screen.fill(WHITE)
    
    
    if playlist:
        song = playlist[current_index][:30]
        text = font.render(f"Track: {song}", True, BLACK)
        screen.blit(text, (50, 100))
        
        info = font.render(f"{current_index + 1}/{len(playlist)}", True, BLACK)
        screen.blit(info, (50, 150))
    else:
        text = font.render("No songs in 'music' folder", True, BLACK)
        screen.blit(text, (50, 100))
    
    
    status_text = font.render(f"Status: {status}", True, BLACK)
    screen.blit(status_text, (50, 200))
    
    
    controls = font.render("SPACE-Play | S-Stop | N-Next | P-Prev", True, BLACK)
    screen.blit(controls, (50, 300))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
