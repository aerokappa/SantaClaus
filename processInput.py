from loadInput import loadInput
from findGiftWeight import findGiftWeight
import numpy as np
import pandas as pd

def processInput( fileName ):
    
    giftList = loadInput( fileName )
    nGifts = len(giftList)
    giftList['GiftType'] = giftList.GiftId.apply(lambda x: x.split('_')[0])
    giftList['GiftWeight'] = np.zeros(nGifts)
    giftList['GiftWeight'] = giftList.GiftType.apply(lambda x: findGiftWeight(x,1)[0])
        
    giftListSummary = pd.DataFrame()
    giftListSummary['GiftType'] = giftList['GiftType'].unique()
    nGiftTypes = len(giftListSummary['GiftType'])
    
    giftListSummary['nGifts'] = giftListSummary.GiftType.apply(lambda x : len(giftList[giftList['GiftType']==x]))
    giftListSummary['weight_average'] = np.zeros(nGiftTypes)
    giftListSummary['weight_STD'] = np.zeros(nGiftTypes)
    
    n = 100000 #an arbitrarily large number for statistical analysis
    
    for i in np.arange(nGiftTypes):
        x = findGiftWeight(giftListSummary['GiftType'][i], n)
        giftListSummary['weight_average'][i] = np.average(x)
        giftListSummary['weight_STD'][i] = np.std(x)

    return giftList, giftListSummary