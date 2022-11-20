import random
import pygame
from pygame.locals import *

class button():
    def __init__(self, maxWidth, maxHeight):
        #Constructor to initialize values for the x,y coordinate and height and width
        self.x = random.randrange(0, maxWidth/2-1, 1)
        self.y = random.randrange(0, maxHeight-1, 1)
        self.width = random.randrange(1, abs(maxWidth-self.x), 1)
        self.height = random.randrange(1, abs(maxHeight-self.y), 1)
        
    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Mutation function to randomly change the values of the button
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth-1, 1)
            self.y = random.randrange(0, maxHeight-1, 1)
            self.width = random.randrange(1, abs(maxWidth-self.x), 1)
            self.height = random.randrange(1, abs(maxHeight-self.y), 1)
    
    def fitness(self, maxWidth, maxHeight):
        #Function to calculate the button's fitness based on various constraints
        fitness = 0
        #(6) The width of the button should be less than 20% of the page width
        if self.width <= 0.2*maxWidth:
            fitness += 2 #If true, reward the GA
        #(6) We don't want the button to get to small, however, so
        elif self.width < 0.05*maxWidth:
            fitness -= 1 #penalize the GA here. 
        #(6) We also want to penalize for a larger button
        elif self.width >= 0.5*maxWidth:
            fitness -= 2
        #(7) If the height of the button is between 1% and 10% of the page height,
        if 0.01*maxHeight <= self.height <= 0.1*maxHeight:
            fitness += 3 #Include a positive fitness value
        #(7) Otherwise, reduce the fitness
        elif self.height > 0.1*maxHeight:
            fitness -= 1
        return fitness #Return the button's fitness value. 

    def display(self, screen):
        #Display the button as a rectangle on the screen using pygame. 
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (238, 140, 255), rect)