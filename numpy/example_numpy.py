"""
np.array(), np.arange(), np.zeros(), np.ones(), np.eye()

Reshape arrays: .reshape(), .ravel(), .flatten()
"""
import numpy as np

myarr = np.array([1,2,3,4,5,6,8,'',3,0])
print(myarr)

arr = np.arange(len(myarr))
print(arr)

# myarr = np.zeros([2,3])
# print(myarr)

# myarr = np.ones([2,3])
# print(myarr)

# myarr = np.eye(3,3)
# print(myarr)

reshape = arr[:9].reshape(3,3)
print(reshape)

reshape = myarr.reshape(5,2)
print(reshape)

print(reshape.ravel())

print(reshape.flatten())
