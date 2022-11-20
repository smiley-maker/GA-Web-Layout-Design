import random
import pygame
from pygame.locals import *

#Navbar class to create a simple rectangle of variable width, height, and location. 
class navbar():
    def __init__(self, maxWidth, maxHeight):
        #Constructor initializing each attribute of the navbar. 
        self.x = random.randrange(0, maxWidth-1, 1)
        self.y = random.randrange(0, maxHeight/2-1, 1)
        self.width = random.randrange(1, abs(maxWidth-self.x), 1)
        self.height = random.randrange(1, abs(maxHeight-self.y), 1)
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Mutates each attribute of the navbar to new random values. 
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth-1, 1)
            self.y = random.randrange(0, maxHeight-1, 1)
            self.width = random.randrange(1, abs(maxWidth-self.x), 1)
            self.height = random.randrange(1, abs(maxHeight-self.y), 1)
    
    def fitness(self, maxWidth, maxHeight):
        #Evaluates the fitness of the navbar based on the following constraints
        fitness = 0
        #(1) Reward if the navbar is close to the top
        if self.y < 0.1*maxHeight:
            fitness += 3
        #(1) Penalize if it is further down the page
        elif self.y > 0.1*maxHeight:
            fitness -= 1
        #(2)&(3) Reward if the navbar is close to the left edge and the width is within a certain range of the page width. 
        if self.x < 0.05*maxWidth and 0.95*maxWidth <= self.width <= maxWidth:
            fitness += 7
        #(4) Reward if the height is under 50px
        if self.height <= 0.1*maxHeight and self.height >= 0.05*maxHeight:
            fitness += 6
        # #(4) Penalize otherwise
        # elif self.height > 0.1*maxHeight:
        #     fitness -= 3
        #(5) Penalize if the height is greater than the width (want a horizontal rectangle)
        if self.height > self.width:
            fitness -= 1
        #(5) Reward otherwise
        elif self.width > self.height:
            fitness += 3
        return fitness

    def display(self, screen):
        #Uses pygame to display the navbar as a rectangle. 
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (82, 148, 255), rect)