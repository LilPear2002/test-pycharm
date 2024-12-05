# 小黎专属python固定模板
# 开发时间：2024/9/19 15:33

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
# 通过np.arange生成从0到6，步长为0.1的数组x
x = np.arange(0, 6, 0.1)
# 计算x对应的正弦值
y1 = np.sin(x)
# 计算x对应的余弦值
y2 = np.cos(x)

# 绘制图形
# 绘制x与y1的关系曲线，表示正弦曲线
plt.plot(x, y1, label="sin")
# 绘制x与y2的关系曲线，使用点划线表示余弦曲线
plt.plot(x, y2, linestyle="--", label="cos")
# 设置x轴标签为'x'
plt.xlabel("x")
# 设置y轴标签为'y'
plt.ylabel("y")
# 设置图形标题为'sin & cos'
plt.title("sin & cos")
# 图例显示，用于区分不同曲线
plt.legend()
# 显示图形
plt.show()