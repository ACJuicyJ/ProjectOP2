import pygame
import pygame, sys
import functions
pygame.init()


black=(0,0,0)
color1=(65,37,19)
color2=(132,34,56)
color3=(98,94,78)
screen_width= 1910
screen_height= 1007
screen= pygame.display.set_mode((screen_width,screen_height))
menu= pygame.image.load('menu.png')
pause= pygame.image.load('pause.png')
highscores= pygame.image.load('highscore.png')
boot= pygame.image.load('Boot-1-offense-mode.png')
boot2= pygame.image.load('Boot-2-offense-mode.png')
boot3= pygame.image.load('Boot-3.png')
gameboard= pygame.image.load('gameboard.png')
pygame.display.set_caption("The Game of port")

button1=pygame.draw.rect(screen,black,[800,300,200,70])
button2=pygame.draw.rect(screen,color2,[800,400,200,70])
button3=pygame.draw.rect(screen,color3,[800,500,200,70])
button4=pygame.draw.rect(screen,color3,[1813,2,100,50])
button5=pygame.draw.rect(screen,color2,[720,570,200,70])
button6=pygame.draw.rect(screen,color3,[950,570,200,70])

pygame.display.update()


        




def button(press_button):
    for event in pygame.event.get():
        if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and press_button.collidepoint(pygame.mouse.get_pos()):
            functions.game_loop()


def game_main_menu():
    gameExit= False
    while not gameExit:
        screen.blit(menu,(0,0))
        pygame.draw.rect(screen,color1,[800,300,200,70])
        button(button1)
        pygame.draw.rect(screen,color2,[800,400,200,70])
        pygame.draw.rect(screen,color3,[800,500,200,70])
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button2.collidepoint(pygame.mouse.get_pos()):
                game_rules()
            elif event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button3.collidepoint(pygame.mouse.get_pos()):
                see_highscores()
            elif event.type == pygame.QUIT:
                gameExit= True

game_main_menu()

pygame.quit()
quit()
