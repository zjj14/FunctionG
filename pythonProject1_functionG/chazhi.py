import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

def interpolate_data(data, length):
    x = range(len(data))
    y = data
    interp_func = interp1d(x, y, kind='linear')
    x_interp = np.linspace(0, len(data)-1, length)
    y_interp = interp_func(x_interp)
    return y_interp

def write_to_excel(data, filename, sheetname, start_row, start_col):
    df = pd.DataFrame({'Data': data})
    writer = pd.ExcelWriter(filename, engine='openpyxl')
    try:
        df.to_excel(writer, sheet_name=sheetname, startrow=start_row, startcol=start_col, index=False, header=False)
        writer.save()
        print("Data has been written to Excel successfully!")
    except Exception as e:
        print(f"Error occurred while writing data to Excel: {str(e)}")
    finally:
        writer.close()

# 示例数据
input_data = [5.477,4.2]
interpolated_data_length = 6500
excel_filename = "C:\\Users\\张骏\\Desktop\\output.xlsx"
excel_sheetname = 'Sheet1'
start_row = 1
start_col = 1

# 进行插值
interpolated_data = interpolate_data(input_data, interpolated_data_length)

# 写入Excel表格
write_to_excel(interpolated_data, excel_filename, excel_sheetname, start_row, start_col)