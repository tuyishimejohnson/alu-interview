#!/usr/bin/python3

''' Function that creates Pascal Triangle '''

def generate_pascal_triangle(n):
    '''returning empty list if n is less than or equal to 0'''

    if n <= 0:
        return []

    pascal_triangle = [[1]]
    for i in range(1,n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
        row.append(1)
        pascal_triangle.apped(row)

    return pascal_triangle
