import os

folder_path = 'C:\\Users\\张骏\\Desktop\\Data\\xiaobo_test'  # 替换为文件夹的路径
files = os.listdir(folder_path)

# 将文件名按照数字大小进行排序
sorted_files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))

# 循环读取每个文件
for file_name in sorted_files:
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        file_path = os.path.join(folder_path, file_name)

        # 读取Excel文件的操作...
        # 在这里添加你的读取Excel文件的代码