import random
from internet import *
from website import *
import copy

def runGA(populationSize, crossoverRate, mutationRate, windowHeight, windowWidth):
    newNet = internet(populationSize, windowWidth, windowHeight)
    for j in range(1000):
        net = internet(populationSize, windowWidth, windowHeight)
        net.sortByFitness()
        for i in range(int(populationSize/2)):
            site1, site2 = net.selectPair()
            if random.random() < crossoverRate:
                net.crossover(site1, site2)
            site1.mutate(mutationRate, windowWidth, windowHeight)
#            print(site1)
            site2.mutate(mutationRate, windowWidth, windowHeight)
 #           print(site2)
  #          print(net.internet)
            newNet.addWebsite(site1)
            newNet.addWebsite(site2)
            net = copy.copy(newNet)
   #         newNet = internet(populationSize, windowWidth, windowHeight)
#        print(net.internet[-1].fitness())
        bestFitness, index = net.evaluateFitness()
        #net.displays(windowWidth, windowHeight, index)
        if j%100 == 0:
            net.displays(windowWidth, windowHeight, index)
            print(bestFitness)

runGA(6, 1, 0.25, 500, 500)