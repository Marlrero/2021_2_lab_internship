# %%
import numpy as np
import sys, os

sys.path.append("..")
from dataset.mnist import load_mnist
# %%
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=True)
# %%
print(x_train.shape, t_train.shape)
# %%
np.random.choice(60000, 10) # MNIST는 6만개 데이터. 여기서 배치 10개 뽑기!
# %%
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
print(batch_mask)
# %%
x_batch = x_train[batch_mask] # 이미지
t_batch = t_train[batch_mask] # 이미지에 대한 정답
print(x_batch)
print(t_batch)