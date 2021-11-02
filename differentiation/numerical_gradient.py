from typing import Callable
import numpy as np

def _numerical_gradient_no_batch(f: Callable, x: np.array) -> np.array:
    """편미분 벡터를 구하는 함수 (배치가 없는 버전)

    Args:
        f (Callable): 미분하고자 하는 함수
        x (np.array): 함수의 인자

    Returns:
        np.array: 편미분 벡터
    """
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)  # x와 형상이 같고 원소가 모두 0인 배열 생성
    
    for idx in range(x.size):
        tmp_val = x[idx]
        
        # f(x + h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)
        
        # f(x - h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val  # 값 복원
        
    return grad

def numerical_gradient(f: Callable, X: np.array) -> np.array:
    """편미분 벡터를 구하는 함수 (배치 버전)

    Args:
        f (Callable): 미분하고자 하는 함수
        X (np.array): 함수의 인자

    Returns:
        np.array: 편미분 벡터
    """
    if X.ndim == 1: # 1차원이면 배치가 없는 버전으로 해도 됨
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):  # enumerate (0, 1) (1, 5) (2, 7) ...
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad
    
def numerical_gradient_iter(f: Callable, x: np.array) -> np.array:
    """편미분 벡터를 구하는 함수 (배치 버전 - 반복자 사용)

    Args:
        f (Callable): [description]
        x (np.array): [description]

    Returns:
        np.array: [description]
    """
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite']) # Iterator
    while not it.finished:   # Iterator가 끝날 때까지 반복
        idx = it.multi_index # index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 값 복원
        it.iternext()        # Iterator 다음으로!

    return grad

if __name__ == '__main__':
    def func(x):
        if x.ndim == 1:
            return np.sum(x**2)
        else:
            return np.sum(x**2, axis=1)
    
    from numerical_diff import tangent_line
    import matplotlib.pyplot as plt
    
    def main():
        print(_numerical_gradient_no_batch(func, np.array([3.0, 4.0])))
        print(_numerical_gradient_no_batch(func, np.array([0.0, 2.0])))
        print(_numerical_gradient_no_batch(func, np.array([3.0, 0.0])))
        
        #print(numerical_gradient_iter(func, np.array([3.0, 4.0])))
        #print(numerical_gradient_iter(func, np.array([0.0, 2.0])))
        #print(numerical_gradient_iter(func, np.array([3.0, 0.0])))
        
        x0 = np.arange(-2, 2.5, 0.25)
        x1 = np.arange(-2, 2.5, 0.25)
        X, Y = np.meshgrid(x0, x1)
        
        X = X.flatten()
        Y = Y.flatten()
        
        grad = numerical_gradient(func, np.array([X, Y]) )
        
        plt.figure()
        plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        plt.xlabel('x0')
        plt.ylabel('x1')
        plt.grid()
        plt.legend()
        plt.draw()
        plt.show()

    main()