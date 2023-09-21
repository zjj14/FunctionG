import pandas as pd


def extract(file_path):
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)

        # 将数据存储在二维列表中
        data = df.values.tolist()

        # 返回数据
        return data
    except Exception as e:
        print("读取Excel文件出错：", str(e))
        return None

