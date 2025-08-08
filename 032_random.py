import numpy as np

mat = np.random.randint(1, 11, size=(3, 3))

print("matrix:\n", mat)

vec = np.array([1, 2, 3])
print("vector: \n", vec)

# adding the vector to each row of the matrix (broadcasting)
result = mat + vec

print("broadcasted addition:\n", result)
