import pygame
pygame.init()
events=pygame.event.get()
width=1000
height=1000
screen=pygame.display.set_mode((width,height))

boot= pygame.image.load('Boot-1-offense-mode.png')
boot2= pygame.image.load('Boot-2-offense-mode.png')
boot3= pygame.image.load('Boot-3-offense-mode.png')
gameboard= pygame.image.load('gameboard.png')

def button(color,p_x,p_y,width,height,image,loop, events):
    buttons=pygame.draw.rect(screen,color,[p_x,p_y,width,height])
    if image != None:
        screen.blit(pygame.image.load(image),(p_x,p_y))
    for event in events:
        if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and buttons.collidepoint(pygame.mouse.get_pos()):
            loop()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def insert_image(image, positionx, positiony):
    screen.blit(pygame.image.load(image),(positionx,positiony))

def exit():
    pygame.quit()
    quit()


def game_loop():
    x = 199
    y = 109
    gameExit = False
    while not gameExit:
        screen.blit(gameboard, (0, 0))
        button((0, 0, 0), 1450, 0, 50, 50, None, pause_loop, events)
        if len(player.boats) < 4:
            if len(player.boats) < 1:
                screen.blit(boot, (x, y))
            elif len(player.boats) < 3 and player.boats.count(boot2) < 2:
                screen.blit(boot2, (x, y))
            elif player.boats.count(boot3) < 1:
                screen.blit(boot3, (x, y))
        elif len(player2.boats) < 4:
            if len(player2.boats) < 1:
                screen.blit(boot, (x, 637))
            elif len(player2.boats) < 3 and player.boats.count(boot2) < 2:
                screen.blit(boot2, (x, 608))
            elif player2.boats.count(boot3) < 1:
                screen.blit(boot3, (x, 579))
        move_key = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if x < 902 and x > 199:
                if move_key[pygame.K_RIGHT]:
                    x = x + 37
                    p = x
                elif move_key[pygame.K_LEFT]:
                    x -= 37
            elif x == 199:
                if move_key[pygame.K_RIGHT]:
                    x += 37
            elif x == 902:
                if move_key[pygame.K_LEFT]:
                    x -= 37
            new_pos = (x, y)
            if len(player.boats) < 4:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    if len(player.boats) == 0:  # and player.boats.count(boot) < 1:
                        player.boats.append((boot, new_pos))
                    elif len(player.boats) < 3:  # and player.boats.count(boot2) < 2:
                        player.boats.append((boot2, new_pos))
                    elif player.boats.count(boot2) < 1:
                        player.boats.append((boot3, new_pos))
            elif len(player2.boats) < 4:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if len(player2.boats) == 0:  # and player.boats.count(boot) < 1:
                        player2.boats.append((boot, (x, 637)))
                    elif len(player2.boats) < 3:  # and player.boats.count(boot2) < 2:
                        player2.boats.append((boot2, (x, 608)))
                    elif player2.boats.count(boot2) < 1:
                        player2.boats.append((boot3, (x, 579)))

        for boat in player.boats:
            screen.blit(boat[0], boat[1])
        for boat in player2.boats:
            screen.blit(boat[0], boat[1])

        pygame.display.flip()


class Player:
    def __init__(self, name):
        self.name = name
        self.boats = []

player = Player('test')
player2 = Player('test2')



class Boat:
    def __init__ (self, img, pos):
        self.image= img
        self.position= pos
























def rules_screen():
    rules = True
    while rules:
        insert_image('rules1.png', 0, 0)
        button((0,0,0),800, 400, 100, 50, rules_screen2,events)
        pygame.display.update()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def rules_screen2():
    rules = True
    while rules:
        insert_image('rules2.png', 0, 0)
        button0 = pygame.draw.rect(screen, color2, [100, 910, 50, 40])
        pygame.draw.rect(screen, color1, [90, 900, 10, 73])
        pygame.draw.rect(screen, black, [80, 905, 10, 60])
        pygame.draw.rect(screen, black, [70, 915, 20, 30])
        pygame.draw.rect(screen, color2, [60, 930, 50, 15])
        insert_image('pijl2.png', 50, 885)
        button1 = pygame.draw.rect(screen, color3, [1813, 2, 100, 50])
        button2 = pygame.draw.rect(screen, color2, [1650, 910, 50, 40])
        button3 = pygame.draw.rect(screen, color1, [1700, 900, 10, 73])
        button4 = pygame.draw.rect(screen, black, [1710, 905, 10, 60])
        button5 = pygame.draw.rect(screen, black, [1710, 915, 20, 30])
        button6 = pygame.draw.rect(screen, color2, [1710, 930, 50, 15])
        insert_image('pijl1.png', 1650, 900)
        pygame.display.update()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button0.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button2.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button3.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button4.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button5.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button6.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def rules_screen3():
    rules = True
    while rules:
        insert_image('rules3.png', 0, 0)
        button0 = pygame.draw.rect(screen, color2, [100, 910, 50, 40])
        pygame.draw.rect(screen, color1, [90, 900, 10, 73])
        pygame.draw.rect(screen, black, [80, 905, 10, 60])
        pygame.draw.rect(screen, black, [70, 915, 20, 30])
        pygame.draw.rect(screen, color2, [60, 930, 50, 15])
        insert_image('pijl2.png', 50, 885)
        button1 = pygame.draw.rect(screen, color3, [1813, 2, 100, 50])
        button2 = pygame.draw.rect(screen, color2, [1650, 910, 50, 40])
        button3 = pygame.draw.rect(screen, color1, [1700, 900, 10, 73])
        button4 = pygame.draw.rect(screen, black, [1710, 905, 10, 60])
        button5 = pygame.draw.rect(screen, black, [1710, 915, 20, 30])
        button6 = pygame.draw.rect(screen, color2, [1710, 930, 50, 15])
        insert_image('pijl1.png', 1650, 900)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button1.collidepoint(
                    pygame.mouse.get_pos()):
                game_main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button0.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen2()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button2.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen4()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button3.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen4()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button4.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen4()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button5.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen4()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button6.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen4()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def rules_screen4():
    rules = True
    while rules:
        insert_image('rules4.png', 0, 0)
        button0 = pygame.draw.rect(screen, color3, [1813, 2, 100, 50])
        button1 = pygame.draw.rect(screen, color2, [100, 910, 50, 40])
        pygame.draw.rect(screen, color1, [90, 900, 10, 73])
        pygame.draw.rect(screen, black, [80, 905, 10, 60])
        pygame.draw.rect(screen, black, [70, 915, 20, 30])
        pygame.draw.rect(screen, color2, [60, 930, 50, 15])
        insert_image('pijl2.png', 50, 885)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button0.collidepoint(
                    pygame.mouse.get_pos()):
                game_main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button1.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def see_highscores():
    see_highscores = True
    while see_highscores:
        insert_image('highscore.png', 0, 0)
        button0 = pygame.draw.rect(screen, color3, [1813, 2, 100, 50])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button0.collidepoint(
                    pygame.mouse.get_pos()):
                game_main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def pause_loop():
    game=True
    while game:
        insert_image('pauses1.png', 0, 0)
        insert_image('pause_scherm.png', 540, 200)
        button((0, 89, 90), 600, 353, 180, 65,'pause1.png',)
        button((0, 89, 90), 800, 353, 180, 65,'pause3.png',rules_screen)
        button((0, 89, 90), 1000, 353, 180, 65,'pause2.png',game_loop)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game= False