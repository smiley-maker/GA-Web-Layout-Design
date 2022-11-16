import random
from internet import *
from website import *
import copy

def runGA(populationSize, crossoverRate, mutationRate, windowHeight, windowWidth):
    newNet = internet(populationSize, windowWidth, windowHeight)
    for j in range(300):
        net = internet(populationSize, windowWidth, windowHeight)
        net.sortByFitness()
        for i in range(int(populationSize/2)):
            site1, site2 = net.selectPair()
            if random.random() < crossoverRate:
                net.crossover(site1, site2)
            site1.mutate(mutationRate, windowWidth, windowHeight)
            site2.mutate(mutationRate, windowWidth, windowHeight)
            newNet.addWebsite(site1)
            newNet.addWebsite(site2)
            net = copy.copy(newNet)
        bestFitness, index = net.evaluateFitness()
        if j%200 == 0:
            net.displays(windowWidth, windowHeight, index)
            print(bestFitness)

runGA(24, 0.85, 0.05, 500, 500)