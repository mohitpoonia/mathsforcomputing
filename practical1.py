#Practical 1: Create and transform vectors and matrices (the transpose vector(matrix)
#transpose of a vector(matrix)

#Program to Transpose a Matrix using Numpy

#taking input from use
#NR: No. of rows
#NC: No. of columns
import numpy as np
NR = int(input("Enter No. of Rows: "))
NC = int(input("Enter No. of Columns: "))

print("Enter the entries in a single line separated by spaces: ")

#user Input of entries in
#a single line separated by space
entries = list(map(int, input().split()))

#for printing the matrix
matrix = np.array(entries).reshape(NR,NC)
print("Matrix X is as follows: ", '\n', matrix)

print("Transpose of Matrix X is as follows: ", '\n',np.transpose(matrix))
