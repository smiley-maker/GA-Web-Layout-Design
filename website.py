######################### Website class to create new designs and update the fitness ############################
#Imports
from navbar import *
from image import *
from button import *
from text import *
import pygame
from pygame.locals import *
import numpy as np

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

    def isIntersecting(self, a, b):
        if abs((a.x + a.width/2) - (b.x + b.width/2)) < (a.width + b.width)/2:
            return True
        return False

    #Calculates area for set packing constraint
    def calculateArea(self, a, b):
        #wh + wh - aoi
        area = 0
        w = min((a.x+a.width), (b.x+b.width)) - max(a.x, b.x)
        h = min((a.y+a.height), (b.y+b.height)) - max(a.y, b.y)
        if w > 0 and h > 0:
            area = a.width*a.height + b.width*b.height - w*h
        else:
            area = a.width*a.height + b.width*b.height
        return area
    
    def fitness(self, maxWidth, maxHeight, gen=None):
        #Calculates the fitness for each component and sums
        fitness = sum([self.web[i].fitness(maxWidth, maxHeight) for i in range(len(self.web))])
#        fitness = self.web[0].fitness(maxWidth, maxHeight) + self.web[1].fitness(maxWidth, maxHeight) + self.web[2].fitness(maxWidth, maxHeight) + self.web[3].fitness(maxWidth, maxHeight)
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
        fitness += sum([-8 for b in self.web[1:] if self.isIntersecting(self.web[0], b)])
        #if sum([i.width*i.height for i in self.web]) <= maxWidth*maxHeight:
#        fitness -= max([int(0.00001*(maxWidth*maxHeight - np.sum([i.width*i.height for i in self.web]))) , 0])
        #Set packing -> whole area should be covered. 
        fitness -= max([int(0.00001*np.sum([(maxWidth*maxHeight - self.calculateArea(self.web[i], self.web[i+1])) for i in range(len(self.web)-1)])), 0])
        
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