import numpy as np

import sys
sys.path.append("..")
from activation.sigmoid import sigmoid

def init_network() -> dict:
    """[summary]
        3층 순전파 신경망
    Returns:
        dict: [network]
    """
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    
    return network

def forward(network: dict, x: np.array) -> np.array:
    """[summary]
        3층 순전파 신경망 학습
    Args:
        network (dict): [3층 순전파 신경망 초기 가중치와 편향]
        x (np.array): [입력 값]

    Returns:
        np.array: [regression 결과 값 반환(항등함수)]
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    A1 = np.dot(x, W1) + b1
    Z1 = sigmoid(A1)
    
    A2 = np.dot(Z1, W2) + b2
    Z2 = sigmoid(A2)
    
    A3 = np.dot(Z2, W3) + b3
    Y = A3  # regression (identity function)
    
    return Y

if __name__ == '__main__':
    def main():
        network = init_network()
        x = np.array([1.0, 0.5])
        y = forward(network, x)
        print(y)
        
    main()