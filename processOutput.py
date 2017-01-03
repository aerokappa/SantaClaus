import numpy as np
import pandas as pd

from processInput import processInput

def processOutput( ):
    
    fileName = 'gifts.csv'
    
    giftList, giftListSummary = processInput( fileName )
    
    packedBags = []
    
    for i in np.arange(1000):
        print i
        currentBag = []        
        itemCount = np.array([1,1,0,1,0,1,1,1,0])

        for i in np.arange(len(itemCount)):
            if (itemCount[i] <= giftListSummary['nGiftsNotPacked'][i]):
                for j in np.arange(itemCount[i]):
                    giftName = giftListSummary['GiftType'][i]
                    currGiftID = giftListSummary['nGiftsPacked'][i]
                    currentBag.append(giftName+'_'+str(currGiftID))
                    giftListSummary['nGiftsPacked'][i] += 1
                    giftListSummary['nGiftsNotPacked'][i] -= 1
        packedBags.append(currentBag)
        
    # Write to File 'submission.csv'
    
    subFile = open('submission.csv','w')
    subFile.write('Gifts\n')
    
    for currentBag in packedBags:
        subFile.write(currentBag[0])
        for currentItem in currentBag[1:]:
            subFile.write(' ')
            subFile.write(currentItem)
        subFile.write('\n')
    subFile.close()
    return packedBags