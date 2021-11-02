import numpy as np

def mean_squared_error(y: np.ndarray, t:np.ndarray) -> np.ndarray:
    """
    평균 제곱 오차

    Args:
        y (np.ndarray): 신경망 출력 (신경망이 추정한 값)
        t (np.ndarray): 정답(타겟) 레이블

    Returns:
        np.ndarray: 평균 제곱 오차 결과 값
    """
    
    return 0.5 * np.sum((y - t)**2)

if __name__ == '__main__':
    def main():
        #    0  1  2  3  4  5  6  7  8  9
        t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # 정답은 2 (One-hot encoding)
        
        #      0     1    2    3     4    5    6    7    8    9    
        y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.0, 0.1, 0.0] # 정답 맞음
        print(mean_squared_error(np.array(y), np.array(t)))
        
        #      0     1    2    3     4    5    6    7    8    9    
        y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.1, 0.0] # 정답 틀림
        print(mean_squared_error(np.array(y), np.array(t)))

    main()