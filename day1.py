"""
import numpy as np
arr =np.array([1, 2, 3, 4, 5])
print("1D array: ", arr)
arr = np.array([[1,2,3], [4,5,6]])
print("2D array: ", arr)
a = np.array(42)
b = np.array([1, 2,3,4,5])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print((arr))
print(a.ndim)
print(b.ndim)
print(c.ndim) 
print(d.ndim)
"""

# matrix puzzle solve 

import numpy as np 
# puzzle: find the sum of elements along the diagonal and flip the matrix 

# Generate a random 4X4 matrix with values from 1 to 20 
matrix = np.random.randint(1, 21, (4,4))
print("Orginal Matrix:")
print(matrix)

# calculate the sum of the diagonal 
diagonal_sum = np.trace(matrix)
print(f"\nSum of diagonal elements: {diagonal_sum}")

# Flip the matrix vertically and horizontally 
flipped_matrix = np.flip(matrix)
print("\nFlipped Matrix:")
print(flipped_matrix)

#Bonus: Identify positions of elements grater than 15 
positions = np.argwhere(matrix > 15)
print("\nPositions of elements greater than 15:")
for pos in positions: 
    print(f"Row {pos[0]+1}, Cloumn {pos[1] + 1}")