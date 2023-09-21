import os
import pandas as pd
import matplotlib.pyplot as plt
# 获取文件夹中所有文件的文件名列表
folder_path = 'C:\\Users\\张骏\\Desktop\\Data\\xiaobo_test'  # 替换为文件夹的路径
files = os.listdir(folder_path)
writepath= 'C:\\Users\\张骏\\Desktop\\Data\\liqun_testimages\\'
print(files)
# 循环读取每个文件
for file_name in files:
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        file_path = os.path.join(folder_path, file_name)
        # 读取 Excel 文件并获取指定行的数据
        data = pd.read_excel(file_path)
        print(data)
        x_data = data.iloc[0]  # 第二行作为横坐标
        y_data = data.iloc[3]  # 第五行作为纵坐标
        # 绘制点线图
        plt.plot(x_data, y_data, 'r-')
        plt.xlabel('G')
        plt.ylabel('G*dP/dG')
        plt.title('G-G*dP/dG')
        # 根据文件名保存图像
        save_name = writepath + os.path.splitext(file_name)[0] + '.jpg'
        plt.savefig(save_name)
        plt.show()
        # 清空图表以便下一次循环使用
        plt.clf()
# 提示处理完成
print('图像保存完成！')