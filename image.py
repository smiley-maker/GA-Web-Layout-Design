############################################ Image Class #################################################
#Imports:
import random
import pygame
from pygame.locals import *

class image():
    def __init__(self, maxWidth, maxHeight):
        #Constructor to randomly initialize a new image
        self.x = random.randrange(maxWidth/2, maxWidth-1, 1)
        self.y = random.randrange(0, maxHeight-1, 1)
        self.width = random.randrange(1, abs(maxWidth-self.x), 1)
        self.height = random.randrange(1, abs(maxHeight-self.y), 1)
        
    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Mutation function to modify parameters with a random probability
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth-1, 1)
            self.y = random.randrange(0, maxHeight-1, 1)
            self.width = random.randrange(1, abs(maxWidth-self.x), 1)
            self.height = random.randrange(1, abs(maxHeight-self.y), 1)    
    def fitness(self, maxWidth, maxHeight):
        #Function to evaluate the fitness based on the designated optimization constraints for the image
        fitness = 0
        #(8)&(9) The image should start on the right and be less than 40% of the page width
        if self.x > 0.5*maxWidth and self.width >= 0.4*maxWidth:
            fitness += 4
        #(10) The height of the image should be at least a third of the height of the page
        if self.height >= 0.3*maxHeight:
            fitness += 3 #Reward if condition is met
        #(10)
        elif self.height < 0.1*maxHeight:
            fitness -= 1 #Penalty otherwise
        return fitness #Returns final fitness value for the image component. 

    def display(self, screen):
        #Displays the image as a rectangle using the values calculated previously
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255, 233, 176), rect)