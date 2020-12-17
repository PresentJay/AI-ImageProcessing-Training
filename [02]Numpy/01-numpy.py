import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x, type(x))  # <ndarray> type means "n-dimension array"

y = np.array([2.0, 4.0, 6.0])

# calculating ndarray (just calculating entities, not matrix calculating )
print(x+y)
print(x-y)
print(x*y)
print(x/y)

y = np.array([2.0, 4.0])
try:
    print(x+y)
except:
    print("it errupts error.") # because of array size is not cooperated
    
A = np.array([[1,2],[3,4]])
print(A, A.shape, A.dtype) # shape means size of each entity array

B = np.array([[3,0],[0,6]])
print(A+B)
print(A*B)

B = np.array([10, 20])
print( A*B )  # how do it works?

X = np.array([[51,55], [14,19], [0,4]])
print(X[0])
print(X[0][1])
print(X[2][0])

for _ in X:
    print(_)

for _ in X:
    for __ in _:
        print(__)
        
X = X.flatten()  # what is flatten?
print(X)  # it makes nd-array to 1d-array (vector)

print(X[np.array([0,2,4])])
print(X>15)
print(X[X>15])