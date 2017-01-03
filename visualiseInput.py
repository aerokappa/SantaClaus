import numpy as np
import pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from processInput import processInput

def visualiseInput( ):
    fileName = 'gifts.csv'
    giftList = processInput( fileName )

    GiftTypes = giftList['GiftType'].unique()
    
    print GiftTypes
    
    nGiftTypes = len(GiftTypes)
    
    k = -1
    plt.cla()
    plt.clf()
    plt.close()
    
    for i in np.arange(3):
        for j in np.arange(3):
            k = k+1
            num_bins = 20
            plt.subplot(3,3,k+1)
            n, bins, patches = plt.hist(giftList['GiftWeight'][giftList['GiftType']==GiftTypes[k]],50,normed=1)
            #plt.plot(bins)
            #plt.xlabel('weight')
            plt.ylabel('density')
            plt.title(GiftTypes[k])
            plt.show()