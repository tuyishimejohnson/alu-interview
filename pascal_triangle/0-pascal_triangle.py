#!/usr/bin/python3
import math

'''Creating a function that returns a list of lists of integers representing the Pascal's triangle '''

def pascal_triangle(n):
    '''n will always be an integer '''
    for num in range(n):
        if n <= 0:
            print([])
        print(' '*(n-num), end='')
        print()
        print(' '.join(map(str, str(11 ** num))))

