import numpy as np

# np.arange()
a = np.array([[1,2,3],[-2,9,3],[-3,5,3]])
b = np.array([[0,6,3],[-2,7,9],[3,7,-3]])

# To multiply arrays use np.dot(a,b)
m = np.dot(a,b)
n = np.dot(b,a)
# print(a,b,sep="\n")
# print(m)
# print(n)

# np.sort will sort
# p = np.sort(a)
# print(p)
# Indexing is same as that of list...

# To join two arrays we use .concatenate()
c = np.concatenate((a,b),1)
print(c)

# np.reshape()
# np.array_split()
