import os
import numpy as np
import pandas as pd
from ctgan import *

data = pd.read_csv('multihazard.csv')
data.columns

data.drop(['Unnamed: 0'], axis=1, inplace=True)
# data.reset_index(inplace = True)

discrete_columns = ['ID_unique', 'ID_unique_haz', 'event_magnitude', 'EQ2y', 'EQ5y',
       'EQ10y', 'EQ25y', 'EQ50y', 'EQ100y', 'EQ200y', 'EQ500y', 'EQ1000y',
       'EQ5000y', 'EQ10000y', 'fdem25fj', 'FL1700', 'FL2000', 'FL2300',
       'FL2500', 'FL2900', 'SB_FL1700', 'SB_FL2000', 'SB_FL2300', 'SB_FL2500',
       'SB_FL2900', 'LSeq', 'LSrf', 'RF10y', 'RF20y', 'RF50y', 'RF100y',
       'AREA', 'SLP_mean', 'W_area', 'SLP_mean_haz', 'distance', 'angle']

from ctgan import CTGANSynthesizer

ctgan = CTGANSynthesizer()
ctgan.fit(data, discrete_columns, epochs=1)