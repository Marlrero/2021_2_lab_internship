# %%
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2

    if tmp <= theta:
        return 0
    else:
        return 1

# %%
AND(0, 0), AND(0, 1), AND(1, 0), AND(1, 1)

# %%
import numpy as np

# %%
x = np.array([0, 1])      # input
w = np.array([0.5, 0.5])  # weight
b = -0.7

print(w*x)             # 0*0.5   1*0.5
print(np.sum(w*x))     #   0   +  0.5         = 0.5
print(np.sum(w*x) + b) #   0   +  0.5  - 0.7  = -0.2

# %%
def NAND(x1, x2):
    x = np.array([x1, x2])

    # AND의 가중치와 편향의 부호만 다름
    w = np.array([-0.5, -0.5])
    b = 0.7

    if np.sum(w*x) + b <= 0:
        return 0
    else:
        return 1

# %%
NAND(0, 0), NAND(0, 1), NAND(1, 0), NAND(1, 1)

# %%
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # AND의 편향만 다름
    b = -0.2  

    if np.sum(w*x) + b <= 0:
        return 0
    else:
        return 1

# %%
OR(0, 0), OR(0, 1), OR(1, 0), OR(1, 1)

# %%
if __name__ == '__main__':
    def main():
        print(AND(0, 0), AND(0, 1), AND(1, 0), AND(1, 1))
        print(NAND(0, 0), NAND(0, 1), NAND(1, 0), NAND(1, 1))
        print(OR(0, 0), OR(0, 1), OR(1, 0), OR(1, 1))

    main()