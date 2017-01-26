import pygame

pygame.init()

width=1000
height=1000
screen=pygame.display.set_mode((width,height))

def button(color,x, y, w, h, image,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, color , (x, y, w, h))
        if click[0]==1 and action!=0:
            action()
    else:
        pygame.draw.rect(screen, (0,56,89), (x, y, w, h))
        screen.blit(pygame.image.load(image), (x, y))

def insert_image(image, positionx, positiony):
    screen.blit(pygame.image.load(image),(positionx,positiony))

def exit():
    pygame.quit()
    quit()


def game_loop():
    game = True
    while game:
        insert_image('gameboard.png', 0, 0)
        button(color3, 1843, 2, 70, 63, 'pause_button.png',pause_loop)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

    pygame.display.update()
black=(0,0,0)
color1=(78,36,27)
color2=(37,48,38)
color3=(37,49,49)
def rules_screen():
    rules = True
    while rules:
        insert_image('rules1.png', 0, 0)
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button2.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen2()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button3.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen2()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button4.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen2()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button5.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen2()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button6.collidepoint(
                    pygame.mouse.get_pos()):
                rules_screen2()
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
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button1.collidepoint(
                    pygame.mouse.get_pos()):
                game_main_menu()
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
