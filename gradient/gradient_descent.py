from typing import Callable
import numpy as np
import matplotlib.pylab as plt

import sys
sys.path.append("..")
from differentiation.numerical_gradient import numerical_gradient

def gradient_descent(f: Callable, init_x: np.array, lr :float = 0.01, 
                     step_num: int = 100) -> np.array:
    """경사 하강법

    Args:
        f (Callable): 최적화하려는 함수
        init_x (np.array): 초깃값
        lr (float, optional): 학습률. Defaults to 0.01.
        step_num (int, optional): 경사법에 따른 반복 횟수. Defaults to 100.

    Returns:
        np.array: 경사 하강법 결과 배열
    """
    x = init_x
    x_history = []  # 경사가 내려가는 것을 history로 저장

    for i in range(step_num): # step_num 만큼 반복
        x_history.append( x.copy() )  # 그냥 x로 하면 레퍼런스! 반드시 copy!

        grad = numerical_gradient(f, x) # 함수 기울기를 구함
        x -= lr * grad   # 경사 하강법(기울기에 학습률을 곱해서 뺌)

    return x, np.array(x_history)

def func(x):
    return np.sum(x**2) # or x[0]**2 + x[1]**2

if __name__ == '__main__':
    def main():
        init_x = np.array([-3.0, 4.0])    

        lr = 0.1
        step_num = 20
        x, x_history = gradient_descent(func, init_x, lr=lr, step_num=step_num)

        print(x, end='\n')
        print(x_history)

        plt.plot( [-5, 5], [0,0], '--b') # 가로 파랑 점선
        plt.plot( [0,0], [-5, 5], '--b') # 세로 파랑 점선
        plt.plot(x_history[:,0], x_history[:,1], 'o')

        plt.xlim(-3.5, 3.5)
        plt.ylim(-4.5, 4.5)
        plt.xlabel("X0")
        plt.ylabel("X1")
        plt.show()
        
    main()