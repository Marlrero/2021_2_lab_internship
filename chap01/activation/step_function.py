# %%
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# %%
import numpy as np

x = np.array([-1.0, 1.0, 2.0])
y = x > 0   # 배열에 부등호 연산이 가능함
print(y)

# %%
y = y.astype(np.int)  # bool -> int
print(y)

# %%
# numpy 방식으로 step function 재구연
def step_function(x): # x는 numpy 배열이 올 수 있음
    y = x > 0
    return y.astype(np.int32)

# %%
# numpy 방식으로 step function 재구연 (한 줄로!)
def step_function(x): # x는 numpy 배열이 올 수 있음
    return np.array(x > 0, dtype=np.int32)

# %%
import matplotlib.pylab as plt
x = np.arange(-5.0, 5.0, 0.1) # -5.0 ~ 5.0까지 간격 0.1로
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위
plt.show()
# %%
if __name__ == '__main__':
    def main():
        pass

main()