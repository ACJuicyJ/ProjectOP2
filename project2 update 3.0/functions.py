import pygame
pygame.init()
boot= pygame.image.load('Boot-1-offense-mode.png')
boot2= pygame.image.load('Boot-2-offense-mode.png')
boot3= pygame.image.load('Boot-3.png')
screen_width= 1910
screen_height= 1007
screen= pygame.display.set_mode((screen_width,screen_height))
gameboard= pygame.image.load('gameboard.png')
events= pygame.event.get()
def game_loop():
    x= 199
    y=109
    l=[ ]
    l2=[ ]
    gameExit= False
    while not gameExit:
        screen.blit(gameboard, (0,0))
        if len(l) < 4:
            if len(l) < 1:
                screen.blit(boot,(x,y))
            elif len(l) <3 and l.count(boot2) < 2:
                screen.blit(boot2,(x,y))
            elif l.count(boot3) < 1:
                screen.blit(boot3,(x,y)) 
        elif len(l2) < 4:
            if len(l2) < 1:
                screen.blit(boot,(x,620))
            elif len(l2)==1 and l.count(boot2) < 2:
                screen.blit(boot2,(x,585))
            elif l2.count(boot3) < 1:
                screen.blit(boot3,(x,550))
        move_key= pygame.key.get_pressed()
        mouse=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if x < 902 and x > 199:
                if move_key[pygame.K_RIGHT]:
                    x= x+ 37
                    p=x
                elif move_key[pygame.K_LEFT]:
                    x-=37
            elif x==199:
                if move_key[pygame.K_RIGHT]:
                    x+=37
            elif x==902:
                if move_key[pygame.K_LEFT]:
                    x -=37
            new_pos= (x,y)
            if len(l) <4:
                if event.type== pygame.MOUSEBUTTONDOWN and event.button==1:
                    if len(l) == 0: # and l.count(boot) < 1:
                        l.append((boot,new_pos))
                    elif len(l)==1: # and l.count(boot2) < 2:
                        l.append((boot2,new_pos))
                    elif l.count(boot2) < 1:
                        l.append((boot3,new_pos))
            elif len(l2) < 4:
                if event.type== pygame.MOUSEBUTTONDOWN and event.button==1:
                    if len(l2) == 0: # and l.count(boot) < 1:
                        l2.append((boot,(x,620)))
                    elif len(l2)==1: # and l.count(boot2) < 2:
                        l2.append((boot2,(x,585)))
                    elif  l2.count(boot2) < 1:
                        l2.append((boot3,(x,550)))

        for boat in l:
            if boat[0] != boot:
                print("TEST")
            screen.blit(boat[0],boat[1])
        for boat in l2:
            if boat[0] != boot:
                print("TEST")
            screen.blit(boat[0],boat[1])

        pygame.display.flip()
        
