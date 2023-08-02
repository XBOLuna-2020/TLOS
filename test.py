from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import xlrd

# options = Options() # 实例化option
# options.add_experimental_option('detach',True) # 打开浏览器后不关闭
# driver = webdriver.Chrome(options=options)

# 打开Excel文件
workbook = xlrd.open_workbook('data/Application_With_Credit_Score_D.xlsx')

# 获取所有工作表
sheets = workbook.sheets()

# 遍历所有的sheets
for sheet in sheets:
    # 获取行数和列数
    num_rows = sheet.nrows
    num_cols = sheet.ncols

    # 遍历每一行
    for i in range(num_rows):
        # 遍历每一列
        for j in range(num_cols):
            cell_value = sheet.cell_value(i, j)
            print(cell_value)
    # 打印工作表的名字
    print(f"工作表名字：{sheet.name}")
    print()

# # 通过索引获取工作表
# worksheet = workbook.sheet_by_index(0)




sleep(2)

