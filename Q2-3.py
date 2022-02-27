import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# 速率——浓度图像
S = np.arange(0, 200, 0.1)#生成等差数组
V = (150*S)/(7.5+S)
plt.xlabel('[S]/uM')
plt.ylabel('V')
plt.title("V-[S]")
plt.plot(S, V)
plt.show()
