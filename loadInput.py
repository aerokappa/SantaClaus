import numpy as np
import pandas as pd

def loadInput( fileName ):
    giftList = pd.read_csv( fileName, dtype=None, header=0 )
    return giftList