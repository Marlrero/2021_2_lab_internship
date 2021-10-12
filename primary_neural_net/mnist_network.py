import pickle
import numpy as np
from tqdm import tqdm  # pip install tqdm

import sys
sys.path.append("..")
from dataset.mnist import load_mnist

from activation.sigmoid import sigmoid
from activation.softmax import softmax

from typing import Tuple  # type hinting

def get_data() -> Tuple[np.ndarray, np.ndarray]:
    """[MNIST에서 검증집합만 가지고 오는 함수]

    Returns:
        Tuple[np.ndarray, np.ndarray]: [검증집합 입력, 검증집합 레이블]
    """
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=True, one_hot_label=False)
    
    return x_test, t_test  # 검증 집합만

def init_network() -> dict:
    """[이미 만들어져 있는 가중치와 편향에 대해
        Python Pickle 객체 파일로 가져오고
        이를 네트워크로 초기화하는 함수]

    Returns:
        dict: [네트워크 가중치, 편향 초기값이 들어있는 딕셔너리]
    """
    with open("../dataset/mnist_weight.pkl", "rb") as f:
        network = pickle.load(f)
    
    print(network)
    return network

def predict(network: dict, x: np.array) -> np.array:
    """[모델이 순전파로 추론함]

    Args:
        network (dict): [네트워크 가중치, 편향 초기값이 들어있는 딕셔너리]
        x (np.array): [입력벡터]

    Returns:
        np.array: [결과벡터]
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    A1 = np.dot(x, W1) + b1
    Z1 = sigmoid(A1)
    
    A2 = np.dot(Z1, W2) + b2
    Z2 = sigmoid(A2)
    
    A3 = np.dot(Z2, W3) + b3
    Y = softmax(A3)  # classification
    
    return Y
    
if __name__ == "__main__":
    def main():
        '''
        # 배치 처리 방식 이전
        x, t = get_data()
        network = init_network()
        
        accuracy_cnt = 0  # 맞은 개수
        for i in range(len(x)):  # test 집합에 대해
            y = predict(network, x[i]) # 분류를 진행
            p = np.argmax(y)  # 확률이 가장 높은 원소의 인덱스
            if p == t[i]:     # 그 인덱스가 정답하고 맞으면
                accuracy_cnt += 1
        
        print("Accuarcy:", str(float(accuracy_cnt) / len(x)))
        '''
        '''
        # 배치 처리 방식 사용
        x, _ = get_data()  # test data, test target
        network = init_network()
        W1, W2, W3 = network['W1'], network['W2'], network['W3']

        print(x.shape, x[0].shape, W1.shape, W2.shape, W3.shape)
        '''
        
        # 배치 처리 방식 사용
        x, t = get_data()
        network = init_network()
        
        batch_size = 1000 # 배치 사이즈
        accuracy_cnt = 0
        
        for i in tqdm(range(0, len(x), batch_size), mininterval=0.01):
            x_batch = x[i : i+batch_size]    # 입력에 대해 배치로 쪼갬
            y_batch = predict(network, x_batch)
            
            print(y_batch)
            p = np.argmax(y_batch, axis=1)
            # x0에 대한 softmax 확률 값(이 값이 몇 개?)
            # x1에 대한 softmax 확률 값
            # ...
            # x999에 대한 softmax 확률 값
            # >> axis=0이면 열방향, axis=1이면 행방향
            
            accuracy_cnt += np.sum(p == t[i : i+batch_size])
            # p는 여기서 가장 높은 확률의 인덱스 배열
            # t는 정답 배열
            # p와 t가 모두 배열이고, 이것이 한 원소에 같으면 True
            # True가 되면 np.sum()은 이를 1로 바꿔서 합산
        
        print("Accuarcy:", str(float(accuracy_cnt) / len(x)))
        
        # execution: python mnist_network.py > result.txt
        
        
    main()