######################### Website class to create new designs and update the fitness ############################
#Imports
from navbar import *
from image import *
from button import *
from text import *
import pygame
from pygame.locals import *

#Website class ->
class website():
    #Constructor
    def __init__(self, maxWidth, maxHeight):
        #Creates a list of web components
        self.web = [] 
        self.web.append(navbar(maxWidth, maxHeight)) #Adds the navbar
        self.web.append(image(maxWidth, maxHeight)) #Adds the image
        self.web.append(button(maxWidth, maxHeight)) #Adds the button
        self.web.append(text(maxWidth, maxHeight)) #Adds the text

    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Uses each components mutate function to update the design
        self.web[0].mutate(mutationRate, maxWidth, maxHeight)
        self.web[1].mutate(mutationRate, maxWidth, maxHeight)
        self.web[2].mutate(mutationRate, maxWidth, maxHeight)
        self.web[3].mutate(mutationRate, maxWidth, maxHeight)
    
    def fitness(self):
        #Calculates the fitness for each component and sums
        fitness = self.web[0].fitness(500) + self.web[1].fitness(500) + self.web[2].fitness(500) + self.web[3].fitness(500)
        #Adds a few other constraints relating two or more components. 
        #(14) If the image and text overlaps, add a penalty
        if self.web[1].x - self.web[3].x < 0 or self.web[3].x - self.web[1].x < 0: 
            fitness -= 3
        #(15) If the button and text are within a certain range of each other, add a reward
        if 5 <= self.web[3].y - self.web[2].y <= 30:
            fitness += 1
        #(16) Applies the golden ratio to the image and the text components. 
        if self.web[1].width*self.web[1].height >= -10 + (self.web[3].width*self.web[3].height*1.68) and self.web[1].width*self.web[1].height <= 10 + (self.web[3].width*self.web[3].height*1.68):
            fitness += 5
        return fitness
    
    def display(self, maxWidth, maxHeight, isOn):
        #Displays the website using pygame. 
        pygame.init() #Initializes the pygame window
        screen = pygame.display.set_mode((maxWidth, maxHeight)) #Creates a screen with the desired size
        running = False #Variable to control if the window is visible
        if isOn: running = True
        #While running is true (we want to see the website)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                screen.fill((255, 255, 255))
            #Loads each of the components onto the screen using their display functions
            for comp in self.web:
                comp.display(screen)
            pygame.display.flip()
        pygame.quit()