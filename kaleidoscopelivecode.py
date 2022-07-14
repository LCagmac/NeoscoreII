pygame.init()
while True: #while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the user presses the 'X' button
            pygame.quit() #De= initialise pygame
            #sys.exit() #Exit
        if event.type == pygame.KEYDOWN: #if a key is pressed down
            if event.key == pygame.K_a:
                print("Pizza")
                neoscore.show(refresh_func)
