from __future__ import division
import pygame
import time

#initialization of all pygame modules
pygame.init()         

#color macros
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)


#variable definitions
display_width = 800
display_height = 600

#game surface game_display
game_display = pygame.display.set_mode((display_width, display_height))    

#title(caption) creation
pygame.display.set_caption("Snake")

block_size = 10
fps = 15

#pygame clock
clock = pygame.time.Clock()

#font object 
font = pygame.font.SysFont(None, 25) 

#display message function
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width/2, display_height/2])

#infinite game loop
def game_loop():
    game_exit = False
    game_over = False
    #starting coordinates of the rectangle
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0 
    lead_y_change = 0
    while not game_exit:
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Game over. Press C to continue or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
            
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                if event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size
            #code fragment to stop movement on key release        
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        lead_x_change = 0
                    
        #background color setting
        game_display.fill(white)
        #drawing rectangle [x,y,width,height]
        lead_x += lead_x_change
        lead_y += lead_y_change

        #barrier logic
        if lead_x >= display_width-block_size or lead_x <= 0 or lead_y >= display_height-block_size or lead_y <= 0:
            game_over = True
            
        pygame.draw.rect(game_display, black, [lead_x,lead_y,block_size,block_size])
        #rendering graphics
        pygame.display.update()
        #defining fps by delay. Keep minimum for processing cost
        clock.tick(fps)

   
    #counterpart of init()
    pygame.quit()
    #quit system
    quit()


game_loop()
