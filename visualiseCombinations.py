import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from processInput import processInput
from fillBags import fillOneBag

fileName = 'gifts.csv'

giftList, giftListSummary = processInput( fileName )

nHorse = 0
nBall = 0
nBike = 0
nTrain = 0
nCoal = 0
nBook = 0
nDoll = 0
nBlocks = 0
nGloves = 0

for nGloves in np.arange(1,20):
    itemCount = np.array([nHorse,nBall,nBike,nTrain,nCoal,nBook,nDoll,nBlocks,nGloves])

    sumWeights = fillOneBag(itemCount, giftListSummary)

    #plt.cla()
    #plt.clf()
    #plt.close()
    #
    #n, bins, patches = plt.hist(sumWeights,50,normed=1)
    ##plt.plot(bins)
    #plt.xlabel('weight')
    #plt.ylabel('density')
    #plt.title('[0,0,0,0,1,1,1,0,1], mean =' + str(np.mean(sumWeights)) + ' , std =' + str(np.std(sumWeights)))
    #plt.show()
    #


    origWeight = np.mean(sumWeights)

    sumWeights[sumWeights>=50]=0

    newWeight = np.mean(sumWeights)

    print itemCount, "Approx. Bag Weight = ", newWeight, " Lost Weight = ", origWeight-newWeight