from processInput import processInput
from findGiftWeight import findGiftWeight

import numpy as np
import pandas as pd

    
#
# Gift types and number of gift types have been hardcoded here.
#


def fillOneBag( itemCount, giftListSummary ):
    
    n = 10000
        
    nGiftTypes = len(giftListSummary['GiftType'])
    
    giftWeights = np.zeros(n)
    
    for i in np.arange(nGiftTypes):
        giftType = giftListSummary['GiftType'][i]
        for j in np.arange(itemCount[i]):
            giftWeights = np.vstack((giftWeights, findGiftWeight(giftType,n)))
    
    sumWeights = sum(giftWeights,0)
        
    return sumWeights      