import openpyxl
def build_excel(i):
    path=f'C:\\Users\\张骏\\Desktop\\Data\\result\\{i+1}.xlsx'
    # 创建一个新的 Excel 工作簿
    workbook = openpyxl.Workbook()
    # 选择默认的工作表
    sheet = workbook.active
    workbook.save(path)
    return sheet