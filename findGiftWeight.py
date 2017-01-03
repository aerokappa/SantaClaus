import numpy as np
import pandas as pd

def glovesWeight ( n ):
    x = np.random.rand( n )
    x[x<0.3] += 3
    return x
    
#
# Gift types and number of gift types have been hardcoded here.
#

def findGiftWeight( GiftType, n ):
    dispatcher = {'horse' : (np.maximum(0, np.random.normal(5,2,n))),
    'ball' : (np.maximum(0, 1 + np.random.normal(1,0.3,n))),
    'bike' : (np.maximum(0, np.random.normal(20,10,n))),
    'train' : (np.maximum(0, np.random.normal(10,5,n))),
    'coal' : (47 * np.random.beta(0.5,0.5,n)),
    'book' : (np.random.chisquare(2,n)),
    'doll' : (np.random.gamma(5,1,n)),
    'blocks' : (np.random.triangular(5,10,20,n)),
    'gloves' : (glovesWeight(n))}
    
    return dispatcher[GiftType]