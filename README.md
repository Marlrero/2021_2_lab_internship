# 2021_2_lab_internship

## 개발환경 설정
1. 아나콘다 설치 후 가상환경 만들기: conda create --name lab_internship
2. 가상환경 리스트 보기: conda info --envs
   - 가상환경 삭제하기: conda remove --name lab_internship --all
3. 가상환경 접속: conda activate lab_internship
4. Python 3.8 설치: conda install python=3.8
5. 필요한 패키지 설치: 실습 도중 패키지 설치가 있으면 그때 그때 설치! (pip install ~~)
   - Jupyter notebook
   - Numpy
   - Pandas
   - Matplotlib
6. 다 설치하고 나서! 이 가상환경을 저장할 때: (lab_internship) conda env export > environment.yaml
   - YAML 파일을 이용하여 가상환경 재설치할 때: conda env create -f '파일명'

## VS Code에서 하는 Python Source File과 Jupyter Notebook 모두 쓰기
1. Visual Studio Code를 설치하고 실행하여 확장팩 설치 (python 검색, Anaconda 검색)
   - Python, Python for VSCode, Python Extension Pack, Anaconda Extension Pack
2. Ctrl + Shift + P를 눌러 Command Pallet 창이 뜨면 Python: select interpreter 선택하여 아까 만들었던 가상환경을 선택함
3. 새 터미널을 만들면(기본으로 powershell이 뜸) 오른쪽에서 + 버튼을 클릭하여 기본 프로필을 누르고 command prompt로 변경함
4. 다시 새 터미널을 만들면 command prompt가 기본으로 뜰 것임
5. 왼쪽에서 hello.py를 하나 만들고 다음과 같이 코드를 작성함
   ```
    # %%
    print('Hello World!')
   ```
6. 위에 Run Cell을 누르면 에러가 발생
7. 터미널에서 conda install -c anaconda pywin32 을 설치하고 VS Code를 재시작하고 다시 실행
   ```
    # %%
    print('hello world!')
    # %%
    import numpy as np
    import matplotlib.pyplot as plt
    # %%
    years = [2015, 2016, 2017, 2018, 2019]
    rank = [5, 3, 2, 3, 4]
    # %%
    plt.plot(
        years,  # x축 데이터
        rank,  # y축 데이터
        color='blue',  # 선 색깔
        marker='o',  # 꼭짓점 설정
        linestyle='solid'  # 선 스타일 설정
    )
    plt.show()
   ```

## VS Code에서 사용하면 좋은 Python Extension
- 참고 사이트: https://www.topbots.com/data-scientists-guide-to-efficient-coding-in-python/
- Bracket Pair Colorizer
- Path Intellisense
- Python Dockstring generator
- Python Indent
- Python Type Hint
- TODO tree
- Pylance
