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
    origOldWeight = np.mean(oldSumWeights)
    oldSumWeights[oldSumWeights>50] = 0
    oldWeight = np.mean(oldSumWeights)
    
    newWeight = oldWeight
    
    iter = 0
    tol = 0.1
    
    print 'iter: {0:03d}, mean_newWeight: {1:07.3f}, mean_lostWeight: {2:07.3f}, std_newWeight: {3:07.3f}, numItems: {4:03d}, {5}'.format(iter, oldWeight, origOldWeight-oldWeight, np.std(oldSumWeights), sum(itemCount), itemCount)    
    
    while ((newWeight-oldWeight)>tol or iter == 0):
        
        oldWeight = newWeight
        
        gradWeights = calcGradient( itemCount, giftListSummary )
        
        ind_max= np.argmax(gradWeights)
        if (gradWeights[ind_max]>0):
            itemCount[ind_max] += 1
        else:
            break
        
        newSumWeights = fillOneBag(itemCount, giftListSummary)
        origNewWeight = np.mean(newSumWeights) 
        newSumWeights[newSumWeights>50] = 0
        newWeight = np.mean(newSumWeights)    
            
        iter += 1
        print 'iter: {0:03d}, mean_newWeight: {1:07.3f}, mean_lostWeight: {2:07.3f}, std_newWeight: {3:07.3f}, numItems: {4:03d}, {5}'.format(iter, newWeight, origNewWeight-newWeight, np.std(newSumWeights), sum(itemCount), itemCount)