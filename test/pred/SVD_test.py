import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from copy import copy
import pudb

df = pd.read_csv("test.csv", sep=',')
cols = df.columns.values
a = df.values
temp = copy(a)
where_are_NANS = np.isnan(a)
a[where_are_NANS] = 0
m,n = a.shape

for i in xrange(0,n):
	col = cols[i]
	weighted_avg = np.sum(a[:,i])/np.sum(df[col]>0.0)
	temp_col = temp[:,i]
	where_are_NANS_col = np.isnan(temp_col)
	temp_col[where_are_NANS_col] = weighted_avg
	a[:,i] = temp_col

k=7	
U, s, Vh = svds(a, k) # k is the number of factors

sigma = np.zeros((k, k))
for i in range(k):
    sigma[i, i] = s[i]

a1 = np.dot(U, np.dot(sigma, Vh))
pu.db