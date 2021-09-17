import math
import os
import random
import re
import sys


#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    sum_x_w = 0
    sum_w = 0
    for x, w in zip(X, W):
        sum_x_w += x * w
        sum_w += w
    return sum_x_w / sum_w


def recursive_weightedMean(X, W, sum_x_w=0, sum_w=0, i=0):
    if len(X) == i:
        return sum_x_w / sum_w
    return recursive_weightedMean(X, W, sum_x_w=sum_x_w + (X[i] * W[i]), sum_w=sum_w + W[i], i=i + 1)


if __name__ == '__main__':
    vals = list(map(int, input().split()))

    weights = list(map(int, input().split()))
    print(round(recursive_weightedMean(vals, weights), 1))
