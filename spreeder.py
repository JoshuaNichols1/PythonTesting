import time
import pygame

pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)

inputf = open('input.txt', 'r')
a=[]
for line in inputf.readlines():
    line.split()
    line.strip()
    if line != '':
        a.append(line)
main_font = pygame.font.SysFont('arial', 50)
word = ''
for line in a:
    for c in line:
        if c != ' ':
            word += c
        else:
            print(word)
            WIN.fill(BLACK)
            words = main_font.render(f'{word}', 1, (255, 255, 255))
            WIN.blit(words, (WIDTH/2.5, HEIGHT/2.5))
            time.sleep(0.15)
            word = ''
            pygame.display.update()