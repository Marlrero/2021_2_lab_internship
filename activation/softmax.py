import numpy as np

def softmax_init(a):
    exp_a = np.exp(a)  # 분자
    sum_exp_a = np.sum(exp_a)  # 분모
    return exp_a / sum_exp_a

def softmax(a: np.array) -> np.array:
    """[소프트맥스 함수 (분류)]

    Args:
        a (np.array): [입력]

    Returns:
        np.array: [결과값]
    """
    c = np.max(a)  # 최댓값
    exp_a = np.exp(a - c) # 분자
    sum_exp_a = np.sum(exp_a) # 분모
    return exp_a / sum_exp_a

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    def main():
        # softmax 초기 버전의 Overflow 문제
        a = np.array([1010, 1000, 990])
        print(softmax_init(a))
        
        # 최댓값을 빼도 소프트맥스는 상관 없음!
        c = np.max(a) # 최댓값 1010
        print(a - c)
        print(np.exp(a - c) / np.sum(np.exp(a - c))) # softmax
        
        # 오버플로 막는 버전
        a = np.array([0.3, 2.9, 4.0])
        y = softmax(a)
        print(y)
        print(np.sum(y))
    
    main()