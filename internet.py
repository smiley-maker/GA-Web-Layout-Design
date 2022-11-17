################################################ Internet Class #################################################
#Imports
from website import *
import numpy as np
class internet:
    def __init__(self, size, windowWidth, windowHeight):
        #Constructor to initialize a list of websites
        self.internetSize = size #Sets the size variable
        self.internet = [] #Creates an empty list to store a certain number of websites
        for i in range(self.internetSize): #Loops through the given size
            w = website(windowWidth, windowHeight)  #creates a new website
            self.internet.append(w) #Uploads that website to the internet (:
    
    def sortByFitness(self):
        #Function to sort the websites in the internet by their fitness values
        tuples = [(web.fitness(), web) for web in self.internet] #Calculates fitness for each site
        tuples.sort(key=lambda x: x[0]) #Sorts through the first value (fitness value) using a sort function
        sortedFitnessValues = [f for (f,g) in tuples] #Retrieves just the fitness values
        sortedWebsites = [g for (f, g) in tuples] #Retrieves just the websites
        return sortedWebsites, sortedFitnessValues #Returns those lists
    
    def selectPair(self):
        #Function to select the top two websites for a given generation
        weight = list(range(len(self.internet))) #Creates a list going from 0 to the length of the internet
        total = sum(weight) #Totals the list
        cost = [w/total for w in weight] #Calculates a respective weight for each sorted website in the internet list
        choiceOne = np.random.choice(self.internet, p = cost) #Chooses two random websites from the list using a cost variable
        choiceTwo = np.random.choice(self.internet, p = cost)
#        newPop = self.sortByFitness()
        return (choiceOne, choiceTwo) #Returns the selected sites

    def evaluateFitness(self):
        #Function to evaluate the fitness of an entire internet
        avgFitness = 0 #Variable to store the average fitness
        bestFitness = 0 #Variable to store the best fitness
        index = 0 #Index at which the best fitness occurred
        for i in range(len(self.internet)): #Loops through the length of the internet
            fitnessLevel = self.internet[i].fitness() #Calculates the fitness of each website in the internet
            avgFitness += fitnessLevel #Adds the current fitness to the average fitness variable
            if fitnessLevel > bestFitness: #If the current fitness is greater than the previous best fitness,
                bestFitness = fitnessLevel #update best fitness
                index = i #update the index
        avgFitness = avgFitness / len(self.internet) #Calculate average
        return bestFitness, index #Returns the best fitness and the index it occurred at
    
    def crossover(self, site1, site2):
        #Function to perform a crossover between two websites
        crossoverPoint = random.randrange(0, len(site1.web), 1) #Randomly selects a point to split at
        #Splits each input based on the point and adds each half together
        newSite1 = site1.web[0:crossoverPoint] + site2.web[crossoverPoint:]
        newSite2 = site2.web[0:crossoverPoint] + site1.web[crossoverPoint:]
        return newSite1, newSite2

    def addWebsite(self, web):
        #Simply appends a new website to the internet
        self.internet.append(web)
    
    def displays(self, windowWidth, windowHeight, index):
        #Displays the current website
        self.internet[index].display(windowWidth, windowHeight, True)