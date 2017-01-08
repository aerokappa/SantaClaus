from processInput import processInput
from automaticOptimization import *

from optimize import *

import numpy as np
import pandas as pd
from tempfile import TemporaryFile


fileName = 'gifts.csv'
giftList, giftListSummary = processInput( fileName )

#nHorse = 0
#nBall = 0
#nBike = 2
#nTrain = 0
#nCoal = 0
#nBook = 0
#nDoll = 0
#nBlocks = 0
#nGloves = 0
#    
#for i in np.arange(0,5):
#    
#    nBook = i
#    
#    print 'nBooks: ', i
#    itemCount = np.array([nHorse,nBall,nBike,nTrain,nCoal,nBook,nDoll,nBlocks,nGloves])
#    optimizeBagWeight( itemCount, giftListSummary )
#    print

allBags = genUseCases()

b_mean, b_std = getBagWeights(allBags, giftListSummary)

np.savez("data", allBags, b_mean, b_std)