import pygame, sys
from pygame.locals import *
import random, time
pygame.init()

FPS = 60
Frame = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
Screen_w = 400
Screen_H = 600
SPEED = 5
SCORE = 0
COINS = 0
COINS_SPEED = 5 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")


DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE) 
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,Screen_w-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_w - 40), 0)

class Сoin(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        rand_val = random.random()
        if rand_val < 0.6:
            self.value = 1
            self.color = GOLD
        elif rand_val < 0.9:
            self.value = 2
            self.color = (192, 192, 192)
        else:
            self.value = 5
            self.color = (255, 100, 100)
            
        image = pygame.image.load("coin.png")    
        self.image = pygame.transform.scale(image, (30, 30))
        color_surface = pygame.Surface((30,30))
        color_surface.fill(self.color)
        self.image.blit(color_surface, (0, 0), special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,Screen_w-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > Screen_H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, Screen_w - 40), 0)
    def respawn(self):
        self.assign_random_value()
        

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < Screen_w:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                 
P1 = Player()
E1 = Enemy()
C1 = Сoin()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:    
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, (255, 215, 0))

    DISPLAYSURF.blit(scores, (10, 10))  
    coin_rect = coin_text.get_rect(topright=(Screen_w - 10, 10))
    DISPLAYSURF.blit(coin_text, coin_rect)
        
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(BLUE)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    coin_collided = pygame.sprite.spritecollideany(P1, coins)
    if coin_collided:
        COINS += coin_collided.value 
        coin_collided.rect.top = 0
        coin_collided.rect.center = (random.randint(40, Screen_w - 40), 0)
    pygame.display.update()
    Frame.tick(FPS)
#________________________________________________________________________

