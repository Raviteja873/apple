import numpy as np

mat = np.array([[2, 0],
                [0, 3]])

eigen = np.linalg.eigvals(mat)
print("Eigenvalues:", eigen)
