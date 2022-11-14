import random
import pygame
from pygame.locals import *

class button():
    def __init__(self, maxWidth, maxHeight):
        self.x = random.randint(0, maxWidth)
        self.y = random.randint(0, maxHeight)
        self.width = random.randint(0, maxWidth)
        self.height = random.randint(0, maxHeight)
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth, 1)
            self.y = random.randrange(0, maxHeight, 1)
            self.width = random.randrange(0, int(maxWidth/3), 1)
            self.height = random.randrange(0, int(maxHeight/3), 1)
    
    def fitness(self, maxWidth):
        fitness = 0
        if self.width <= 75:
            fitness += 2
        elif self.width < 15:
            fitness -= 1
        elif self.width >= 200:
            fitness -= 2
        if self.height <= 50:
            fitness += 3
        elif self.height > 50:
            fitness -= 1
        return fitness

    def display(self, screen):
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (238, 140, 255), rect)