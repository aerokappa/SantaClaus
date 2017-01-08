import numpy as np
import pandas as pd
import itertools
from fillBags import fillOneBag

def genUseCases ( ):
    nHorse = 0
    nBall = 0
    nBike = 0
    nTrain = 0
    nCoal = 0
    nBook = 0
    nDoll = 0
    nBlocks = 0
    nGloves = 0
    
    wHorse = 5
    wBall = 2
    wBike = 20
    wTrain = 10
    wCoal = 23
    wBook = 2
    wDoll = 5
    wBlocks = 10
    wGloves = 2
    
    targetWeight = 50
    
    return np.array([np.array([ nHorse, nBall, nBike, nTrain, nCoal, nBook, nDoll, nBlocks, nGloves]) \
    for nCoal   in np.arange(0, (targetWeight)/wCoal + 1) \
    for nBike   in np.arange(0, (targetWeight - nCoal*wCoal)/wBike + 1) \
    for nTrain  in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike)/wTrain + 1) \
    for nBlocks in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike - nTrain*wTrain)/wBlocks + 1) \
    for nHorse  in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike - nTrain*wTrain - nBlocks*wBlocks)/wHorse + 1) \
    for nDoll   in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike - nTrain*wTrain - nBlocks*wBlocks - nHorse*wHorse)/wDoll + 1) \
    for nBall   in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike - nTrain*wTrain - nBlocks*wBlocks - nHorse*wHorse - nDoll*wDoll)/wBall + 1) \
    for nBook   in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike - nTrain*wTrain - nBlocks*wBlocks - nHorse*wHorse - nDoll*wDoll - nBall*wBall)/wBook + 1) \
    for nGloves in np.arange(0, (targetWeight - nCoal*wCoal - nBike*wBike - nTrain*wTrain - nBlocks*wBlocks - nHorse*wHorse - nDoll*wDoll - nBall*wBall - nBook*wBook)/wGloves + 1) \
    ])
    
def getBagWeights( bagItemCounts, giftListSummary ):
    
    bagList = genUseCases()
    
    nBags = len(bagList)
    bagWeight_mean = np.zeros(nBags)
    bagWeight_std  = np.zeros(nBags)
    
    for i, currBag in enumerate(bagList):
        print nBags, i
        bagWeights = fillOneBag( currBag, giftListSummary)
        if np.size(bagWeights) != 1:
            bagWeights[ bagWeights >= 50 ] = 0
        bagWeight_mean[i] = np.mean(bagWeights)
        bagWeight_std[i] = np.std(bagWeights)
        
    return bagWeight_mean, bagWeight_std