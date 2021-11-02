# %%
from numerical_diff import numerical_diff
# %%
def func(x):
    return x[0]**2 + x[1]**2   # or np.sum(x**2)
# %%
def func_part1(x0):
    return x0*x0 + 4.0**2.0
numerical_diff(func_part1, 3.0)
# %%
def func_part2(x1):
    return 3.0**2.0 + x1*x1
numerical_diff(func_part2, 4.0)