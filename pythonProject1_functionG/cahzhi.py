import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import medfilt

# 从 Excel 文件中读取第一列数据
file_path = "C:\\Users\\张骏\\Desktop\\yuanshuju.xlsx" # 替换为你的 Excel 文件路径
df = pd.read_excel(file_path)
data = df.iloc[:, 0].values

# 去噪处理
filtered_data = medfilt(data)

# 插值函数
interp_func = interp1d(np.arange(len(filtered_data)), filtered_data, kind='linear')

# 生成插值后的数据点
new_x = np.linspace(0, len(filtered_data)-1, len(filtered_data)*3)
new_y = interp_func(new_x)

# 将插值后的数据保存到指定路径的 Excel 文件
output_path = 'output_file_path.xlsx'  # 替换为你的输出文件路径
output_data = pd.DataFrame({'X': new_x, 'Y': new_y})
output_data.to_excel(output_path, index=False)

# 绘制原始数据和插值后的数据
plt.plot(np.arange(len(data)), data, 'ro', label='Original Data')
plt.plot(new_x, new_y, 'g-', label='Interpolated Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()