# #image processing 
import numpy as np
# image = np.array([[100, 150, 200],
#                   [80, 120, 180],
#                   [60, 100, 160]])

# filter = np.array([[1,0,-1],
#                    [1, 0, -1],
#                    [1, 0, -1]])

# #convolution = element - wise multipilcation + sum
# edge_value = np.sum(image *filter)

# #word embeddings 
# # Word embeddings (just an example)
# king = np.array([0.5, 0.8, 0.3])
# man  = np.array([0.2, 0.7, 0.1])
# woman = np.array([0.3, 0.6, 0.4])

# # king - man + woman ≈ queen
# guess = king - man + woman

# # ai model evaluation
y_true = np.array([1, 0, 1, 1])
y_pred = np.array([1, 0, 0, 1])

accuracy = np.mean(y_true == y_pred)
print(f"accuracy : {accuracy * 100:.2f}%")


signal = np.array([0.5, 0.7, -0.2, -0.5])
amplified = signal * 2  # Increase volume


user_pref = np.array([4, 0,3])
item_features = np.array([[1, 0.2, 0.5],  # Item 1
                          [0.5, 0.1, 0.3],
                          [0.2, 0.9, 0.7]])


predicted_ratings = item_features @ user_pref

