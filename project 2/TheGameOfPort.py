import pygame, sys

pygame.init()


black=(0,0,0)
color1=(65,37,19)
color2=(132,34,56)
color3=(98,94,78)
screen_width= 1910
screen_height= 1007
screen= pygame.display.set_mode((screen_width,screen_height))
menu= pygame.image.load('menu.png')
gameboard= pygame.image.load('gameboard.png')
highscores= pygame.image.load('highscore.png')
pause= pygame.image.load('pause.png')
rules4= pygame.image.load('rules4.png')
rules3= pygame.image.load('rules3.png')
rules2= pygame.image.load('rules2.png')
rules1= pygame.image.load('rules1.png')
buttons1=pygame.image.load('button1.png')
buttons2=pygame.image.load('button2.png')
buttons3=pygame.image.load('button3.png')
pijl=pygame.image.load('pijl.png')
pijl2=pygame.image.load('pijl2.png')
pygame.display.set_caption("The Game of port")

rulesbuttons1=pygame.draw.rect(screen,color2,[1650,910,50,40])
rulesbuttons2=pygame.draw.rect(screen,color1,[1700,900,10,73])
rulesbuttons3=pygame.draw.rect(screen,black,[1710,905,10,60])
rulesbuttons4= pygame.draw.rect(screen,black,[1710,915,20,30])
rulesbuttons5=pygame.draw.rect(screen,color2,[1710,930,50,15])


        

button1=pygame.draw.rect(screen,black,[800,300,200,70])
button2=pygame.draw.rect(screen,color2,[800,400,200,70])
button3=pygame.draw.rect(screen,color3,[800,500,200,70])
button4=pygame.draw.rect(screen,color3,[1813,2,100,50])
button5=pygame.draw.rect(screen,color2,[720,570,200,70])
button6=pygame.draw.rect(screen,color3,[950,570,200,70])
button7=pygame.draw.rect(screen,color3,[1813,2,100,50])
button8=pygame.draw.rect(screen,color3,[1813,2,100,50])
rulesbutton2=pygame.draw.rect(screen,color2,[1600,900,200,70])
rulesbutton1=pygame.draw.rect(screen,color3,[100,900,200,70])

pygame.display.update()



def game_loop():
    game=True
    while game:
        screen.blit(gameboard,(0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])
        pause_button(button4)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game= False
                
                
def pause_loop():
    game=True
    while game:
        screen.blit(pause,(700,400))
        pygame.draw.rect(screen,color2,[720,570,200,70])
        pygame.draw.rect(screen,color3,[950,570,200,70])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button5.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button6.collidepoint(pygame.mouse.get_pos()):
                game= False
            if event.type == pygame.QUIT:
                game= False

def go_to_main_button():
    for event in pygame.event.get():
        if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button5.collidepoint(pygame.mouse.get_pos()):
            game_main_menu()

def pause_button(press_button):
    for event in pygame.event.get():
        if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and press_button.collidepoint(pygame.mouse.get_pos()):
            pause_loop()

        
def button(press_button):
    for event in pygame.event.get():
        if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and press_button.collidepoint(pygame.mouse.get_pos()):
            game_loop()
            
def rules_screen1():
    rules=True
    while rules:
        screen.blit(rules1,(0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])
        pygame.draw.rect(screen,color2,[1650,910,50,40])
        pygame.draw.rect(screen,color1,[1700,900,10,73])
        pygame.draw.rect(screen,black,[1710,905,10,60])
        pygame.draw.rect(screen,black,[1710,915,20,30])
        pygame.draw.rect(screen,color2,[1710,930,50,15])
        screen.blit(pijl,(1650,900))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button7.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons1.collidepoint(pygame.mouse.get_pos()):
                rules_screen2()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons2.collidepoint(pygame.mouse.get_pos()):
                rules_screen2()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons3.collidepoint(pygame.mouse.get_pos()):
                rules_screen2()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons4.collidepoint(pygame.mouse.get_pos()):
                rules_screen2()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons5.collidepoint(pygame.mouse.get_pos()):
                rules_screen2()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
