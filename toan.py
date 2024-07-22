#cau 1
'''import numpy as np #import numpy and uses shorter keyword
_A = [ [1, 5, 3], [4, 6, 6], [3, 8, 9] ] #array-like object  
A = np.array(_A) #create a 2-dimension array (matrix) from _A 
print(A) #print matrix A

import numpy as np 
_B = [ [1, 5, 3, 4], [4, 5, 7, 8], [7, 8, 9, 3] ] 
B = np.array(_B) 
print(B) 

import numpy as np 
_C = [ [1, 5], [4, 5], [3, 2], [7, 8] ] 
C = np.array(_C) 
print(C) '''

# câu 2
## a. 
'''import numpy as np
matrix = np.array([[1, 5, 3],
                   [4, 6, 6],
                   [3, 8, 9]])

# Tính hạng của ma trận
rank = np.linalg.matrix_rank(matrix)

print(f"Hạng của ma trận là: {rank}")
# Tính định thức của ma trận
det = np.linalg.det(matrix)

print(f"Định thức của ma trận là: {det}")
# Tìm chuyển vị của ma trận
transpose_matrix = np.transpose(matrix)

print("Ma trận gốc:")
print(matrix)

print("Chuyển vị của ma trận:")
print(transpose_matrix)
# Tính ma trận nghịch đảo
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Ma trận nghịch đảo là:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Ma trận không khả nghịch (không có ma trận nghịch đảo).")'''

##B. 
'''import numpy as np
matrix = np.array([[1, 5, 3, 4],
                   [4, 5, 7, 8],
                   [7, 8, 9, 3]])

# Tính hạng của ma trận
rank = np.linalg.matrix_rank(matrix)

print(f"Hạng của ma trận là: {rank}")
# Tính định thức của ma trận
det = np.linalg.det(matrix)

print(f"Định thức của ma trận là: {det}")
# Tìm chuyển vị của ma trận
transpose_matrix = np.transpose(matrix)

print("Ma trận gốc:")
print(matrix)

print("Chuyển vị của ma trận:")
print(transpose_matrix)
# Tính ma trận nghịch đảo
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Ma trận nghịch đảo là:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Ma trận không khả nghịch (không có ma trận nghịch đảo).")'''

##c. 
'''import numpy as np
matrix = np.array([[1, 5],
                   [4, 5],
                   [3, 2],
                   [7, 8]])

# Tính hạng của ma trận
rank = np.linalg.matrix_rank(matrix)

print(f"Hạng của ma trận là: {rank}")
# Tính định thức của ma trận
det = np.linalg.det(matrix)

print(f"Định thức của ma trận là: {det}")
# Tìm chuyển vị của ma trận
transpose_matrix = np.transpose(matrix)

print("Ma trận gốc:")
print(matrix)

print("Chuyển vị của ma trận:")
print(transpose_matrix)
# Tính ma trận nghịch đảo
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Ma trận nghịch đảo là:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Ma trận không khả nghịch (không có ma trận nghịch đảo).")'''

#Câu 3 
## AxB
'''import numpy as np
# Tạo hai ma trận
A = np.array([[1, 5, 3],
              [4, 6, 6],
              [3, 8, 9]])

B = np.array([[1, 5, 3, 4],
              [4, 5, 7, 8],
              [7, 8, 9, 3]])

# Tính tích của hai ma trận
product = np.dot(A, B)

print("Ma trận tích là:")
print(product)
##BxA
import numpy as np
# Tạo hai ma trận
A = np.array([[1, 5, 3],
              [4, 6, 6],
              [3, 8, 9]])

B = np.array([[1, 5, 3, 4],
              [4, 5, 7, 8],
              [7, 8, 9, 3]])

# Tính tích của hai ma trận
product = np.dot(B, A)

print("Ma trận tích là:")
print(product)
##AxC
import numpy as np
# Tạo hai ma trận
A = np.array([[1, 5, 3],
              [4, 6, 6],
              [3, 8, 9]])

C = np.array([[1, 5],
                   [4, 5],
                   [3, 2],
                   [7, 8]])


# Tính tích của hai ma trận
product = np.dot(A, C)

print("Ma trận tích là:")
print(product)
##CxA
import numpy as np
# Tạo hai ma trận
A = np.array([[1, 5, 3],
              [4, 6, 6],
              [3, 8, 9]])

C = np.array([[1, 5],
                   [4, 5],
                   [3, 2],
                   [7, 8]])


# Tính tích của hai ma trận
product = np.dot(C, A)

print("Ma trận tích là:")
print(product)
##BxC
import numpy as np
# Tạo hai ma trận
B = np.array([[1, 5, 3, 4],
              [4, 5, 7, 8],
              [7, 8, 9, 3]])
C= np.array([[1, 5],
                   [4, 5],
                   [3, 2],
                   [7, 8]])
# Tính tích của hai ma trận
product = np.dot(B, C)
print("Ma trận tích là:")
print(product)
##CxB
import numpy as np
# Tạo hai ma trận
B = np.array([[1, 5, 3, 4],
              [4, 5, 7, 8],
              [7, 8, 9, 3]])
C= np.array([[1, 5],
                   [4, 5],
                   [3, 2],
                   [7, 8]])


# Tính tích của hai ma trận
product = np.dot(C, B)
print("Ma trận tích là:")
print(product)'''

##Câu 4
'''# importing NumPy module 
import numpy as np
 
# input matrix 
inputMatrix = np.matrix([[1, 5, 3], [4, 6, 6], [3, 8, 9]])
# printing the input matrix
print("Input Matrix:\n", inputMatrix)
 
# getting Eigenvalues of an input matrix 
eigenValues = np.linalg.eigvals(inputMatrix)
 
# printing Eigenvalues of an input matrix 
print("Eigenvalues of an input matrix:\n", eigenValues)'''

#Câu 5
'''import numpy as np
import numpy.linalg as la
A = np.array([[1, 2],
              [3, 4]])
b = np.array([[5],
              [6]])
Ainv= la.inv(A)
x = Ainv.dot(b)
print(x)

## cách 2
import numpy as np
A = np.array([[1, 2],
              [3, 4]])
b = np.array([[5],
              [6]])
x = np.linalg.solve(A,b)
print(x)'''

#câu 6
import numpy as np

# Hệ phương trình: Ax = B
A = np.array([[1, 2],
              [3, 4],
              [7, 8]])

B = np.array([[5], [6], [9]])

# Tính nghiệm x bằng phương pháp bình phương cực tiểu
x = np.linalg.lstsq(A, B, rcond=None)[0]
print(x)

