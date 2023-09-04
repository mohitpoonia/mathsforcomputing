#Practical 2: Generate the matrix into each form and find its rank using Numpy

#Taking input from user
#NR: Number of Rows
#NC: Number of Columns
import numpy as np
NR = int(input("Enter No. of Rows: "))
NC = int(input("Enter No. of Columns: "))

print("Enter the entries in a single line separated by spaces: ")

#user input entries in single line separated by spaces
entries = list(map(int, input().split()))

#For printing the matrix
matrix = np.array(entries).reshape(NR,NC)
print("Matrix X is as follows: ", '\n', matrix)

#For printing the rank of a matrix
print("Inverse of Matrix X: ", '\n',np.linalg.matrix_rank(matrix))

