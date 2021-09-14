# 파이썬 스크립트 파일 실행 예제
import script1

print('file name: script2.py')
print('__name__: {0}'.format(__name__))

# 파이썬은 변수 __name__이 만들어지고 이에 __main__ 문자열이 담김

# script2.py에는 별도의 main 함수가 없으므로
# import 문에 의해 script1.py의 __name__의 문자열은 해당 소스코드 이름이 됨

# 실행이 시작되는 스크립트 파일의 __name__에는 문자열 __main__을 채워줌
# import 되는 스크립트 파일에서는 __name__에는 파일 이름을 문자열로 채워줌