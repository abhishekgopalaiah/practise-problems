#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    l = []
    for n in grades:
        if n < 38 or n % 5 < 3:
            l.append(n)
        else:
            rounded_n = n + (5 - (n % 5))
            l.append(rounded_n)
    return l


if __name__ == '__main__':

    grades = [33, 67, 88, 41, 78]

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))

