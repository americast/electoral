import pandas as pd
import pudb
import numpy
from copy import copy
import math

K = 5
df = pd.read_csv('test.csv', sep=',').values
print df

where_are_NaNs = numpy.isnan(df)
df[where_are_NaNs] = 0


def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in xrange(steps):
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P,Q)
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in xrange(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        if e < 0.001:
            break
    return P, Q.T


N = len(df)
M = len(df[0])

P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)

nP, nQ = matrix_factorization(df, P, Q, K)
nR = numpy.dot(nP, nQ.T)

result = copy(df)
result[where_are_NaNs] = nR[where_are_NaNs]

count = 0

original = df[~where_are_NaNs]
predicted = nR[~where_are_NaNs]
error_mae = 0.0
error_rmse = 0.0

for i in xrange(len(original)):
	error_mae  += math.fabs(original[i] - predicted[i])
	error_rmse += math.pow((original[i] - predicted[i]), 2)
	count += 1

error_mae /= count
error_rmse = math.sqrt(error_rmse / count)

print ("error_mae: ", error_mae)
print ("error_rmse: ", error_rmse)

numpy.savetxt("predicted_nmf_text.txt", result)

pu.db