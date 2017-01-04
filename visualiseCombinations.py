import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from processInput import processInput
from fillBags import fillOneBag

fileName = 'gifts.csv'

giftList, giftListSummary = processInput( fileName )

itemCount = np.array([0,0,1,0,0,7,0,0,0])

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

print newWeight, origWeight, origWeight-newWeight