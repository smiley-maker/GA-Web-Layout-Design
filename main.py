import random
from internet import *
from website import *
import copy
import numpy as np
import pandas as pd

#This function runs the genetic algorithm (GA) using various parameters that we can fine tune
#to get different results. The window height and width will be used to create a canvas of that
#size using pygame and then to display all components of a website. 
def runGA(populationSize, crossoverRate, mutationRate, windowHeight, windowWidth):
    #Variables used for data collection
    bestList = []
    avgBest = []
    #Creates a dummy internet variable
    newNet = internet(populationSize, windowWidth, windowHeight)
    #Loops through a designated (1000 here) number of generations
    for j in range(1000):
        #Creates a new random internet with a given number of websites. 
        net = internet(populationSize, windowWidth, windowHeight)
        net.internet , _ = net.sortByFitness(windowWidth, windowHeight) #Sorts the websites by their fitnesses
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
        outwebs , fitnessess = net.sortByFitness(windowWidth, windowHeight) #Re-sorts by fitness to make it easier to see result
#        bestList.append(fitnessess[-1]) #Appends the current best fitness to the list (to make a graph later)

#    outwebs[-1].display(windowWidth, windowHeight, True, True, "websites/finalGen.png")
        if j%50 == 0: #I didn't want to see all 300 generations of internets, so this shows every 50th (and just one site from each). 
            print(j)
            #avgBest.append(np.mean(bestList)) #Calculates the mean of the current best list every 50th generation
            #bestList = [] #Resets best list
            outwebs[-1].display(windowWidth, windowHeight, True, True, "websites/website-"+str(j)+".png") #Displays website & saves image to file
            print(fitnessess[-1]) #Prints associated fitness value

    #df = pd.DataFrame(avgBest, columns=["Average Best"]) #Creates a dataframe with average best fitness for analysis
    #df.to_csv("fitness-l.csv", index=False) #Creates a csv file to be used in excel for charts
            

runGA(60, 0.9, 0.1, 750, 1200) #Runs the genetic algorithm with a population size of 60, 90% crossover rate, 10% mutation rate, and a window size of 1200 x 750. 