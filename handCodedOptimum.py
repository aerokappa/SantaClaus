import numpy as np
import pandas as pd

from processInput import processInput

def handCodedOptimum ( ):
    
    fileName = 'gifts.csv'
    
    giftList, giftListSummary = processInput( fileName )
    
    packedBags = []
    
    for i in np.arange(1000):
        print i
        currentBag = []
        
        if (i< 50):   
            itemCount = np.array([0,22,0,0,0,0,0,0,0])
        elif ((i>=50) & (i<58)):
            itemCount = np.array([0,0,0,0,0,0,0,0,25])            
        elif ((i>=58) & (i<183)):
            itemCount = np.array([8,0,0,0,0,0,0,0,0])
        elif ((i>=183) & (i<308)):
            itemCount = np.array([0,0,0,0,0,0,8,0,0])
        elif ((i>=308) & (i<641)):
            itemCount = np.array([0,0,0,0,0,0,0,3,0])
        elif ((i>=641) & (i<974)):
            itemCount = np.array([0,0,0,3,0,3,0,0,0])
        #elif ((i>=974) & (i<987)):
        #    itemCount = np.array([0,0,0,0,0,15,0,0,0])
        #elif ((i>=987) & (i<993)):
        #    itemCount = np.array([0,0,0,0,1,1,0,0,0])
        else:
            itemCount = np.array([0,0,1,0,0,7,0,0,0])
            
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