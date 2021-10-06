# %%
import numpy as np
# %%
A = np.array([1, 2, 3, 4]) # 1D
print(A)
print(np.ndim(A))  # 배열의 차원 수
print(A.shape)     # 배열의 형상 (튜플을 반환)
print(A.shape[0])
# %%
B = np.array([[1, 2], [3, 4], [5, 6]]) # 2D
print(B)
print(np.ndim(B))  # row와 column
print(B.shape)
# %%
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A.shape)
print(B.shape)

np.dot(A, B)  # *으로 연산하지 않음!
# %%
A = np.array([[1, 2, 3], [4, 5, 6]])
C = np.array([[1, 2], [3, 4]])

print(A.shape, C.shape)
np.dot(A, C)
# %%
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])
print(A.shape, B.shape)
C = np.dot(A, B)
print("result:", C, C.shape)
# %%
X = np.array([1, 2])
print("Input:", X, X.shape)

W = np.array([[1, 3, 5], [2, 4, 6]])
print("Weight:\n", W, W.shape)

Y = np.dot(X, W)
print("Output:", Y, Y.shape)