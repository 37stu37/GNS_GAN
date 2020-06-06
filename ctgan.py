"""
pip install ctgan
pip3 install --upgrade pandas
"""
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import ctgan
import time

data = pd.read_csv('FFEsample1perc.csv')
data.drop(['Unnamed: 0', 'scenario', 'pid'], axis=1, inplace=True)

# sample = data.sample(frac=0.01)
# print(len(sample))
sample = data

discrete_columns = ['source', 'target']


ctgan = ctgan.CTGANSynthesizer()
fit_time = time.time()
e=85
ctgan.fit(sample, discrete_columns, epochs=e)
endFit_time = time.time()-fit_time
print("{} epochs finished in {}".format(e, endFit_time))
GANsamples = ctgan.sample(1000000)