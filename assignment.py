import time
import random
import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
low_red = (220, 0, 0)
low_green = (0, 220, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Maths Attack')

clock = pygame.time.Clock()

laserImg = pygame.image.load('laser.png')
shipImg = pygame.image.load('spaceship.png')
bgImg = pygame.image.load('bg.png')


def objects(img, x, y):
    gameDisplay.blit(img, (x, y))


def font(size):
    return pygame.font.Font('freesansbold.ttf', size)


def text_objects(text, color, size):
    font = pygame.font.SysFont(None, size)
    textSurface = font.render(text, font, color)
    return textSurface, textSurface.get_rect()


def center_write(text, color, size, x_more, y_more, num):
    if num == 'no':
        TextSurf, TextRect = text_objects(
            str(text), color, size)
        TextRect.center = (((display_width/2)-x_more),
                           ((display_height/2)-y_more))
        gameDisplay.blit(TextSurf, TextRect)
    else:
        TextSurf, TextRect = text_objects(
            str(text) + str(num), color, size)
        TextRect.center = (((display_width/2)-x_more),
                           ((display_height/2)-y_more))
        gameDisplay.blit(TextSurf, TextRect)


def game_message(message, x, y, color, size, num):
    font = pygame.font.SysFont(None, size)
    if num == 'no':
        text = font.render(message, True, color)
    else:
        text = font.render(message + str(num), True, color)
    gameDisplay.blit(text, (x, y))


def button(msg, fontsize, x, y, w, h, i, a):
    pygame.draw.rect(gameDisplay, a, (x, y, w, h))
    textSurf, textRect = text_objects(msg, black, fontsize)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def sides_guess(shape, sides_string):
    amount = ''
    current = ''
    stop = False

    thing_width = 100
    thing_height = 100
    thing_startx = ((display_width/2)-50)
    thing_starty = ((display_height/2)-200)

    def correct(sides, guess):
        if guess == sides:
            return 'Correct'
        else:
            return f'Incorrect, the correct amount of sides were {sides}'

    gameDisplay.blit(bgImg, (0, 0))

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    amount += '1'
                elif event.key == pygame.K_2:
                    amount += '2'
                elif event.key == pygame.K_3:
                    amount += '3'
                elif event.key == pygame.K_4:
                    amount += '4'
                elif event.key == pygame.K_5:
                    amount += '5'
                elif event.key == pygame.K_6:
                    amount += '6'
                elif event.key == pygame.K_7:
                    amount += '7'
                elif event.key == pygame.K_8:
                    amount += '8'
                elif event.key == pygame.K_9:
                    amount += '9'
                elif event.key == pygame.K_0:
                    amount += '0'
                elif event.key == pygame.K_BACKSPACE:
                    amount = amount[:-1]
                elif event.key == pygame.K_RETURN:
                    answer = correct(sides_string, amount)
                    stop = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_0:
                    amount = amount

        gameDisplay.fill(white)
        gameDisplay.blit(bgImg, (0, 0))
        center_write(f'How many sides does a {shape} have? ',
                     white, 60, 0, 240, 'no')
        if shape == 'Triangle':
            print('k')
        elif shape == 'Square':
            pygame.draw.rect(gameDisplay, low_red, [thing_startx, thing_starty,
                                                    thing_width, thing_height])
        center_write(amount, white, 60, 0, 0, 'no')
        if stop == True:
            center_write(answer, white, 50, 0, -60, 'no')
            pygame.display.update()
            time.sleep(3)
            game_loop(3, 0, True)
        pygame.display.update()
        clock.tick(60)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        center_write('Shape Protector', black, 60, 0, 0, 'no')

        button('GO!', 50, ((display_width/2)-90), 450, 200, 90, low_green,
               green)
        button('Quit the Game', 30, (display_width-150), 0, 150, 67.5, low_red,
               red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop(2, 0, False)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(60)


def game_loop(thingSpeed, shotnum, sidescorrect):
    x = ((display_width/2) - (113/2))
    y = (display_height - 108)

    x_change = 0
    y_change = 0

    ship_width = 113
    ship_height = 108
    laser_width = 58
    laser_height = 58

    laser_startx = x+113/4
    laser_starty = y-108/2
    laser_speed = 6
    shot = shotnum
    laser = False
    charge = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = thingSpeed
    thing_width = 100
    thing_height = 100

    gameDisplay.blit(bgImg, (0, 0))

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_e:
                    laser = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        if sidescorrect == False:
            sides_guess('Square', '4')
        x += x_change
        y += y_change
        gameDisplay.fill(white)
        gameDisplay.blit(bgImg, (0, 0))
        pygame.draw.rect(gameDisplay, white, [thing_startx, thing_starty,
                                              thing_width, thing_height])
        thing_starty += thing_speed
        objects(shipImg, x, y)
        if laser_starty < 0:
            laser = False
            laser_startx = x+(ship_width/4)
            laser_starty = y-(ship_height/2)
            if charge == 0:
                charge = 1
            else:
                charge = 0
        if laser == True:
            if charge == 1:
                gameDisplay.blit(
                    laserImg, (laser_startx, laser_starty))
                laser_starty -= laser_speed
            else:
                laser_starty -= laser_speed*2
        if laser_starty < 0:
            laser = False
            laser_startx = x+(ship_width/4)
            laser_starty = y-(ship_height/2)
            if charge == 0:
                charge = 1
            else:
                charge = 0

        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x + ship_width > display_width:
            x = display_width - ship_width
        if y + ship_height > display_height:
            y = display_height - ship_width
        if y + ship_height < (display_height - display_height/3):
            y = (display_height - display_height/3) - ship_height

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + ship_width > thing_startx and x + ship_width < thing_startx + thing_width:
                game_loop(3, 0, False)

        if laser_startx < thing_starty+thing_height:
            if laser_startx > thing_startx and laser_startx < thing_startx + thing_width or laser_startx + laser_width > thing_startx and x + laser_width < thing_startx + thing_width:
                if laser == True and charge == 1:
                    thing_starty = 0 - thing_height
                    thing_startx = random.randrange(0, display_width)

        game_message('Shapes Captured: ', 0, 0, white, 25, shot)
        game_message('Charge: ', display_width-84,
                     0, white, 25, charge)
        pygame.display.update()
        clock.tick(144)


game_intro()
quit()
