import numpy as np
import pandas as pd

from processInput import processInput

def handCodedOptimum_v3 ( ):
    
    fileName = 'gifts.csv'
    
    giftList, giftListSummary = processInput( fileName )
    
    packedBags = []
    
    for i in np.arange(1000):
        print i
        currentBag = []
        
        if (i< 53):   
            itemCount = np.array([0,1,1,0,0,3,0,0,0])
        elif ((i>=53) & (i<54)):
            itemCount = np.array([0,1,1,0,0,0,0,1,0])            
        elif ((i>=54) & (i<62)):
            itemCount = np.array([0,0,0,0,0,0,0,0,25])
        elif ((i>=62) & (i<187)):
            itemCount = np.array([8,0,0,0,0,0,0,0,0])
        elif ((i>=187) & (i<312)):
            itemCount = np.array([0,0,0,0,0,0,8,0,0])
        elif ((i>=312) & (i<645)):
            itemCount = np.array([0,3,0,0,0,0,0,3,0])
        elif ((i>=645) & (i<978)):
            itemCount = np.array([0,0,0,3,0,3,0,0,0])
        elif ((i>=978) & (i<979)):
            itemCount = np.array([0,1,1,1,0,0,0,0,0])
        elif ((i>=979) & (i<996)):
            itemCount = np.array([0,2,1,0,0,2,0,0,0])
        else:
            itemCount = np.array([0,3,1,0,0,2,0,0,0])
            
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
    
    subFile = open('submission_3.csv','w')
    subFile.write('Gifts\n')
    
    for currentBag in packedBags:
        subFile.write(currentBag[0])
        for currentItem in currentBag[1:]:
            subFile.write(' ')
            subFile.write(currentItem)
        subFile.write('\n')
    subFile.close()
    return packedBags