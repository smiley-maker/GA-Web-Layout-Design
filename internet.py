from website import *
import numpy as np


class internet:
    def __init__(self, size, windowWidth, windowHeight):
        self.internetSize = size
        self.internet = []
        for i in range(self.internetSize):
            w = website(windowWidth, windowHeight)
            self.internet.append(w)
    
    def sortByFitness(self):
        tuples = [(web.fitness(), web) for web in self.internet]
        tuples.sort(key=lambda x: x[0])
        sortedFitnessValues = [f for (f,g) in tuples]
        sortedWebsites = [g for (f, g) in tuples]
        return sortedWebsites, sortedFitnessValues

    def selectPair(self):
        weight = list(range(len(self.internet)))
        total = sum(weight)
        cost = [w/total for w in weight]
        choiceOne = np.random.choice(self.internet, p = cost)
        choiceTwo = np.random.choice(self.internet, p = cost)
#        newPop = self.sortByFitness()
        return (choiceOne, choiceTwo)
    
    def crossover(self, site1, site2):
        crossoverPoint = random.randrange(0, len(site1.web), 1)
        newSite1 = site1.web[0:crossoverPoint] + site2.web[crossoverPoint:]
        newSite2 = site2.web[0:crossoverPoint] + site1.web[crossoverPoint:]
        return newSite1, newSite2

    def addWebsite(self, web):
        self.internet.append(web)
    
    def displays(self, windowWidth, windowHeight, index):
#        if index == -1:
 #           print(self.internet[index].fitness())
  #          self.internet[index].display(windowWidth, windowHeight, True)
#        for i in range(int(len(self.internet))):
        self.internet[index].display(windowWidth, windowHeight, True)
#            print(len(self.internet))
#        if index%1000 != 0:
 #           self.internet[index].display(windowWidth, windowHeight, False)
  #          print(self.internet[index].fitness())
   #     elif index%1000 == 0:
    #        self.internet[index].display(windowWidth, windowHeight, True)
                
                #print(i)