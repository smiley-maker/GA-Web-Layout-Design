import random
import pygame
from pygame.locals import *
from color import *
class text():
    def __init__(self, maxWidth, maxHeight):
        #Constructor to initialize parameters of text object to random values
        self.x = random.randrange(0, maxWidth/2-1, 1)
        self.y = random.randrange(0, maxHeight-1, 1)
        self.width = random.randrange(1, abs(maxWidth-self.x), 1)
        self.height = random.randrange(1, abs(maxHeight-self.y), 1)
        self.color = color()
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        #Mutation function to randomize some of the values of the text
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth-1, 1)
            self.y = random.randrange(0, maxHeight-1, 1)
            self.width = random.randrange(1, abs(maxWidth-self.x), 1)
            self.height = random.randrange(1, abs(maxHeight-self.y), 1)
            self.color.randomize()

    def contrast(self):
        contrastRatio = 0
        lum1 = color.luminance(self.color)
        white = color(255, 255, 255)
        lum2 = color.luminance(white)
        if lum1 > lum2:
            contrastRatio = (lum1 + 0.05)/(lum2 + 0.05)
        else:
            contrastRatio = (lum2 + 0.05)/(lum1 + 0.05)
        return contrastRatio

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
        if self.contrast() < 2.8:
            fitness -= 5
        elif self.contrast() > 5:
            fitness += 5
        return fitness #Returns the fitness of the text component

    def display(self, screen):
        #Function to draw the rectangle using the calculated parameters
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (self.color.red, self.color.green, self.color.blue), rect)
