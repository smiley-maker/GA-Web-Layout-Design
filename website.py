import random
from navbar import *
from image import *
from button import *
from text import *
import pygame
from pygame.locals import *

class website():
    def __init__(self, maxWidth, maxHeight):
        self.web = []
        self.web.append(navbar(maxWidth, maxHeight))
        self.web.append(image(maxWidth, maxHeight))
        self.web.append(button(maxWidth, maxHeight))
        self.web.append(text(maxWidth, maxHeight))

    def mutate(self, mutationRate, maxWidth, maxHeight):
        self.web[0].mutate(mutationRate, maxWidth, maxHeight)
        self.web[1].mutate(mutationRate, maxWidth, maxHeight)
        self.web[2].mutate(mutationRate, maxWidth, maxHeight)
        self.web[3].mutate(mutationRate, maxWidth, maxHeight)
    
    def fitness(self):
        fitness = self.web[0].fitness(500) + self.web[1].fitness(500) + self.web[2].fitness(500) + self.web[3].fitness(500)
        if self.web[1].x - self.web[3].x < 0 or self.web[3].x - self.web[1].x < 0: 
            fitness -= 3
        if self.web[3].y - self.web[2].y <= 30:
            fitness += 1
#        print(fitness)
        return fitness
    
    def display(self, maxWidth, maxHeight, isOn):
        pygame.init()
        screen = pygame.display.set_mode((maxWidth, maxHeight))
        running = False
        if isOn: running = True
#        print(running)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                screen.fill((255, 255, 255))
            for comp in self.web:
                comp.display(screen)
            pygame.display.flip()
        pygame.quit()