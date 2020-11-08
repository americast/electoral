import pandas as pd
import numpy
from copy import copy
import math
import datetime
import logging

logging.basicConfig(filename="app_numpy.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

print('INFO: Reading input')
logger.info('INFO: Reading Input')
K = 5
df = pd.read_csv('modelling.csv', sep=',').values

where_are_NaNs = numpy.isnan(df)
df[where_are_NaNs] = 0


def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    logger.info('INFO: Starting matrix factorization')
    print('INFO: Starting matrix factorization')
    try:
        for step in range(steps):
            print(f'\nINFO: Starting step {step+1}/{steps}')
            logger.info(f'INFO: Starting step {step+1}/{steps}')
            a = datetime.datetime.now()
            # Gradient descent step for P and Q
            for i in range(len(R)):
                for j in range(len(R[i])):
                    if R[i][j] > 0:
                        eij = R[i][j] - numpy.dot(P[i, :], Q[:, j])
                        for k in range(K):
                            P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                            Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
            # Error calculation for R and PQ
            e = 0
            for i in range(len(R)):
                for j in range(len(R[i])):
                    if R[i][j] > 0:
                        e = e + pow(R[i][j] - numpy.dot(P[i, :], Q[:, j]), 2)
                        for k in range(K):
                            e = e + (beta / 2) * (pow(P[i][k], 2) + pow(Q[k][j], 2))
            logger.info(f'INFO: Error for step {step + 1}/{steps} is {e}')
            print(f'INFO: Error for step {step + 1}/{steps} is {e}')
            if e < 0.001:
                logger.info(f'Exiting loop for error {e}')
                print(f'Exiting loop for error {e}')
                break

            nR = numpy.dot(P, Q)
            result = copy(df)
            result[where_are_NaNs] = nR[where_are_NaNs]
            count = 0
            original = df[~where_are_NaNs]
            predicted = nR[~where_are_NaNs]
            error_mae = 0.0
            error_rmse = 0.0

            for i in range(len(original)):
                error_mae += math.fabs(original[i] - predicted[i])
                error_rmse += math.pow((original[i] - predicted[i]), 2)
                count += 1

            error_mae /= count
            error_rmse = math.sqrt(error_rmse / count)

            logger.info(f'INFO: Error MAE for step {step + 1}/{steps} is {error_mae}')
            logger.info(f'INFO: Error R-MSE for step {step + 1}/{steps} is {error_rmse}')
            print(f'INFO: Error MAE for step {step + 1}/{steps} is {error_mae}')
            print(f'INFO: Error R-MSE for step {step + 1}/{steps} is {error_rmse}')

            b = datetime.datetime.now()
            print("INFO: Time Taken:" + str(b - a))
            logger.info('INFO: Time Taken '+ str(b-a))

            nP = copy(P)
            nQ = copy(Q.T)

            if step % 10 == 0:
                print(f'INFO: Saving matrix for step {step}')
                logger.info(f'INFO: Saving matrix for step {step}')
                numpy.savetxt("predicted_nmf_text_numpy.txt", result)
    except:
        pass
    return nP, nQ


N = len(df)
M = len(df[0])
logging.info(f'Size of V matrix {N}X{M}')

P = numpy.random.rand(N, K)
Q = numpy.random.rand(M, K)
logger.info('INFO: Formed matrix P and Q')

nP, nQ = matrix_factorization(df, P, Q, K)
print('INFO: Saving and calculating final matrix')
logger.info('INFO: Saving and calculating final matrix')

nR = numpy.dot(nP, nQ.T)
result = copy(df)
print('INFO: Final Matrix copy created')
logger.info('INFO: Final Matrix copy created')

result[where_are_NaNs] = nR[where_are_NaNs]
count = 0
original = df[~where_are_NaNs]
predicted = nR[~where_are_NaNs]
error_mae = 0.0
error_rmse = 0.0

print('INFO: Calculating RMSE and MAE for final matrix')
logger.info('INFO: Calculating RMSE and MAE for final matrix')

for i in range(len(original)):
    error_mae += math.fabs(original[i] - predicted[i])
    error_rmse += math.pow((original[i] - predicted[i]), 2)
    count += 1

error_mae /= count
error_rmse = math.sqrt(error_rmse / count)

print(f'INFO: Fianl Error MAE {error_mae} and Error RMSE {error_rmse}')
logger.info(f'INFO: Fianl Error MAE {error_mae} and Error RMSE {error_rmse}')
logger.info('Saving final matrix')

numpy.savetxt("predicted_nmf_text_numpy.txt", result)
logger.info('Final Matrix saved')
