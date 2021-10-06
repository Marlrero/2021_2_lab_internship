# %%
import numpy as np
# 상위경로 모듈 포함
import sys
sys.path.append("..")
from activation.sigmoid import sigmoid
# %%
# 입력층 -> 1층
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(X.shape, W1.shape, B1.shape)

A1 = np.dot(X, W1) + B1
print(A1, A1.shape)

Z1 = sigmoid(A1)
print(Z1)
# %%
# 1층 -> 2층
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape, W2.shape, B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(Z2)
# %%
def identity_function(x):
    return x
# %%
# 2층 -> 3층
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

print(Z2.shape, W3.shape, B3.shape)

A3 = np.dot(Z2, W3) + B3
Z3 = sigmoid(A3)

Y = identity_function(A3)  # or Y = A3
print(Y)