import random
import pygame
from pygame.locals import *

class navbar():
    def __init__(self, maxWidth, maxHeight):
        self.x = random.randrange(0, maxWidth, 1)
        self.y = random.randrange(0, maxHeight, 1)
        self.width = random.randrange(0, maxWidth, 1)
        self.height = random.randrange(0, maxHeight, 1)
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth, 1)
            self.y = random.randrange(0, maxHeight, 1)
            self.width = random.randrange(0, maxWidth, 5)
            self.height = random.randrange(0, maxHeight, 5)
    
    def fitness(self, maxWidth):
        fitness = 0
        if self.y < 10:
            fitness += 3
        elif self.y > 50:
            fitness -= 1
        if self.x < 10 and self.width >= maxWidth - 10 and self.width <= maxWidth:
            fitness += 4
        if self.height <= 50:
            fitness += 3
        elif self.height > 50:
            fitness -= 1
        if self.height > self.width:
            fitness -= 3
        elif self.width > self.height:
            fitness += 1
        return fitness

    def display(self, screen):
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (82, 148, 255), rect)