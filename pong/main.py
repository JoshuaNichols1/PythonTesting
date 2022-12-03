import pygame
import os
import time
import random

pygame.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter Tutorial')

PLAYER_PADDLE = pygame.image.load(os.path.join('pong/assets', 'player.png'))
ENEMY_PADDLE = pygame.image.load(os.path.join('pong/assets', 'player.png'))
BALL = pygame.transform.scale(pygame.image.load(os.path.join('pong/assets', 'ball.png')), (8,8))
BG = pygame.transform.scale(pygame.image.load(os.path.join('pong/assets', 'background-black.png')), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
    
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = PLAYER_PADDLE
        self.mask = pygame.mask.from_surface(self.ship_img)

class Enemy(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = ENEMY_PADDLE
        self.mask = pygame.mask.from_surface(self.ship_img)

class Ball(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = BALL
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, vel):
        self.y += vel
        self.x += vel

def main():
    FPS = 240
    run = True
    level = 0
    lives = 3
    main_font = pygame.font.SysFont('arial', 50)
    lost_font = pygame.font.SysFont('arial', 60)

    enemy_vel = 5
    
    player_vel = 5
    
    ball_vel = 6
    
    enemy = Enemy(0, HEIGHT/2)
    player = Player(WIDTH-enemy.get_width(), (HEIGHT/2 - enemy.get_width()/2))
    enemy = Enemy(0, (HEIGHT/2 - player.get_width()/2))
    ball = Ball(WIDTH/2 - 4, HEIGHT/2 -4)
    
    clock = pygame.time.Clock()
    
    lost = False
    lost_count = 0
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        
        # for enemy in enemies:
        #     enemy.draw(WIN)
        
        player.draw(WIN)
        
        enemy.draw(WIN)
        
        ball.draw(WIN)
        
        lives_lable = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        level_lable = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        
        WIN.blit(lives_lable, (10, 10))
        WIN.blit(level_lable, (WIDTH-level_lable.get_width() - 10, 10))
        
        if lost:
            lost_lable = lost_font.render("You lost!!", 1, (255, 255, 255))
            WIN.blit(lost_lable, (WIDTH/2 - lost_lable.get_width()/2, 350))
        
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        if lives <= 0:
            lost = True
        
        if lost:
            if lost_count > FPS * 3:
                pygame.QUIT()
                run = False
            else:
                continue
            time.sleep(FPS*3)
            pygame.QUIT()
            run = False
        
        # if len(enemies) == 0:
        #     level += 1
        #     wave_length += 5
        #     for i in range(wave_length):
        #         enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100))
        #         enemies.append(enemy)
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
            elif keys[pygame.K_ESCAPE]:
                run = False
                pygame.QUIT()
        if keys[pygame.K_w] and player.y - player_vel > 0: #forward
            player.y -= player_vel
        elif keys[pygame.K_UP] and player.y - player_vel > 0: #forward
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #backwards
            player.y += player_vel
        elif keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT: #backwards
            player.y += player_vel
        # if keys[pygame.K_a] and player.x - player_vel > 0: #left
        #     player.x -= player_vel
        # if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #right
        #     player.x += player_vel
        up_or_down = ["u", "d"]
        choose = random.choice(up_or_down)
        if choose == "u" and enemy.y - enemy_vel > 0:
            enemy.y -= enemy_vel
        elif choose == "d" and enemy.y + enemy_vel + enemy.get_height() < HEIGHT:
            enemy.y += enemy_vel
        
        # if enemy.y + enemy.get_height() > HEIGHT:
        #     lives -= 1
        #     enemies.remove(enemy)
main()