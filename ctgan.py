"""
pip install ctgan
pip3 install --upgrade pandas
"""
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import ctgan
import time
from scipy.stats import ks_2samp

data = pd.read_csv('FFEsample1perc.csv')
data.columns
data.drop(['Unnamed: 0', 'scenario', 'pid'], axis=1, inplace=True)

# sample = data.sample(frac=0.5)

discrete_columns = ['source', 'target']


ctgan = ctgan.CTGANSynthesizer()
fit_time = time.time()
e=5
ctgan.fit(data, discrete_columns, epochs=e)
endFit_time = time.time()-fit_time
print("{} epochs finished in {}".format(e, endFit_time))
# GANsamples = ctgan.sample(1000)


# ## options for scoring the model
# y_hat, test_features = lgb_model.predict(X_test)
# # check score
# test_score = roc_auc_score(y_test, y_hat)

#test
# sns.pairplot(sample)
sns.set(style='white')
for (c, columnData) in sample.iteritems():
# for c in sample.columns:
    print(c)
    sns.jointplot(sample[c].sample(1000), GANsamples[c], kind="kde") # .annotate(stats.pearsonr)
    stats.ks_2samp(sample[c], GANsamples[c])