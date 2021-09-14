def add(a, b):
    return a + b

# if의 조건이 True인 경우에만 main 함수가 정의되고 실행됨
if __name__ == '__main__':
    def main():
        print(add(3, 4))
        print(add(4, 5))

    main()