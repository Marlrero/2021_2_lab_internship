def add(a, b):
    return a + b

def main():   # 이 파일을 import하면 main 함수도 정의됨
    print(add(3, 4))
    print(add(4, 5))

main()  # 이 파일을 import하면 main 함수도 실행됨


# 위에 파일을 import 한다는 의미는 add 함수를 가져다 쓰는 것이 목적
# 그러나, 의도치 않게 main 함수가 실행되는 결과 초래