# %%
# 리스트와 레인지
list(range(0, 10))
# %%
list(range(0, 10000, 100))
# %%
import numpy as np
x = np.array([[0.1, 0.8, 0.1],
              [0.3, 0.1, 0.6],
              [0.2, 0.5, 0.3], 
              [0.8, 0.1, 0.1]])
y = np.argmax(x, axis=0) # 열방향
y
# %%
y = np.argmax(x, axis=1) # 행방향
y
# %%
y = np.array([1, 2, 1, 0]) # 모델 예측
t = np.array([1, 2, 0, 0]) # 타겟(정답)
print(y == t)
print(np.sum(y == t))