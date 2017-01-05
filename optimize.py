import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from processInput import processInput
from fillBags import fillOneBag

def calcGradient( itemCount, giftListSummary ):

    nGiftTypes = len(giftListSummary['GiftType']) #number of gift types
    
    gradWeights = np.zeros(nGiftTypes)
    
    sumWeightsBase = fillOneBag(itemCount, giftListSummary)
    sumWeightsBase[ sumWeightsBase >= 50 ] = 0
    baseWeight = np.mean(sumWeightsBase)
    
    for i in np.arange(nGiftTypes):
        
        itemCount[i] += 1 # increment to get gradient
                
        sumWeights = fillOneBag(itemCount, giftListSummary)
        sumWeights[sumWeights>=50]=0
        newWeight = np.mean(sumWeights)
    
        gradWeights[i] = (newWeight - baseWeight)/giftListSummary['weight_average'][i]
        
        #print itemCount, "Orig Bag Weight = ", baseWeight, " New Weight = ", newWeight
        
        itemCount[i] -= 1 # decrement back to base
        
    return gradWeights
    
    
def optimizeBagWeight( itemCount, giftListSummary ):

    oldSumWeights = fillOneBag(itemCount, giftListSummary)
    oldSumWeights[oldSumWeights>50] = 0
    oldWeight = np.mean(oldSumWeights)
    
    newWeight = oldWeight
    
    iter = 0
    tol = 0.1
    
    print iter, oldWeight, itemCount
    
    while ((newWeight-oldWeight)>tol or iter == 0):
        
        oldWeight = newWeight
        
        gradWeights = calcGradient( itemCount, giftListSummary )
        
        ind_max= np.argmax(gradWeights)
        if (gradWeights[ind_max]>0):
            itemCount[ind_max] += 1
        else:
            break
        
        newSumWeights = fillOneBag(itemCount, giftListSummary)
        newSumWeights[newSumWeights>50] = 0
        newWeight = np.mean(newSumWeights)    
            
        iter += 1
        print iter, newWeight, np.std(newSumWeights), itemCount