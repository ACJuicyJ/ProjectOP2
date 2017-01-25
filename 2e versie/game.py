import pygame
import functions
pygame.init()

width = 1551
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.update()


def Game():
    game = True
    while game:
        functions.insert_image('menu.png', 0,0)
        functions.button((0, 89, 90), 651, 300, 200, 70, 'button3.png', functions.game_loop)
        functions.button((0, 89, 90), 651, 400, 200, 70, 'button2.png', functions.rules_screen)
        functions.button((0, 89, 90), 651, 500, 200, 70, 'button1.png', functions.see_highscores)
        functions.button((0, 89, 90), 651, 600, 200, 70, 'button4.png', exit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
Game()

