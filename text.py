import random
import pygame
from pygame.locals import *

class text():
    def __init__(self, maxWidth, maxHeight):
        #Constructor to initialize parameters of text object to random values
        self.x = random.randint(0, maxWidth) #Sets the x coordinate of the text to a random value on the screen
        self.y = random.randint(0, maxHeight) #Sets the y coordinate of the text to a random value on the screen
        self.width = random.randint(0, maxWidth) #Sets the width of the text to a random number
        self.height = random.randint(0, maxHeight) #Sets the height of the text to an integer feasible random number. 
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Mutation function to randomize some of the values of the text
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth, 1)
            self.y = random.randrange(0, maxHeight, 1)
            self.width = random.randrange(0, int(maxWidth/2), 5)
            self.height = random.randrange(0, int(maxHeight/2), 5)
    
    def fitness(self, maxWidth, maxHeight):
        #Function to calculate the fitness of the text given the following constraints. 
        fitness = 0
        #(11)&(12) The text should be on the left and be less than half the window size
        if self.x < 0.02*maxWidth and self.width <= maxWidth/2:
            fitness += 4 #Reward if constraint is met
        #(13) The height of the text box should be at least a third of the height of the page. 
        if self.height >= 0.3*maxHeight:
            fitness += 3 #Reward if condition is met
        #(13)
        elif self.height < 0.3*maxHeight:
            fitness -= 1 #Penalty if not met
        return fitness #Returns the fitness of the text component

    def display(self, screen):
        #Function to draw the rectangle using the calculated parameters
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (0,0,0), rect)
