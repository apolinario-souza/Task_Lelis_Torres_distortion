import pygame
from contents.constants import WIDTH, HEIGHT
from contents.draw import Draw


FPS = 200

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Motor Task')

pygame.init()




def main():
    run = True
    clock = pygame.time.Clock()
    draw = Draw(WIN)  
       

    while run:
        clock.tick(FPS)      
                                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
                   
            
       
        
        draw.update()
        
                               

       
        
    
    pygame.quit()

main()