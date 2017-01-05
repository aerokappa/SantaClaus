from processInput import processInput
from optimize import *

import numpy as np
import pandas as pd

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
    
itemCount = np.array([nHorse,nBall,nBike,nTrain,nCoal,nBook,nDoll,nBlocks,nGloves])

optimizeBagWeight( itemCount )