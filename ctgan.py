"""
pip install ctgan
pip3 install --upgrade pandas
"""

import pandas as pd
import ctgan
# from ctgan import CTGANSynthesizer

data = pd.read_csv('big_sampleV2.csv')
data.columns

sample = data.sample(20000)

discrete_columns = ['ID_unique', 'ID_unique_haz']
       # , 'event_magnitude', 'EQ2y', 'EQ5y',
       # 'EQ10y', 'EQ25y', 'EQ50y', 'EQ100y', 'EQ200y', 'EQ500y', 'EQ1000y',
       # 'EQ5000y', 'EQ10000y', 'fdem25fj', 'FL1700', 'FL2000', 'FL2300',
       # 'FL2500', 'FL2900', 'SB_FL1700', 'SB_FL2000', 'SB_FL2300', 'SB_FL2500',
       # 'SB_FL2900', 'LSeq', 'LSrf', 'RF10y', 'RF20y', 'RF50y', 'RF100y',
       # 'AREA', 'SLP_mean', 'W_area', 'SLP_mean_haz', 'distance', 'angle']


ctgan = ctgan.CTGANSynthesizer()
ctgan.fit(sample, discrete_columns, epochs=5)
GANsamples = ctgan.sample(1000)


# ## options for scoring the model
# y_hat, test_features = lgb_model.predict(X_test)
# # check score
# test_score = roc_auc_score(y_test, y_hat)