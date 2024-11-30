import numpy as np

# Ma trận vuông
A = np.array([[1,-1,2],[-1,1,2],
              [2,2,2]])

# Tìm giá trị riêng và vector riêng
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Giá trị riêng:", eigenvalues)
print("Vector riêng:")
print(eigenvectors)
