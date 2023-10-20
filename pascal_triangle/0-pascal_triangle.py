#!/usr/bin/python3
import math

'''Creating a function that returns a list of lists of integers representing the Pascal's triangle '''

def pascal_triangle(n):
    '''n will always be an integer '''
    my_list = int(n)
    list_length = len(my_list)
    number = math.factorial(my_list)/math.factorial(list_length)*math.factorial(my_list - list_length)
    return number