"""
pygame.init()

W, H = 600, 640
CELL = 30
GRID = W // CELL
FPS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (160, 32, 240)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

snake = [[10, 10], [9, 10], [8, 10]]
direction = [1, 0]
score = 0
level = 1
speed = FPS - 5

foods = []
MAX_FOODS = 3
FOOD_LIFETIME = 10000


def check_boom(pos):
    return (pos[0] < 0 or pos[0] >= GRID or 
            pos[1] < 0 or pos[1] >= GRID or 
            pos in snake[1:])


def generate_food_weight():
    rand = random.random()
    
    if rand < 0.60:
        return 1, RED
    elif rand < 0.85:
        return 2, YELLOW
    else:
        return 3, PURPLE


def generate_food():
    while True:
        x = random.randint(0, GRID - 1)
        y = random.randint(0, GRID - 1)
        
        if [x, y] not in snake and not any(f['pos'] == [x, y] for f in foods):
            weight, color = generate_food_weight()
            return {
                'pos': [x, y],
                'weight': weight,
                'color': color,
                'spawn_time': pygame.time.get_ticks()
            }


def remove_expired_foods():
    current_time = pygame.time.get_ticks()
    return [f for f in foods if current_time - f['spawn_time'] < FOOD_LIFETIME]


for _ in range(MAX_FOODS):
    foods.append(generate_food())

running = True
while running:
    clock.tick(speed)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction[1] == 0:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction[1] == 0:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction[0] == 0:
                direction = [1, 0]
    
    foods = remove_expired_foods()
    
    while len(foods) < MAX_FOODS:
        foods.append(generate_food())
    
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    
    if check_boom(new_head):
        print(f"Game Over! Final Score: {score}")
        running = False
        continue
    
    snake.insert(0, new_head)
    
    food_eaten = None
    for food in foods:
        if new_head == food['pos']:
            food_eaten = food
            break
    
    if food_eaten:
        points = food_eaten['weight'] * 10
        score += points
        print(f"Съедена еда весом {points} очков! Всего: {score}")
        
        if score % 30 == 0:
            level += 1
            speed += 2
            print(f"Level {level}! Speed: {speed}")
        
        foods.remove(food_eaten)
        foods.append(generate_food())
        
    else:
        snake.pop()
    
    screen.fill(BLACK)
    
    for segment in snake:
        pygame.draw.rect(screen, WHITE, 
                        (segment[0] * CELL, segment[1] * CELL, CELL - 2, CELL - 2))
    
    current_time = pygame.time.get_ticks()
    for food in foods:
        pygame.draw.rect(screen, food['color'], 
                        (food['pos'][0] * CELL, food['pos'][1] * CELL, CELL - 2, CELL - 2))
        
        time_left = (FOOD_LIFETIME - (current_time - food['spawn_time'])) // 1000
        
        if time_left <= 5:
            timer_text = small_font.render(str(time_left), True, ORANGE)
            timer_x = food['pos'][0] * CELL + CELL // 4
            timer_y = food['pos'][1] * CELL - 15
            screen.blit(timer_text, (timer_x, timer_y))
        
        weight_text = small_font.render(f"x{food['weight']}", True, WHITE)
        weight_x = food['pos'][0] * CELL + 2
        weight_y = food['pos'][1] * CELL + 2
        screen.blit(weight_text, (weight_x, weight_y))
    
    score_text = font.render(f'Score: {score}  Level: {level}', True, WHITE)
    screen.blit(score_text, (10, H - 35))
    
    legend_y = 10
    legend_items = [
        (RED, "Normal (x1)"),
        (YELLOW, "Medium (x2)"),
        (PURPLE, "Bonus (x3)")
    ]
    for color, text in legend_items:
        pygame.draw.rect(screen, color, (10, legend_y, 20, 20))
        legend_text = small_font.render(text, True, WHITE)
        screen.blit(legend_text, (35, legend_y))
        legend_y += 25
    
    pygame.display.flip()

pygame.quit()
#__________________________________________________________________________

import pygame, sys
from pygame.locals import *
import random, time
import math
pygame.init()
def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()
    
    
    radius = 10
    color = (0, 0, 255)  
    tool = 'brush'  
    points = []
    shapes = []
    
    
    drawing = False
    start_pos = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  
                elif event.key == pygame.K_y:
                    color = (255, 255, 0)  
                elif event.key == pygame.K_w:
                    color = (255, 255, 255)
                elif event.key == pygame.K_p:
                    color = (255, 192, 203)  
                
                
                elif event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'square'
                elif event.key == pygame.K_5:
                        tool = 'right_triangle'  
                elif event.key == pygame.K_6:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_7:
                    tool = 'rhombus'  
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                
                
                elif event.key == pygame.K_c:
                    points = []
                    shapes = []
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if tool in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        drawing = True
                        start_pos = event.pos
                    else:
                        radius = min(50, radius + 1)
                elif event.button == 3:  
                    radius = max(1, radius - 1)
            
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing:
                    shapes.append((tool, start_pos, event.pos, color, radius))
                    drawing = False
            
            
            if event.type == pygame.MOUSEMOTION:
                if tool == 'brush':
                    points.append((event.pos, color, radius))
                elif tool == 'eraser':
                    points.append((event.pos, (0, 0, 0), radius))  
        
        
        screen.fill((0, 0, 0))

        for i in range(len(points) - 1):
            p1, c1, r1 = points[i]
            p2, c2, r2 = points[i + 1]
            pygame.draw.line(screen, c1, p1, p2, r1)
        
        
        for shape in shapes:
            s_tool, s_start, s_end, s_color, s_width = shape
            
            if s_tool == 'rectangle':
                
                x1, y1 = s_start
                x2, y2 = s_end
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(screen, s_color, rect, s_width)
            
            elif s_tool == 'circle':
                
                x1, y1 = s_start
                x2, y2 = s_end
                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                if r > 0:
                    pygame.draw.circle(screen, s_color, (x1, y1), r, s_width)
            elif s_tool == 'square':
                x1, y1 = s_start
                x2, y2 = s_end
                side = max(abs(x2-x1), abs(y2-y1))
                if x2 < x1:
                    side = -side
                rect = pygame.Rect(x1, y1, side, side)
                pygame.draw.rect(screen, s_color, rect, s_width)
            
            elif s_tool == 'right_triangle':
                x1, y1 = s_start
                x2, y2 = s_end
                points_triangle = [(x1, y1), (x2, y1), (x2, y2)]
                pygame.draw.polygon(screen, s_color, points_triangle, s_width)
            
            elif s_tool == 'equilateral_triangle':
                x1, y1 = s_start
                x2, y2 = s_end
                height = y2 - y1
                base = abs(height * 2 / math.sqrt(3))
                points_triangle = [
                    (x1, y1),  
                    (x1 - base/2, y2),  
                    (x1 + base/2, y2)
                ]
                pygame.draw.polygon(screen, s_color, points_triangle, s_width)
            
            elif s_tool == 'rhombus':
                x1, y1 = s_start
                x2, y2 = s_end
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                half_width = abs(x2 - x1) / 2
                half_height = abs(y2 - y1) / 2
                points_rhombus = [
                    (center_x, y1),  
                    (x2, center_y),
                    (center_x, y2),  
                    (x1, center_y)  
                ]
                pygame.draw.polygon(screen, s_color, points_rhombus, s_width)
                   
        
        if drawing and start_pos:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if tool == 'rectangle':
                x1, y1 = start_pos
                rect = pygame.Rect(min(x1, mouse_x), min(y1, mouse_y), 
                                  abs(mouse_x-x1), abs(mouse_y-y1))
                pygame.draw.rect(screen, color, rect, radius)
            
            elif tool == 'circle':
                x1, y1 = start_pos
                r = int(((mouse_x-x1)**2 + (mouse_y-y1)**2)**0.5)
                if r > 0:
                    pygame.draw.circle(screen, color, (x1, y1), r, radius)
        
            elif tool == 'square':
                x1, y1 = start_pos
                side = max(abs(mouse_x-x1), abs(mouse_y-y1))
                if mouse_x < x1:
                    side = -side
                rect = pygame.Rect(x1, y1, side, side)
                pygame.draw.rect(screen, color, rect, radius)
            
            elif tool == 'right_triangle':
                x1, y1 = start_pos
                points_triangle = [(x1, y1), (mouse_x, y1), (mouse_x, mouse_y)]
                pygame.draw.polygon(screen, color, points_triangle, radius)
            
            elif tool == 'equilateral_triangle':
                x1, y1 = start_pos
                height = mouse_y - y1
                base = abs(height * 2 / math.sqrt(3))
                points_triangle = [
                    (x1, y1),
                    (x1 - base/2, mouse_y),
                    (x1 + base/2, mouse_y)
                ]
                pygame.draw.polygon(screen, color, points_triangle, radius)
            
            elif tool == 'rhombus':
                x1, y1 = start_pos
                center_x = (x1 + mouse_x) / 2
                center_y = (y1 + mouse_y) / 2
                points_rhombus = [
                    (center_x, y1),
                    (mouse_x, center_y),
                    (center_x, mouse_y),
                    (x1, center_y)
                ]
                pygame.draw.polygon(screen, color, points_rhombus, radius)
        
        font = pygame.font.Font(None, 24)
        info = font.render(f'{tool.upper()} | Size: {radius}', True, (200, 200, 200))
        screen.blit(info, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)

main()
"""
