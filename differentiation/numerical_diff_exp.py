# %%
import numpy as np

np.float32(1e-50) # 0에 가까운 아주 작은 값 (소수점 아래 49개)
# 반올림 오차 문제 발생으로 인해 최종 계산 결과 오차가 발생 가능함
# 가급적 h의 경우 1e-4(10^-4)이 좋다고 알려져 있음
# %%
from typing import Callable
def numerical_diff(f: Callable, x: float) -> float:
    """수치 미분 (나쁜 구현 예)

    Args:
        f (Callable): 함수
        x (float): 함수에 들어갈 인자

    Returns:
        float: 수치 미분 값
    """
    h = 10e-50  # 0에 가까운 아주 작은 값
    return (f(x + h) - f(x)) / h