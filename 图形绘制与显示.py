# 小黎专属python固定模板
# 开发时间：2024/9/19 15:29
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1)  # 以0.1为单位，生成从0到6的数组
y = np.sin(x)  # 计算sin函数

# 绘制图形
plt.plot(x, y)
plt.show()

