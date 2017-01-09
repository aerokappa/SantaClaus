import numpy as np
import pandas as pd
import random

def genGiftIDs( giftListSummary ):
    allBags = {}
    for i, giftType in enumerate(giftListSummary.GiftType):
        
        nGiftsOfGiftType = giftListSummary.nGifts[i]
        
        allBags[giftType] = []
        
        for j in np.arange(nGiftsOfGiftType):
            allBags[giftType].append((giftType+'_'+str(j)))
        
        random.shuffle(allBags[giftType])
        
    return allBags