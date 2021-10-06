import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x)) # np.exp(-x)가 numpy array를 반환 -> broadcast

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from step import step_function
    
    def main():
        # broadcast 예제
        t = np.array([1.0, 2.0, 3.0])
        print(1.0 + t)
        print(1.0 / t)
        
        # sigmoid 함수 정의 후 사용
        x = np.array([-1.0, 1.0, 2.0])
        sigmoid(x)
        
        # sigmoid 함수 그래프 그리기
        x = np.arange(-5.0, 5.0, 0.1) # x축 범위 (-5.0 ~ 5.0까지 0.1씩)
        y = sigmoid(x)
        plt.plot(x, y)
        plt.ylim(-0.1, 1.1) # y축 범위
        plt.show()
        
        # step과 sigmoid 비교
        x = np.arange(-5.0, 5.0, 0.1)
        y1 = step_function(x)
        y2 = sigmoid(x)

        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.ylim(-0.1, 1.1)
        plt.show()
    
    main()