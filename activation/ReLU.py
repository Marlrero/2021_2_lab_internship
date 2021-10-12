import numpy as np

def ReLU(x: np.array) -> np.array:
    """[ReLU(Rectified Linear Unit)]

    Args:
        x (np.array): [입력값]

    Returns:
        np.array: [배열의 원소가 양수면 그대로, 0이거나 음수면 0이 출력]
    """
    return np.maximum(0, x)  # 두 입력 중 최댓값을 반환

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    def main():
        x = np.arange(-5.0, 5.0, 0.1)
        y = ReLU(x)

        plt.plot(x, y)
        plt.ylim(-1, 5.5)
        plt.show()

    main()