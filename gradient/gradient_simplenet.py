import numpy as np

import sys
sys.path.append("..")
from activation.softmax import softmax
from loss.cee import cross_entropy_error_batch
from differentiation.numerical_gradient import numerical_gradient_iter

class SimpleNet:
    def __init__(self) -> None:
        # 정규분포(평균 0, 표준편차 1)로 초기화 (numpy 배열)
        self.W = np.random.randn(2, 3)
        
    def predict(self, x: np.array) -> np.array:
        """신경망 순전파 함수

        Args:
            x (np.array): 입력 벡터

        Returns:
            np.array: Dot product한 가중치와 곱한 벡터
        """
        return np.dot(x, self.W) # 곱이 아니라 dot product임에 주의!
    
    def loss(self, x: np.array, t: np.array) -> np.ndarray:
        """신경망의 손실 값 확인 (학습 시작)

        Args:
            x (np.array): 입력 벡터
            t (np.array): 타겟 벡터(정답)

        Returns:
            np.ndarray: 교차 엔트로피 오차 결과 값
        """
        z = self.predict(x)
        y = softmax(z)     # 활성화 함수 소프트맥스 사용
        loss = cross_entropy_error_batch(y, t)
        
        return loss
    
if __name__ == '__main__':
    def main():
        net = SimpleNet()
        print(net.W)  # 가중치 파라미터
        
        x = np.array([0.6, 0.9])  # 입력 벡터
        t = np.array([0, 0, 1])   # 타겟 벡터(정답)
        p = net.predict(x)
        print("predict: ", p)  # 가중치 벡터와 입력 벡터의 점곱
        print("result: ", np.argmax(p))  # 신경망이 예측한 결과에서 최댓값 인덱스

        print("loss: ", net.loss(x, t)) # softmax 값과 타겟의 교차 엔트로피 값
        
        # W는 dummy로 만든 것임
        # numerical_gradient(f, x) 내부에서 f(x)를 실행하는데,
        # 일관성을 위해 f(W)를 정의함 (람다 형식)
        
        f = lambda w: net.loss(x, t)
        # or
        #def f(W):
        #    return net.loss(x, t)
        
        dW = numerical_gradient_iter(f, net.W)

        print("weight gradient: \n", dW)  # 가중치 파라미터의 편미분 값
    
    main()
        
