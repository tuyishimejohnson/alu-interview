#!/usr/bin/python3

'''Creating a function that returns a list of lists of integers representing the Pascal's triangle '''

def pascal_triangle(n):
    '''n will always be an integer '''
    n = int(n)
    my_list = []
    for i in range(n):
        if n <= 0:
            return []
        return my_list.append(i)    
