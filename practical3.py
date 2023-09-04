#Practical 3: Find the Cofactors, Determinant, Adjoint and Inverse of a Matrix
#NR: Number of Rows
#NC: Number of Columns
import numpy as np
NR = int(input("Enter No. of Rows: "))
NC = int(input("Enter No. of Columns: "))

print("Enter the entries in a single line separated by spaces: ")

#Usinf input entries
entries = list(map(int, input().split()))

#For printing the matrix
A = np.array(entries).reshape(NR,NC)
print("Matrix X is as follows: ", '\n', A)

A_Inverse = np.linalg.inv(A)
Transpose_of_A_Inverse = np.transpose(A_Inverse)
Determinant_of_A = np.linalg.det(A)
Cofactor_of_A = np.dot(Transpose_of_A_Inverse, Determinant_of_A)
Adjoint_of_A = np.transpose(Cofactor_of_A)
#for finding the cofactor of a Matrix
print("The Cofsctor of a Matrix is: ",'\n', Cofactor_of_A)

#for finding the Determinant of a Matrix
print("The Determinant of a Matrix is: ", '\n', Determinant_of_A)

#for finding the Adjoint of a Matrix
print("The Adjoint of a Matrix :", '\n', Adjoint_of_A)
