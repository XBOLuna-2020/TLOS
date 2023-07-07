# 导入Excel 的方法有两种，可以用pandas 库也可以使用xlrd 的方法


# 以下是使用xlrd 库的代码
# import xlrd
# file = 'D:\Python\Project1\data\Application_With_Credit_Score_D.xlsx' # Excel文件路径
# OpenExcelFile = xlrd.open_workbook(filename=file) #打开excel文件
# SheetCreateApp = 'ApplicationInterview_BasicInfo'
# SheetData = OpenExcelFile.sheet_by_name(SheetCreateApp) #打开指定的sheet
# dataset = []
# for r in range(SheetData.nrows):#遍历行
#     col = []
#     for l in range(SheetData.ncols): #便利列
#         col.append(SheetData.cell(r,l).value) #将单元格中的值加到列表中（r,l）中相当于坐标系，cell（）为单元格，value为单元格的值
#     dataset.append(col)
# from pprint import pprint  # pprint的输出形式为一行输出一个结果，下一个结果换行输出。实质上pprint输出的结果更为完整
#
# pprint(dataset)

# # 读取excel中的数据，填写入页面中
# #下面是使用pandas 库导入数据的方法
#
# #定义字段的元素定位方法和值
# field_locators = {
#     'ApplicationInterview_BasicInfo':{
#         'Source':(By.ID,'source_field_id'),
#         'id':(By.ID,'id_field_id'),
#         'value':(By.ID,'value_field_id')
#     }
#
# }
# # Excel文件路径
# file = 'D:\Python\Project1\data\Application_With_Credit_Score_D.xlsx'
# #sheet列表
# sheet_names = ['ApplicationInterview_BasicInfo','ApplicationInterview_BorrowerIn','ApplicationInterview_AddressInf','ApplicationInterview_SpouseInfo','ApplicationInterview_Addresshis','ApplicationInterview_EmployerIn','ApplicationInterview_SpouseEmpl','ApplicationInterview_BankInfo','ApplicationInterview_ResidenceI','ApplicationInterview_CarInfo','ApplicationInterview_REInfo','ApplicationInterview_AssetInfo','ApplicationInterview_BankruptIn','ApplicationInterview_CreditorIn','Calculation']
# #打开excel中指定sheet
# ReadData = pd.read_excel(file,sheet_name='ApplicationInterview_BasicInfo')
#
# #遍历sheet名称列表
# for sheet_name in sheet_names:
#     #读取sheet的数据
#     df = pd.read_excel(file,sheet_name=sheet_name)
#     #遍历数据行
#     for index,row in df.iterrows():
#         #遍历字段及其对应的数据
#         for field,locator in field_locators.items():
#             #获取字段的元素定位方式和值
#             field_locator = locator[0]
#             field_value = locator[1]
#             #获取对应字段的数据
#             field_data = row[field]
#
#             #在页面上填充数据
#             field_element = driver.find_element(By.ID,field_value)
#             field_element.clear()
#             field_element.send_keys(str(field_data))
#             time.sleep() #等待一秒钟，以确保数据已经填充完毕
#
#         # 单击click button
#         click_button = driver.find_element(By.ID,'Clickbutton')
# driver.quit()

# 不使用excel 而是自己手动定位页面的元素再诸葛填入数据
#Appbasicinfo

driver.find_element(By.ID,'AmountRequested').send_keys(1000)
print('金额输入完成。')

source_select = driver.find_element(By.ID,'LoanSourceId')#定位到Source下拉框
source_obj = Select(source_select)#创建Source下拉框对象
source_obj.select_by_visible_text('CUSTOMERRECOMMENDED(5)')#通过可见文本进行选择Source
print('Source选择完成。')
time.sleep(1)#等待选择的操作完成

purpose_select=driver.find_element(By.ID,'LoanPurposeId')#定位到purpose下拉框
purpose_obj=Select(purpose_select)#创建purpose下拉框对象
purpose_obj.select_by_visible_text('CHRISTMAS(1)')#通过可见文本进行选择purpose
print('Purpose选择完成。')

#Borrower info
InputBox_BorrowerSSN=driver.find_element(By.ID,'Applicant_SSN')#定位到BorrowerSSN
InputBox_BorrowerSSN.send_keys()