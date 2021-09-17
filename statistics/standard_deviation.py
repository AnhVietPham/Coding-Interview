#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def _numpy_stdDev(arr):
    return np.std(arr)


def _homemade_std(arr):
    total = sum(arr)
    mean = total / len(arr)
    total_deviation = 0

    for x in arr:
        total_deviation += (x - mean) ** 2

    return math.sqrt(total_deviation / len(arr))


if __name__ == '__main__':
    vals = list(map(int, input().split()))

    print(round(_homemade_std(arr=vals), 1))
