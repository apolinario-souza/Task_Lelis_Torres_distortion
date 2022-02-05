import pygame
from .constants import BLACK, BLACK_2, RED, WHITE, WIDTH, HEIGHT, DIAMETER_H, GREEN, DIAMETER_T, HOLDING, WARNING, EXECUTION, RANDOM_INTERVAL,TIME_IMG, N_TRIALS, TARGET_x_1, TARGET_y_1,TARGET_x_2, TARGET_y_2, TARGET_x_3, TARGET_y_3, TARGET_x_4, TARGET_y_4, TARGET_x_5, TARGET_y_5, TARGET_x_6, TARGET_y_6   
import random

import numpy as np
import random
import math


pygame.init()

class Target_random:
    def __init__(self):
        self.cont1 = 0
        self.cont2 =0
        self.cont3 = 0
        self.cont4 = 0
        self.cont5 = 0
        self.cont6 = 0
        self.response = []
        
    def target_control (self, n_trial):        
        for k in range(n_trial):   
            
            check = True
            while check:
                
                b = random.randint(1,  6)           
                if b == 1 and self.cont1 < n_trial//6:
                    self.response.append(1)
                    self.cont1 +=1
                    check = False
                if b == 2 and self.cont2 < n_trial//6:
                    self.response.append(2)
                    self.cont2 +=1
                    check = False
                if b == 3 and self.cont3 < n_trial//6:
                    self.response.append(3)
                    self.cont3 +=1
                    check = False
                if b == 4 and self.cont4 < n_trial//6:
                    self.response.append(4)
                    self.cont4 +=1
                    check = False
                if b == 5 and self.cont5 < n_trial//6:
                    self.response.append(5)
                    self.cont5 +=1
                    check = False
                if b == 6 and self.cont6 < n_trial//6:
                    self.response.append(6)
                    self.cont6 +=1
                    check = False
                    
        return self.response
            

                
      
   
 
        
    