def rules_screen2():
    rules=True
    while rules:
        screen.blit(rules2,(0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])
        pygame.draw.rect(screen,color2,[100,910,50,40])
        pygame.draw.rect(screen,color1,[90,900,10,73])
        pygame.draw.rect(screen,black,[80,905,10,60])
        pygame.draw.rect(screen,black,[70,915,20,30])
        pygame.draw.rect(screen,color2,[60,930,50,15])
        screen.blit(pijl2,(50,885))
        pygame.draw.rect(screen,color2,[1650,910,50,40])
        pygame.draw.rect(screen,color1,[1700,900,10,73])
        pygame.draw.rect(screen,black,[1710,905,10,60])
        pygame.draw.rect(screen,black,[1710,915,20,30])
        pygame.draw.rect(screen,color2,[1710,930,50,15])
        screen.blit(pijl,(1650,900))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button7.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbutton1.collidepoint(pygame.mouse.get_pos()):
                rules_screen1()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons1.collidepoint(pygame.mouse.get_pos()):
                rules_screen3()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons2.collidepoint(pygame.mouse.get_pos()):
                rules_screen3()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons3.collidepoint(pygame.mouse.get_pos()):
                rules_screen3()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons4.collidepoint(pygame.mouse.get_pos()):
                rules_screen3()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons5.collidepoint(pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
def rules_screen3():
    rules=True
    while rules:
        screen.blit(rules3,(0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])

        pygame.draw.rect(screen,color2,[100,910,50,40])
        pygame.draw.rect(screen,color1,[90,900,10,73])
        pygame.draw.rect(screen,black,[80,905,10,60])
        pygame.draw.rect(screen,black,[70,915,20,30])
        pygame.draw.rect(screen,color2,[60,930,50,15])
        screen.blit(pijl2,(50,885))
        pygame.draw.rect(screen,color2,[1650,910,50,40])
        pygame.draw.rect(screen,color1,[1700,900,10,73])
        pygame.draw.rect(screen,black,[1710,905,10,60])
        pygame.draw.rect(screen,black,[1710,915,20,30])
        pygame.draw.rect(screen,color2,[1710,930,50,15])
        screen.blit(pijl,(1650,900))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button7.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbutton1.collidepoint(pygame.mouse.get_pos()):
                rules_screen2()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons1.collidepoint(pygame.mouse.get_pos()):
                rules_screen4()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons2.collidepoint(pygame.mouse.get_pos()):
                rules_screen4()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons3.collidepoint(pygame.mouse.get_pos()):
                rules_screen4()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons4.collidepoint(pygame.mouse.get_pos()):
                rules_screen4()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbuttons5.collidepoint(pygame.mouse.get_pos()):
                rules_screen4()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def rules_screen4():
    rules=True
    while rules:
        screen.blit(rules4,(0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])
        pygame.draw.rect(screen,color2,[100,910,50,40])
        pygame.draw.rect(screen,color1,[90,900,10,73])
        pygame.draw.rect(screen,black,[80,905,10,60])
        pygame.draw.rect(screen,black,[70,915,20,30])
        pygame.draw.rect(screen,color2,[60,930,50,15])
        screen.blit(pijl2,(50,885))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button7.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbutton1.collidepoint(pygame.mouse.get_pos()):
                rules_screen3()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    

pos_mouse=pygame.mouse.get_pos()
def game_rules():
    rules= True
    while rules:
        screen.blit(rules1,(0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])
        pygame.draw.rect(screen,color2,[1600,900,100,35])
        pygame.draw.rect(screen,color3,[100,900,200,70])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button7.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and rulesbutton2.collidepoint(pygame.mouse.get_pos()):
                rules_screen1()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
def see_highscores():
    see_highscores= True
    while see_highscores:
        screen.blit(highscores, (0,0))
        pygame.draw.rect(screen,color3,[1813,2,100,50])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button8.collidepoint(pygame.mouse.get_pos()):
                game_main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def game_main_menu():
    gameExit= False
    while not gameExit:
        screen.blit(menu,(0,0))
        pygame.draw.rect(screen,color1,[800,300,200,70])
        screen.blit(buttons3,(800,300))
        pygame.draw.rect(screen,color2,[800,400,200,70])
        screen.blit(buttons2,(800,400))
        pygame.draw.rect(screen,color3,[800,500,200,70])
        screen.blit(buttons1,(800,500))
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button1.collidepoint(pygame.mouse.get_pos()):
                game_loop()
            elif event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button2.collidepoint(pygame.mouse.get_pos()):
                rules_screen1()
            elif event.type== pygame.MOUSEBUTTONDOWN and event.button==1 and button3.collidepoint(pygame.mouse.get_pos()):
                see_highscores()
            elif event.type == pygame.QUIT:
                gameExit= True
                pygame.quit()
                quit()
game_main_menu()
pygame.quit()
quit()
