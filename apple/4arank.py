import numpy as np


mat = np.array([[1, 2],
                [3, 4]])


print("Rank:", np.linalg.matrix_rank(mat))


print("Determinant:", np.linalg.det(mat))


print("Trace:", np.trace(mat))
