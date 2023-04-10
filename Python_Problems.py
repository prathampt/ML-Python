'''
Q1. Write a program to take a list as input which will contain dublicate values...
And display the number and its occurance...
'''

# list = map(int,input("Enter the values in list separated by spaces: ").split())
# dict = {}

# for i in list:
#     for j in dict.keys():
#         if i == j:
#             dict[i] += 1 
#             break   
#     else:
#         dict[i] = 1

# print(dict)

'''
Q2. Convert a matrix into an array and print elements in reverse...
'''
# import numpy as np
# r,c = map(int,input().split())

# arr = np.array([])
# for i in range(r):
#     t = np.array(list(map(int, input().split())))
#     arr = np.concatenate((arr,t),0)

# def reverse_array(a):
#     for i in range(len(a)//2):
#         a[i],a[len(a)-i-1] = a[len(a)-i-1],a[i]
# print("Original list:")
# print(arr)
# arr2 = np.reshape(arr,(r,c))
# print("Matrix is: ")
# print(arr2)
# reverse_array(arr)
# print("Reversed array is: ")
# print(arr)

'''
Q3. Given 2 np.arrays, create a one-many relation to print all sorts of possible sentences...
'''
# import numpy as np
# name_array = np.array(["Arun","Vishwas"])
# verb_array = np.array([["likes to cook","likes to eat"],
#                         ["codes in python3","codes in c++"]])
# ans = np.array([])
# for i in range(len(name_array)):
#     for j in range(len(verb_array[0])):
#         ans = np.concatenate((ans,np.array([f"{name_array[j]} {verb_array[i][j]}"])))

# print(ans)



"""Q4. Exercise: Write a Python function that takes a list of tuples as input, where each tuple contains a name (string) and an age (integer),
 and returns a dictionary where the keys are the names and the values are the ages.

For example, given the input [( "Alice", 25 ), ( "Bob", 30 ), ( "Charlie", 35 )], the function should return
 {"Alice": 25, "Bob": 30, "Charlie": 35}.
"""

# data = [( "Alice", 25 ), ( "Bob", 30 ), ( "Charlie",35)]
# def create_age_dictionary(data):
#     new_dict = {}
#     for name,age in data:
#         new_dict[name] = age
#     return new_dict

# print(create_age_dictionary(data))

"""
Q5. Given any 2D matrix, find row echelon form, display rank and nullity of the given matrix...
"""
import numpy as np
import numpy.linalg as la

def row_echelon(matrix):
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 0:
                #Zero division rule
                if matrix[i][j] != 0:
                    matrix[i] /= matrix[i][j] 

    if matrix[0][0] != 0 or matrix[1][0] != 0 or matrix[2][0] != 0: # We will swap only if atleast one entry in column is not zero.
        while not matrix[0][0]: # Swapping until we get 1 in 1,1 postion
            matrix[[0,2,1]] = matrix[[2,1,0]] 
        for i in range(1,3): # reducing other rows to zero
            if matrix[i][0] == 1:
                matrix[i] -= matrix[0]
    else:
        count += 1
    
    for i in range(1-count,3): # If value of count increments then leading one is shifted above
        if matrix[i][1] != 0 and matrix[i][1] != 1:
            matrix[i] /= matrix[i][1]

    if matrix[0][1] != 0 or matrix[1][1] != 0 or matrix[2][1] != 0:
        if count == 1:
            if matrix[1][1] == 0:
                matrix[[0,2]] = matrix[[2,0]]
            else:
                matrix[2] -= matrix[1]
                matrix[[0,1]] = matrix[[1,0]]
        else:
            if matrix[1][1] == 0:
                matrix[[1,2]] = matrix[[2,1]]
            else:
                matrix[2] -= matrix[1]
    else:
        count += 1

    if round(matrix[2][2]) != 0 and round(matrix[2][2]) != 1:
            matrix[2] /= matrix[2][2]

    if count == 1:
        matrix[1] -= matrix[1][2]*matrix[2]
        matrix[[1,2]] = matrix[[2,1]]
    elif count == 2:
        matrix[1] -= matrix[1][2]*matrix[2]
        matrix[0] -= matrix[0][2]*matrix[2]
        matrix[[0,2]] = matrix[[2,0]]

    matrix = np.round_(matrix,2)
    return matrix

given_matrix = np.arange(0,9,dtype='float').reshape(3,3)

print("Given matrix is:\n",given_matrix)
print("Row-echelon form:\n",row_echelon(given_matrix))
print("Rank is: ",la.matrix_rank(given_matrix))
print("Nullity is: ",3 - la.matrix_rank(given_matrix))


given_matrix = np.array([1,3,5,3,5,3,2,4,2],dtype="float").reshape(3,3)

print("Given matrix is:\n",given_matrix)
print("Row-echelon form:\n",row_echelon(given_matrix))
print("Rank is: ",la.matrix_rank(given_matrix))
print("Nullity is: ",3 - la.matrix_rank(given_matrix))


given_matrix = np.array([0,0,5,0,0,7,0,0,8],dtype="float").reshape(3,3)

print("Given matrix is:\n",given_matrix)
print("Row-echelon form:\n",row_echelon(given_matrix))
print("Rank is: ",la.matrix_rank(given_matrix))
print("Nullity is: ",3 - la.matrix_rank(given_matrix))

A = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]],dtype="float")
print("Given matrix is:\n",A)
print("Row-echelon form:\n",row_echelon(A))
print("Rank is: ",la.matrix_rank(A))
print("Nullity is: ",3 - la.matrix_rank(A))

