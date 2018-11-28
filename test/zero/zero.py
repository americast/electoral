import pandas as pd
import pudb
import numpy
from copy import copy
import math

df = pd.read_csv('test.csv', sep=',').values

where_are_NaNs = numpy.isnan(df)
df[where_are_NaNs] = 0
print df

numpy.savetxt("zero_text.txt", df)

# pu.db