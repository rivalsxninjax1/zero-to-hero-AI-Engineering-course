import numpy as np
mat = np.array([[5,10], [15,20]])
trans = mat.T
print(trans)
print(mat @ trans)