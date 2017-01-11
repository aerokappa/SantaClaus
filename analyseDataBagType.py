import numpy as np
from scipy.optimize import linprog

from processInput import processInput
from genGiftIDs import genGiftIDs

npz = np.load('allData.npz')
print npz.files

allBags = npz['arr_0']
b_mean  = npz['arr_1']
b_std   = npz['arr_2']

print allBags
print b_mean
print b_std

allowedBags = np.sum(allBags,axis=1)>3
sortedOrder = np.argsort(-b_mean[allowedBags])

bm = b_mean[allowedBags][sortedOrder]
bs = b_std[allowedBags][sortedOrder]
ab = allBags[allowedBags][sortedOrder]

nBags  = ab.shape[0]
nGiftTypes = ab.shape[1]

A = np.matrix(np.hstack((np.ones((nBags,1)),ab))).transpose()
w = np.matrix(bm).transpose()

nGifts = np.matrix([[1000],[1000],[1100],[500],[1000],[166],[1200],[1000],[1000],[200]])

sol = linprog(-bm,A,nGifts,options={"disp":True})

print A[:,sol.x!=0]*np.matrix(sol.x[sol.x!=0]).transpose(), sum(bm[sol.x!=0]*sol.x[sol.x!=0])


approxSol = [47, 76, 333, 142, 57, 23, 230, 92]

print A[:,sol.x!=0]*np.matrix(approxSol).transpose(), sum(bm[sol.x!=0]*approxSol)

### Old code ###

fileName = 'gifts.csv'

giftList, giftListSummary = processInput( fileName )
    
packedBags = []
    
#
# after random gift IDs were generated
#
giftIDs = genGiftIDs( giftListSummary )
    
for i in np.arange(1000):
    if (i%100 == 0):
        print i
    currentBag = []
        
    #if (i< 333):   
    #    itemCount = np.array([0 ,3 ,0 ,0 ,0 ,0 ,0 ,3 ,0])
    #elif ((i>=333) & (i<458)):
    #    itemCount = np.array([8, 0, 0, 0, 0, 0, 0, 0, 0])            
    #elif ((i>=458) & (i<583)):
    #    itemCount = np.array([0, 0, 0, 0, 0, 0, 8, 0, 0])
    #elif ((i>=583) & (i<916)):
    #    itemCount = np.array([0, 0, 0, 3, 0, 2, 0, 0, 0])
    #elif ((i>=916) & (i<924)):
    #    itemCount = np.array([ 0,  0,  0,  0,  0,  0,  0,  0, 25])
    #elif ((i>=924) & (i<928)):
    #    itemCount = np.array([ 0, 23,  0,  0,  0,  0,  0,  0,  0])
    #elif ((i>=928) & (i<938)):
    #    itemCount = np.array([ 0,  0,  0,  0,  0, 19,  0,  0,  0])
    #elif ((i>=938) & (i<939)):
    #    itemCount = np.array([ 0,  0,  0,  0,  0, 11,  0,  1,  0])
    #elif ((i>=939) & (i<940)):
    #    itemCount = np.array([0, 9, 0, 1, 0, 0, 0, 0, 0])
    #else:
    #    itemCount = np.array([0, 0, 1, 0, 0, 5, 0, 0, 0])
        
    for j in np.arange(len(approxSol)):
        if ((i>=sum(approxSol[:j])) & (i<sum(approxSol[:j+1]))):
            itemCount  = np.array(A[1:,sol.x!=0][:,j].transpose())[0]
                
    #
    #before random gift IDs were generated
    #
    #for k in np.arange(len(itemCount)):
    #    if (itemCount[k] <= giftListSummary['nGiftsNotPacked'][k]):
    #        for j in np.arange(itemCount[k]):
    #            giftName = giftListSummary['GiftType'][k]
    #            currGiftID = giftListSummary['nGiftsPacked'][k]
    #            currentBag.append(giftName+'_'+str(currGiftID))
    #            giftListSummary['nGiftsPacked'][k] += 1
    #            giftListSummary['nGiftsNotPacked'][k] -= 1

    if ((i>=sum(approxSol[:6])) & (i<sum(approxSol[:7]))):
        for k in np.arange(len(itemCount)):
            if (itemCount[k] <= giftListSummary['nGiftsNotPacked'][k]):
                for j in np.arange(itemCount[k]):
                    giftName = giftListSummary['GiftType'][k]
                    currGiftID = giftListSummary['nGiftsPacked'][k]
                    currentBag.append(giftIDs[giftName].pop())
                    giftListSummary['nGiftsPacked'][k] += 1
                    giftListSummary['nGiftsNotPacked'][k] -= 1
                
        packedBags.append(currentBag)
    
# Write to File 'submission.csv'

subFile = open('./submissions/submission_TrainBook_randomised_1.csv','w')
subFile.write('Gifts\n')

for currentBag in packedBags:
    subFile.write(currentBag[0])
    for currentItem in currentBag[1:]:
        subFile.write(' ')
        subFile.write(currentItem)
    subFile.write('\n')
subFile.close()