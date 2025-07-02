import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

print("Dot:", np.dot(a, b))

print("Inner:", np.inner(a, b))


print("Outer:\n", np.outer(a, b))


mat = np.array([[2, 0],
                [0, 2]])

print("Matrix squared:\n", np.linalg.matrix_power(mat, 2))
