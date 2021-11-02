from typing import Callable

def numerical_diff(f: Callable, x: float) -> float:
    """중심 차분 (미분의 오차를 줄이는 좋은 방법)

    Args:
        f (Callable): 함수
        x (float): 함수에 들어갈 인자

    Returns:
        float: 수치 미분 값
    """
    h = 1e-4  # 0.0001
    return (f(x + h) - f(x - h)) / 2*h

# Callable[[arg, ...], result]
def tangent_line(f: Callable, x: float) -> Callable[[float], float]:
    """접선 기울기 그리기

    Args:
        f (Callable): 함수
        x (float): 함수에 들어갈 인자

    Returns:
        Callable[float]: 람다 함수
    """
    d = numerical_diff(f, x)    # 접선의 기울기가 반영된 함수 값
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y   # 기울기*입력 + 차분값

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    
    def func1(x):
        return 0.01*x**2 + 0.1*x
    

    def main():
        x = np.arange(0.0, 20.0, 0.1)
        y = func1(x)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.plot(x, y)
        #plt.show()

        tf1 = tangent_line(func1, 5)  # x = 5일 때 접선의 기울기
        y2 = tf1(x)
        
        plt.plot(x, y2)
        #plt.show()
        
        tf2 = tangent_line(func1, 10) # x = 10일 때 접선의 기울기
        y3 = tf2(x)
        
        plt.plot(x, y3)
        plt.show()

    main()