import numpy as np
import pandas as pd

from processInput import processInput

def handCodedOptimum_v4 ( ):
    
    fileName = 'gifts.csv'
    
    giftList, giftListSummary = processInput( fileName )
    
    packedBags = []
    
    for i in np.arange(1000):
        print i
        currentBag = []
        
        if (i< 333):   
            itemCount = np.array([0 ,3 ,0 ,0 ,0 ,0 ,0 ,3 ,0])
        elif ((i>=333) & (i<458)):
            itemCount = np.array([8, 0, 0, 0, 0, 0, 0, 0, 0])            
        elif ((i>=458) & (i<583)):
            itemCount = np.array([0, 0, 0, 0, 0, 0, 8, 0, 0])
        elif ((i>=583) & (i<916)):
            itemCount = np.array([0, 0, 0, 3, 0, 2, 0, 0, 0])
        elif ((i>=916) & (i<924)):
            itemCount = np.array([ 0,  0,  0,  0,  0,  0,  0,  0, 25])
        elif ((i>=924) & (i<928)):
            itemCount = np.array([ 0, 23,  0,  0,  0,  0,  0,  0,  0])
        elif ((i>=928) & (i<938)):
            itemCount = np.array([ 0,  0,  0,  0,  0, 19,  0,  0,  0])
        elif ((i>=938) & (i<939)):
            itemCount = np.array([ 0,  0,  0,  0,  0, 11,  0,  1,  0])
        elif ((i>=939) & (i<940)):
            itemCount = np.array([0, 9, 0, 1, 0, 0, 0, 0, 0])
        else:
            itemCount = np.array([0, 0, 1, 0, 0, 5, 0, 0, 0])
            
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
    
    subFile = open('submission_5.csv','w')
    subFile.write('Gifts\n')
    
    for currentBag in packedBags:
        subFile.write(currentBag[0])
        for currentItem in currentBag[1:]:
            subFile.write(' ')
            subFile.write(currentItem)
        subFile.write('\n')
    subFile.close()
    return packedBags