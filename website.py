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

    #Function to determine if two components are intersecting
    def isIntersecting(self, a, b):
        #If the difference between the center point of object a and the center point of object b is less than their average width
        if abs((a.x + a.width/2) - (b.x + b.width/2)) < (a.width + b.width)/2:
            return True #They are intersecting
        return False

    #Calculates area for set packing constraint
    def calculateArea(self, a, b):
        combinedArea = 0 #Variable to store the area result
        newW = min((a.x+a.width), (b.x+b.width)) - max(a.x, b.x) #Calculates the width of the combined objects
        newH = min((a.y+a.height), (b.y+b.height)) - max(a.y, b.y) #Calculates the height of the combined objects
        if newW > 0 and newH > 0:
            combinedArea = a.width*a.height + b.width*b.height - newW*newH #Calculates reduced area
        else:
            combinedArea = a.width*a.height + b.width*b.height #If the objects aren't overlapping, return just the normal areas
        return combinedArea #Returns the combined area. 
    
    def fitness(self, maxWidth, maxHeight, gen=None):
        #Calculates the fitness for each component and sums
        fitness = sum([self.web[i].fitness(maxWidth, maxHeight) for i in range(len(self.web))])
        #Adds a few other constraints relating two or more components. 
        #(14) If the image and text overlaps, add a penalty
        if not self.web[1].x - self.web[3].x < 0 or not self.web[3].x - self.web[1].x < 0: 
            fitness += 3
        #(15) If the button and text are within a certain range of each other, add a reward
        if 0.05*maxWidth <= self.web[3].y - self.web[2].y <= 0.1*maxWidth:
            fitness += 1
        #(17) Applies the golden ratio to the image and the text components. 
        if self.web[1].width*self.web[1].height >= -10 + (self.web[3].width*self.web[3].height*1.68) and self.web[1].width*self.web[1].height <= 10 + (self.web[3].width*self.web[3].height*1.68):
            fitness += 5
        #(16) Components aren't overlapping the navbar
        fitness += sum([4 for b in self.web[1:] if not self.isIntersecting(self.web[0], b)])
        #(18) Set packing -> whole area should be covered. 
        fitness -= max([int(0.000005*np.sum([(maxWidth*maxHeight - self.calculateArea(self.web[i], self.web[i+1])) for i in range(len(self.web)-1)])), 0])
        
        return fitness
    
    def display(self, maxWidth, maxHeight, isOn, isPicture, name):
        #Displays the website using pygame. 
        pygame.init() #Initializes the pygame window
        screen = pygame.display.set_mode((maxWidth, maxHeight)) #Creates a screen with the desired size
        running = False #Variable to control if the window is visible
        if isOn: running = True
        #While running is true (we want to see the website)
        while running:
            screen = pygame.display.set_mode((maxWidth, maxHeight))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                screen.fill((255, 255, 255))
            #Loads each of the components onto the screen using their display functions
            for comp in self.web:
                comp.display(screen)
            pygame.display.flip()
            pygame.image.save(screen , name)
        pygame.quit()