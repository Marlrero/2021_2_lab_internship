# %%
import sys, os

sys.path.append("..")
from dataset.mnist import load_mnist
# %%
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)
# parameter
#  - normalize: 입력 이미지 픽셀 값을 0.0 ~ 1.0 사이 정규화
#               False이면 0 ~ 255 사이 그대로 유지
#  - flatten  : 입력 이미지를 평탄하게 1차원 배열로 형성함
#               False이면 1*28*28의 3차원, True이면 784의 1차원
#  - one_hot_label: One-hot encoding
#                   Ex) 숫자 2 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
#                       숫자 7 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# return
#  - (훈련 이미지, 훈련 레이블), (시험 이미지, 시험 레이블)
# %%
# 참고: x(input), y or t(target)
print(x_train.shape, t_train.shape)
print(x_test.shape, t_test.shape)
#print(type(x_test))
# %%
from PIL import Image
import numpy as np

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img)) # unsigned int 8 -> 2^8 = 256
    pil_img.show()

img = x_train[0]
label = t_train[0]  # target
print(label)

print(img.shape)   # (784, ) -> 앞서 flatten=True로 하였음
img = img.reshape(28, 28) # 이미지로 보여줘야 하므로 원래 이미지 모양 변경
print(img.shape)   # (28, 28)

img_show(img)