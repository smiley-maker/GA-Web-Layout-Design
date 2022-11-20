import random
import numpy as np
import copy

#Color class to define an R, G, B color
class color:
    #Constructor that either accepts specific red, green, and blue values or randomly generates them
    def __init__(self, red=None, green=None, blue=None):
        if red != None:
            self.red = red
        else:
            self.red = random.randint(0, 255)
        if green != None:
            self.green = green
        else:
            self.green = random.randint(0, 255)
        if blue != None:
            self.blue = blue
        else:
            self.blue = random.randint(0, 255)
    
    def randomize(self):
        #Function to change each R, G, B value in a given color
        rate = 100 #Change in mutation
        mod = random.randint(-rate, rate)
        while not 0 <= self.red + mod <= 255:
            mod = random.randint(-rate, rate)
        self.red += mod
        mod = random.randint(-rate, rate)
        while not 0 <= self.green + mod <= 255:
            mod = random.randint(-rate, rate)
        self.green += mod
        mod = random.randint(-rate, rate)
        while not 0 <= self.blue + mod <= 255:
            mod = random.randint(-rate, rate)
        self.blue += mod
    
    def display(self):
        #Simply prints the R, G, and B values in a color
        print("(%f, %f, %f)" % (self.red, self.green, self.blue))
    
    def luminance(self):
        #Function to calculate the luminance of a color
        #Formats the values
        R = self.red/255
        G = self.green/255
        B = self.blue/255
        #Calculates luminance based on a specific formula
        lum = 0.2126*R + 0.7152*G + 0.0722*B
        return lum
    
    def copy(self):
        #Copies a color
        return copy.copy(self)