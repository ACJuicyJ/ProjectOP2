import pygame
import functions
pygame.init()

width=1500
height=800
screen=pygame.display.set_mode((width,height))
pygame.display.update()


def Game():
    game=True
    while game:
        events = pygame.event.get()
        functions.insert_image('menu.png', 0,0)
        functions.button((0, 89, 90), 800, 300, 200, 70, 'button3.png',functions.game_loop,events)
        functions.button((0, 89, 90), 800, 400, 200, 70, 'button2.png',functions.rules_screen,events)
        functions.button((0, 89, 90), 800, 500, 200, 70, 'button1.png',functions.see_highscores,events)
        functions.button((0, 89, 90), 800, 600, 200, 70, 'button4.png',exit, events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
Game()

