import numpy as np

def ReLU(x):
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