class Background:
    def __init__(self):
        self.clicked = False
        self.start = False
        self.current_time = []
        self.trial = 0
        self.pos_target_x = []
        self.pos_target_y = []
        self.cont = 0
        self.cont2 = False
        self.mouse_position = []
        self.check = False
        self.execution_time = []
        self.sequence = Target_random().target_control(N_TRIALS)   
        self.random = 0
        
        self.increase = 0
                  
    
       
    
    def draw_circle_t(self, win, pos_x, pos_y, diameter, fill,color):
        
        pygame.draw.circle(win, color, (pos_x, pos_y), diameter, fill)
    
    def img (self, win, pos_x, pos_y, diameter,  img):
        image = pygame.image.load(img)        
        
        image = pygame.transform.scale(image, (diameter, diameter)) 
        win.blit(image, (pos_x-diameter//2, pos_y-diameter//2)) 
    
    def draw_mouse(self, win, mouse_position):
        mouse_position = mouse_position        
        for pos in mouse_position:                                  
            pygame.draw.circle(win, RED, (pos[0],pos[1]), DIAMETER_T//4, 0)
        
    def text_write (self, win, text, width, height):
        base_font = pygame.font.Font(None, 32)
        text_surface = base_font.render(text, True, (255,255,255))
        win.blit(text_surface, (width, height))     
        
    def draw_button (self, win):
        win.fill(BLACK)        
        pos = pygame.mouse.get_pos()       
        button_1 = pygame.Rect(WIDTH//2-DIAMETER_H//2, (HEIGHT//2*1.5)+(DIAMETER_H//2)//2, DIAMETER_H, DIAMETER_H//2)
        pygame.draw.rect(win, BLACK, button_1)
        if button_1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True        
        
        self.text_write(win,'Start', WIDTH//2-DIAMETER_H//2, (HEIGHT//2*1.5)+(DIAMETER_H//2)//2)   
      
        
    def draw(self, win):
        
        
        #Set random value      
        if self.cont2 == False:
            self.random = random.randint(RANDOM_INTERVAL[0],  RANDOM_INTERVAL[1])
            
        
        self.cont2  = True
        

        if self.clicked == True and self.trial < N_TRIALS:
            #Hide mouse 
            pygame.mouse.set_visible(False)
        
            #def cont timer
            self.current_time.append(pygame.time.get_ticks())            
            self.cont = self.current_time[-1] - self.current_time[0]
                       
            
            # Screen 1: Holding 
            if self.cont >= 0 and self.cont < HOLDING:
                win.fill(BLACK)
                x = WIDTH//2+(DIAMETER_H//2)
                y = HEIGHT//2-(DIAMETER_H//2)
                self.draw_circle_t(win, x,y, DIAMETER_H, 0, WHITE)            
               
               
            
            # Screen 2: Stimulus 
            if self.cont >= HOLDING and self.cont < WARNING:
                win.fill(BLACK)
                
                n_of_points = (abs(HOLDING-WARNING)/1000)*(200-5)
                x = WIDTH//2+(DIAMETER_T//2)
                y = HEIGHT//2-(DIAMETER_T//2)
                
                if self.sequence[self.trial] == 1:
                    self.pos_target_x = int(x*TARGET_x_1) 
                    self.pos_target_y = int(y*TARGET_y_1)    
                    self.increase +=1
                    set_x = self.pos_target_x+(x-self.pos_target_x)
                    set_y = self.pos_target_y+(y-self.pos_target_y)                 
                    
                    rate_increas_x = abs(set_x-self.pos_target_x)/n_of_points
                    rate_increas_y = abs(set_y-self.pos_target_y)/n_of_points       
                    
                    self.draw_circle_t(win, set_x+(rate_increas_x*self.increase), set_y-(rate_increas_y*self.increase), DIAMETER_T, 0, BLACK_2)
                                    
                if self.sequence[self.trial] == 2:
                    self.pos_target_x = int(x*TARGET_x_2) 
                    self.pos_target_y = int(y*TARGET_y_2)  
                    self.increase +=1
                    set_x = self.pos_target_x+(x-self.pos_target_x)
                    set_y = self.pos_target_y+(y-self.pos_target_y)                  
                    rate_increas_x = abs(set_x-self.pos_target_x)/n_of_points
                    rate_increas_y = abs(set_y-self.pos_target_y)/n_of_points       
                    
                    self.draw_circle_t(win, set_x-(rate_increas_x*self.increase), set_y-(rate_increas_y*self.increase), DIAMETER_T, 0, BLACK_2)
                   
                
                if self.sequence[self.trial] == 3:
                    self.pos_target_x = int(x*TARGET_x_3) 
                    self.pos_target_y = int(y*TARGET_y_3)   
                    self.increase +=1
                    set_x = self.pos_target_x+(x-self.pos_target_x)
                    set_y = self.pos_target_y+(y-self.pos_target_y)
                                                            
                    rate_increas_x = abs(set_x-self.pos_target_x)/n_of_points
                    rate_increas_y = abs(set_y-self.pos_target_y)/n_of_points       
                    
                    self.draw_circle_t(win, set_x-(rate_increas_x*self.increase), set_y-(rate_increas_y*self.increase), DIAMETER_T, 0, BLACK_2)
                    
                
                if self.sequence[self.trial] == 4:
                    self.pos_target_x = int(x*TARGET_x_4)  
                    self.pos_target_y = int(y*TARGET_y_4)    
                    self.increase +=1
                    set_x = self.pos_target_x+(x-self.pos_target_x)
                    set_y = self.pos_target_y+(y-self.pos_target_y)        
                   
                    
                    rate_increas_x = abs(set_x-self.pos_target_x)/n_of_points
                    rate_increas_y = abs(set_y-self.pos_target_y)/n_of_points       
                    
                    self.draw_circle_t(win, set_x+(rate_increas_x*self.increase), set_y+(rate_increas_y*self.increase), DIAMETER_T, 0, BLACK_2)
                    
                    
                if self.sequence[self.trial] == 5:
                    self.pos_target_x = int(x*TARGET_x_5)  
                    self.pos_target_y = int(y*TARGET_y_5)    
                    self.increase +=1
                    set_x = self.pos_target_x+(x-self.pos_target_x)
                    set_y = self.pos_target_y+(y-self.pos_target_y)     
                                        
                    rate_increas_x = abs(set_x-self.pos_target_x)/n_of_points
                    rate_increas_y = abs(set_y-self.pos_target_y)/n_of_points       
                    
                    self.draw_circle_t(win, set_x+(rate_increas_x*self.increase), set_y+(rate_increas_y*self.increase), DIAMETER_T, 0, BLACK_2)
                    
                    
                if self.sequence[self.trial] == 6:
                    self.pos_target_x = int(x*TARGET_x_6)  
                    self.pos_target_y = int(y*TARGET_y_6)   
                    self.increase +=1
                    set_x = self.pos_target_x+(x-self.pos_target_x)
                    set_y = self.pos_target_y+(y-self.pos_target_y)
                    
                    
                    
                    rate_increas_x = abs(set_x-self.pos_target_x)/n_of_points
                    rate_increas_y = abs(set_y-self.pos_target_y)/n_of_points       
                    
                    self.draw_circle_t(win, set_x-(rate_increas_x*self.increase), set_y+(rate_increas_y*self.increase), DIAMETER_T, 0, BLACK_2)
                                      
                            
                
                
                #Circle of home position
                x = WIDTH//2+(DIAMETER_H//2)
                y = HEIGHT//2-(DIAMETER_H//2)
                self.draw_circle_t(win, x, y, DIAMETER_H, 0, WHITE)
                #print(self.increase)
                
                if self.increase >= 0  and self.increase < 200//6:
                    self.img (win,  x, y, DIAMETER_H, "img/trial_"+str(self.trial+1)+"/1.png")
                
                if self.increase >= (200//6)  and self.increase < (200//6)*2:
                    self.img (win,  x, y, DIAMETER_H, "img/trial_"+str(self.trial+1)+"/2.png") 
                
                if self.increase >= (200//6)*2  and self.increase < (200//6)*3:
                    self.img (win,  x, y, DIAMETER_H, "img/trial_"+str(self.trial+1)+"/3.png") 
                
                if self.increase >= (200//6)*3  and self.increase < (200//6)*4:
                    self.img (win,  x, y, DIAMETER_H, "img/trial_"+str(self.trial+1)+"/4.png")
                
                if self.increase >= (200//6)*4  and self.increase < (200//6)*5:
                    self.img (win,  x, y, DIAMETER_H, "img/trial_"+str(self.trial+1)+"/5.png")
                
                if self.increase >= (200//6)*5:
                    self.img (win,  x, y, DIAMETER_H, "img/trial_"+str(self.trial+1)+"/6.png")                
            
            #Screen 3: Empty         
            if self.cont >= WARNING and self.cont < WARNING+self.random:
                #print('Empty')
                win.fill(BLACK)
                
                #Circle of home position
                x = WIDTH//2+(DIAMETER_H//2)
                y = HEIGHT//2-(DIAMETER_H//2)
                
                
                self.start = True
                self.mouse_position = [] #Set mouse position
                x = WIDTH//2+(DIAMETER_H//2)
                y = HEIGHT//2-(DIAMETER_H//2)
                pygame.mouse.set_pos([x, y]) #Set to center
                
                
            #Screen 4: Start 
            if  self.cont >= WARNING+self.random and self.cont < WARNING+EXECUTION+self.random and self.start == True :
                #print('Start')
                                
                #Circle of home position
                x = WIDTH//2+(DIAMETER_H//2)
                y = HEIGHT//2-(DIAMETER_H//2)
                self.draw_circle_t(win, x, y, DIAMETER_H, 0, GREEN)
                
                #Circles of target
                self.draw_circle_t(win, x*TARGET_x_1, y*TARGET_y_1, DIAMETER_T, 0, WHITE) #1
                self.draw_circle_t(win, x*TARGET_x_2, y*TARGET_y_2, DIAMETER_T, 0, WHITE) #2
                self.draw_circle_t(win,  x*TARGET_x_3, y*TARGET_y_3, DIAMETER_T, 0, WHITE) #3
                self.draw_circle_t(win,  x*TARGET_x_4, y*TARGET_y_4, DIAMETER_T, 0, WHITE) #4
                self.draw_circle_t(win,  x*TARGET_x_5, y*TARGET_y_5, DIAMETER_T, 0, WHITE) #5
                self.draw_circle_t(win, x*TARGET_x_6, y*TARGET_y_6, DIAMETER_T, 0, WHITE) #6
                
                #Get time of response 
                self.execution_time.append(pygame.time.get_ticks())  
                
                
                #Get mouse position and draw                
                self.mouse_position.append(pygame.mouse.get_pos())
                self.draw_mouse(win, self.mouse_position)
                      
                
            if self.cont > WARNING+EXECUTION+self.random and self.cont < WARNING+EXECUTION+self.random+10000:
                win.fill(BLACK)
                self.img (win,  WIDTH//2*.60, HEIGHT//2- DIAMETER_H*2, DIAMETER_H*2, "img/trial_"+str(self.trial+1)+"/1show.png")
                self.img (win,  WIDTH//2*.80, HEIGHT//2- DIAMETER_H*2, DIAMETER_H*2, "img/trial_"+str(self.trial+1)+"/2show.png")
                self.img (win,  WIDTH//2*1, HEIGHT//2- DIAMETER_H*2, DIAMETER_H*2, "img/trial_"+str(self.trial+1)+"/3show.png")
                self.img (win,  WIDTH//2*1.2, HEIGHT//2- DIAMETER_H*2, DIAMETER_H*2, "img/trial_"+str(self.trial+1)+"/4show.png")
                self.img (win,  WIDTH//2*1.4, HEIGHT//2- DIAMETER_H*2, DIAMETER_H*2, "img/trial_"+str(self.trial+1)+"/5show.png")
                self.img (win,  WIDTH//2*1.6, HEIGHT//2- DIAMETER_H*2, DIAMETER_H*2, "img/trial_"+str(self.trial+1)+"/6show.png")
                
                self.text_write (win, "1", WIDTH//2*.60,  HEIGHT//2- DIAMETER_H*3.5)
                self.text_write (win, "2", WIDTH//2*.80,  HEIGHT//2- DIAMETER_H*3.5)
                self.text_write (win, "3", WIDTH//2*1,  HEIGHT//2- DIAMETER_H*3.5)
                self.text_write (win, "4", WIDTH//2*1.2,  HEIGHT//2- DIAMETER_H*3.5)
                self.text_write (win, "5", WIDTH//2*1.4,  HEIGHT//2- DIAMETER_H*3.5)
                self.text_write (win, "6", WIDTH//2*1.6,  HEIGHT//2- DIAMETER_H*3.5)
                
                
            # Set all ans Save
            if self.cont > WARNING+EXECUTION+self.random+10000:
                
                self.trial +=1
                
                #Save data
                target_x = []
                target_y = []
                names = ['Time', 'Mouse_x', 'Mouse_y', 'Target_x', 'Target_y']
                
                for i in range (len(self.execution_time)):
                    target_x.append(self.pos_target_x)
                    target_y.append(self.pos_target_y)
                np.savetxt('trials/trial_'+ str(self.trial)+'.csv', np.column_stack([self.execution_time,self.mouse_position,target_x, target_y] ), header = ','.join(names), delimiter=',')
                
                #Set data
                self.current_time = []
                self.mouse_position = []
                self.execution_time = [] 
                self.increase = 0
               
                self.cont2 = False 
                
               
                
                             
        
        else:
            
            pygame.mouse.set_visible(True)
            
            self.draw_button(win)
            
            
            
                
              
        
 