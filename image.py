import random
import pygame
from pygame.locals import *

class image():
    def __init__(self, maxWidth, maxHeight):
        self.x = random.randint(0, maxWidth)
        self.y = random.randint(0, maxHeight)
        self.width = random.randint(0, maxWidth)
        self.height = random.randint(0, maxHeight)
    
    def mutate(self, mutationRate, maxWidth, maxHeight):
        if random.random() < mutationRate:
            self.x = random.randrange(0, maxWidth, 1)
            self.y = random.randrange(0, maxHeight, 1)
            self.width = random.randrange(0, maxWidth, 5)
            self.height = random.randrange(0, maxHeight, 5)
    
    def fitness(self, maxWidth):
        fitness = 0
        if self.x < maxWidth-30 and self.width >= maxWidth/2:
            fitness += 4
        if self.height >= 150:
            fitness += 3
        elif self.height < 50:
            fitness -= 1
        return fitness

    def display(self, screen):
        rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255, 233, 176), rect)