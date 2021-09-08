# %%
print('hello world!')
# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
years = [2015, 2016, 2017, 2018, 2019]
rank = [5, 3, 2, 3, 4]
# %%
plt.plot(
    years,  # x축 데이터
    rank,  # y축 데이터
    color='blue',  # 선 색깔
    marker='o',  # 꼭짓점 설정
    linestyle='solid'  # 선 스타일 설정
)
plt.show()