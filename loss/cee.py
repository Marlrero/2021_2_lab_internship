import numpy as np

def cross_entropy_error(y: np.ndarray, t:np.ndarray) -> np.ndarray:
    """
    교차 엔트로피 오차 구현
    Args:
        y (np.ndarray): 신경망 출력 (신경망이 추정한 값)
        t (np.ndarray): 정답(타겟) 레이블

    Returns:
        np.ndarray: 교차 엔트로피 오차 결과 값
    """
    delta = 1e-7  # 아주 작은 값 delta를 더해야 np.log(0) = -inf가 방지됨
    return -np.sum(t * np.log(y + delta))

def cross_entropy_error_batch(y: np.ndarray, t:np.ndarray) -> np.ndarray:
    """
    교차 엔트로피 오차 구현 (배치버전)
    Args:
        y (np.ndarray): 신경망 출력 (신경망이 추정한 값)
        t (np.ndarray): 정답(타겟) 레이블

    Returns:
        np.ndarray: 교차 엔트로피 오차 결과 값
    """
    if y.ndim == 1: # y가 1차원이라면
        t = t.reshape(1, t.size) # t를 1*size만큼 형상 변환
        y = t.reshape(1, y.size) # y를 1*size만큼 형상 변환
        
    # 훈련 데이터가 원-핫 벡터라면 정답 레이블의 인덱스로 반환
    if t.size == y.size:
        t = t.argmax(axis=1)
        
    batch_size = y.shape[0]
    # return -np.sum(t * np.log(y + 1e-7)) / batch_size
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    def main():
        # 자연 로그 그래프
        x = np.arange(-5.0, 1.0, 0.001)
        plt.plot(x, np.log(x))
        plt.xlim(0.0, 1.0)
        plt.ylim(-5.0, 0.0)
        plt.show()
        
        # 정답일 때 정답이 아닐 때 오차 비교
        #    0  1  2  3  4  5  6  7  8  9
        t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # 정답은 2 (One-hot encoding)
        
        #      0     1    2    3     4    5    6    7    8    9    
        y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.0, 0.1, 0.0] # 정답 맞음
        print(cross_entropy_error(np.array(y), np.array(t)))
        
        #      0     1    2    3     4    5    6    7    8    9    
        y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.1, 0.0] # 정답 틀림
        print(cross_entropy_error(np.array(y), np.array(t)))

    
    main()