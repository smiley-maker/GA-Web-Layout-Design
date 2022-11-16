import random
import pygame
from pygame.locals import *

#Navbar class to create a simple rectangle of variable width, height, and location. 
class navbar():
    def __init__(self, maxWidth, maxHeight):
        #Constructor initializing each attribute of the navbar. 
        self.x = random.randrange(0, maxWidth, 1)
        self.y = random.randrange(0, maxHeight, 1)
        self.width = random.randrange(maxWidth/2, maxWidth, 1)
        self.height = random.randrange(20, maxHeight, 1)
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Mutates each attribute of the navbar to new random values. 
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth, 1)
            self.y = random.randrange(0, maxHeight, 1)
            self.width = random.randrange(maxWidth/2, maxWidth, 5)
            self.height = random.randrange(20, maxHeight, 5)
    
    def fitness(self, maxWidth):
        #Evaluates the fitness of the navbar based on the following constraints
        fitness = 0
        #Reward if the navbar is close to the top
        if self.y < 30:
            fitness += 3
        #Penalize if it is further down the page
        elif self.y > 50:
            fitness -= 1
        #Reward if the navbar is close to the left edge and the width is within a certain range of the page width. 
        if self.x < 10 and self.width >= maxWidth - 10 and self.width <= maxWidth:
            fitness += 4
        #Reward if the height is under 50px
        if self.height <= 50:
            fitness += 3
        #Penalize otherwise
        elif self.height > 50:
            fitness -= 1
        #Penalize if the height is greater than the width (want a horizontal rectangle)
        if self.height > self.width:
            fitness -= 3
        #Reward otherwise
        elif self.width > self.height:
            fitness += 1
        return fitness

    def display(self, screen):
        #Uses pygame to display the navbar as a rectangle. 
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (82, 148, 255), rect)