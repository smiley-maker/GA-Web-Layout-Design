import random
from internet import *
from website import *
import copy


#This function runs the genetic algorithm (GA) using various parameters that we can fine tune
#to get different results. The window height and width will be used to create a canvas of that
#size using pygame and then to display all components of a website. 
def runGA(populationSize, crossoverRate, mutationRate, windowHeight, windowWidth):
    #Creates a dummy internet variable
    newNet = internet(populationSize, windowWidth, windowHeight)
    #Loops through a designated (300 here) number of generations
    for j in range(300):
        #Creates a new random internet with a given number of websites. 
        net = internet(populationSize, windowWidth, windowHeight)
        net.sortByFitness() #Sorts the websites by their fitnesses
        #Loops through half the population size
        for i in range(int(populationSize/2)):
            site1, site2 = net.selectPair() #Selects two websites that performed the best
            if random.random() < crossoverRate: #Possibly performs crossover (random chance)
                net.crossover(site1, site2) #Uses the crossover method to take part of one website and add it to the other and vice versa
            site1.mutate(mutationRate, windowWidth, windowHeight) #Mutates the first selected site
            site2.mutate(mutationRate, windowWidth, windowHeight) #Mutates the second selected site
            newNet.addWebsite(site1) #Adds the new websites to the new internet variable
            newNet.addWebsite(site2)
            net = copy.copy(newNet) #Makes a copy of the dummy internet variable
        bestFitness, index = net.evaluateFitness() #Calculates the best performing website for the given generation
        if j%50 == 0: #I didn't want to see all 300 generations of internets, so this shows every 50th (and just one site from each). 
            net.displays(windowWidth, windowHeight, index)
            print(bestFitness)

runGA(24, 0.85, 0.05, 500, 500)