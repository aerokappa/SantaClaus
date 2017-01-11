import numpy as np
import pandas as pd

from processInput import processInput
from fillBags import fillOneBag

npz = np.load('optWeightMatrix.npz')
print npz.files

A = npz['arr_0']
approxSol = [47, 76, 333, 142, 57, 23, 230, 92]

fileName = 'gifts.csv'
giftList, giftListSummary = processInput( fileName )

itemCountMatrix = A.transpose() 

print approxSol
print itemCountMatrix

for i in np.arange(itemCountMatrix.shape[0]):
    origWeights = fillOneBag(itemCountMatrix[i], giftListSummary)
    origWeight  = np.mean(origWeights)
    origWeights[origWeights>50] = 0
    newWeight  = np.mean(origWeights)
    print 'Orig: {1:07.3f}, New: {2:07.3f}, Lost: {3:07f}, Total Lost: {4:07.3f}, Bag Contents: {0}'.format(itemCountMatrix[i], origWeight, newWeight, origWeight-newWeight, (origWeight-newWeight)*approxSol[i])