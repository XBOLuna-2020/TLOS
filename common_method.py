from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.support.select import Select
from faker import Faker
from selenium.webdriver.chrome.options import Options


#调浏览器
options = Options() #实例化
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options) #实例化
driver.maximize_window() #窗口最大化

# 打开url 并且在用户名和密码放在里面
driver.get('http://mgrtest:tower1@uft-svr-010110/Tower010110/')
time.sleep(1)

# 单击图标，回到首页
def back_to_main_menu():
    # Logo = driver.find_element(By.CLASS_NAME,'logo')
    logo = driver.find_element(By.XPATH,'/html/body/header/div/div[1]/a')
    logo.click()
    print('回到首页啦!')

# 在首页中找到 Credit Application -> Application Interview 的链接并单击
def access_application_interview():
    link_credit_application = driver.find_element(By.XPATH,'//*[@id="body"]/section/div[1]/a[1]')
    # Link_CreditApplication = driver1.find_element(By.LINK_TEXT,'Credit Application')
    link_credit_application.click()
    print('Link: Credit Application clicked')

    # 单击链接1.Application Interview
    link_credit_application = driver.find_element(By.XPATH,'/html/body/div/section/a[1]')
    link_credit_application.click()
    print('Link: Application Interview clicked.')

# 生成新的SSN，并保存成global变量
def generate_new_ssn():
    global new_ssn
    fake = Faker()
    new_ssn = fake.ssn()
    print('New SSN:' + new_ssn)


# 在搜索框中输入ssn,查看是否已存在
def search_new_ssn():
    wait = WebDriverWait(driver,10)#等待ssn visible
    ssn_input = wait.until(EC.element_to_be_clickable((By.ID,'SSN')))
    # ssn_input = driver.find_element(By.ID,"SSN")
    ssn_input.click()
    # ssn_input.clear()
    ssn_input.send_keys(new_ssn) #输入 SSN

    # 点击搜索按钮
    search_button = driver.find_element(By.XPATH,'//*[@id="body"]/section/form/fieldset/p/button[1]')
    search_button.click()

    #等待表格的出现
    # wait = WebDriverWait(driver,10)
    table_prompt = EC.text_to_be_present_in_element((By.ID,'AppplicationTable'),'No data available in table')
    WebDriverWait(driver,10).until(table_prompt)
    # wait = driver.implicitly_wait(15)
    # no_data_message = wait.until(EC.visibility_of_element_located((By.ID,"AppplicationTable")))
    #
    # # 如果是新SSN，结果应该是空 判断搜索结果是"No data available in table"
    # if no_data_message.text == "No data available in table":
    #     print(f"SSN {new_ssn} 可以使用")
    # else:
    #     print('继续产生新的SSN 吧')


# 在搜索页单击create button
def click_create_btn():
    # 单击Create button
    button_create = driver.find_element(By.ID,"btnLink")
    button_create.click()
    print('开始创建application了！')
    time.sleep(2)  #处理下弹窗前，需要等待，让弹窗加载2s

    # 在弹出的窗口上单击 Agree button
    Button_Agree = driver.find_element(By.XPATH,'/html/body/div[1]/section/form/div/div/div/div[3]/button')
    Button_Agree.click()
    create_new_application() #新页面开始输入数据

# 进入新建application interivew的页面，开始输入数据
def create_new_application():
    driver.find_element(By.ID,'AmountRequested').send_keys('1000')
    applicant_ssn = driver.find_element(By.ID, 'Applicant_SSN')
    applicant_ssn.click()  # 单击一下applicant ssn 的输入框，否则老是无效输入
    applicant_ssn.send_keys(new_ssn)

    # input name
    fake = Faker()
    full_name = fake.name()  # 注意后面要加（）调用方法并返回姓名字符串数据,此处返回的是first + last name，否则就是返回方法本身
    print(full_name)
    first_name_box = driver.find_element(By.ID, "Applicant_FirstName")
    last_name_box = driver.find_element(By.ID, "Applicant_LastName")
    # 检查姓名是否包含头衔（例如 "PhD"、"Jr."等）
    if any(title in full_name for title in ["PhD", "Jr.", "Sr.", "II", "III", "IV", "V"]):
        # 使用空格分割姓名，并将最后一个部分作为姓氏
        name_parts = full_name.split()
        first_name = "".join(name_parts[:-1])  # 姓氏为除去最后一个部分的所有部分
        last_name = name_parts[-1]  # 最后一个部分为姓氏
        first_name_box.send_keys(first_name) #填入名字
        last_name_box.send_keys(last_name) # 填入姓氏
    else:
        # 如果没有头衔，正常分割姓名
        first_name, last_name = full_name.split(' ', 1)
        first_name_box.send_keys(first_name) #填入名字
        last_name_box.send_keys(last_name) # 填入姓氏

    # 定位并输入多个字段的数据
    input_fields = {
        # Basic loan information
        # "AmountRequested": '1000', #不知道为啥使用循环无法有效输入
        "LoanSourceId": 'CUSTOMER RECOMMENDED (5)',
        "LoanPurposeId": 'CHRISTMAS (1)',
        "Applicant_Birthdate": '8/8/1998',

        # Residence info
        "ResidenceStatusId": 'Rent',
        "DateOfResidence": '1/1/2010',
        "Applicant_CurrentAddress_Address1": '2220 RIDGEVIEW ST',
        "Applicant_CurrentAddress_Zip": '76119-3117',
        # Emp info
        "Applicant_EmploymentHistory_0__Employer": 'Marsk',
        "Applicant_EmploymentHistory_0__Industry": 'EDUCATION',
        # "Applicant_EmploymentHistory_0__Position":'TEACHER',
        "Applicant_EmploymentHistory_0__DateEmployed": '8/8/2008',
        "Applicant_EmploymentHistory_0__NetSalary": '10000',
        # Bank info
        "Applicant_BankName": 'Bank of US',
        "Applicant_CheckingAccount": 'Y',
        "Applicant_SavingAccount": 'Y',

        "DeclaredBankruptcy": 'N'

    }
    for field, value in input_fields.items():
        driver.find_element(By.ID, field).send_keys(value)
        print('输入了：' + field)

    # 输入电子邮件
    driver.find_element(By.ID,'Applicant_Emails_0__EmailAddress').send_keys('test@gmail.com')

    #输入countyName
    driver.find_element(By.ID,'countyName').send_keys('OUT OF STATE (1000)')

    #选择mail 的radio
    driver.find_element(By.ID,'mail').click()

    driver.find_element(By.ID,'btnCreate').click()
    driver.minimize_window()


# 进入新建application interivew的页面，开始输入数据
# def create_new_application():
#     driver.find_element(By.ID, 'Applicant_SSN').click()  # 单击一下ssn 的输入框，否则老是无效输入
#     driver.find_element(By.ID, 'Applicant_SSN').clear()
#     driver.find_element(By.ID,'Applicant_SSN').send_keys(new_ssn)  # enter ssn
#     driver.find_element(By.ID, 'AmountRequested').click()  # 单击一下ssn 的输入框，否则老是无效输入
#     driver.find_element(By.ID, 'AmountRequested').clear()
#     driver.find_element(By.ID, 'AmountRequested').send_keys('1000')
#
#     # input name
#     fake = Faker()
#     full_name = fake.name() #注意后面要加（）调用方法并返回姓名字符串数据,此处返回的是first + last name，否则就是返回方法本身
#     print(full_name)
#     first_name, last_name = full_name.split() #拆分姓名为名字和姓氏
#     driver.find_element(By.ID,"Applicant_FirstName").send_keys(first_name) #填入名字
#     driver.find_element(By.ID, "Applicant_LastName").send_keys(last_name) # 填入形式
#
#     #定位并输入多个字段的数据
#     input_fields = {
#         #Basic loan information
#         "AmountRequested": '1000',
#         "LoanSourceId": 'CUSTOMER RECOMMENDED (5)',
#         "LoanPurposeId": 'CHRISTMAS (1)',
#         "Applicant_Birthdate":'8/8/2008',
#
#
#         # Residence info
#         "ResidenceStatusId":'Rent',
#         "DateOfResidence": '1/1/2010',
#         "Applicant_CurrentAddress_Address1": '2220 RIDGEVIEW ST',
#         "Applicant_CurrentAddress_Zip": '76119-3117',
#         #Emp info
#         "Applicant_EmploymentHistory_0__Employer":'Marsk',
#         "Applicant_EmploymentHistory_0__Industry":'EDUCATION',
#         # "Applicant_EmploymentHistory_0__Position":'TEACHER',
#         "Applicant_EmploymentHistory_0__DateEmployed":'8/8/2008',
#         "Applicant_EmploymentHistory_0__NetSalary":'10000',
#         #Bank info
#         "Applicant_BankName":'Bank of US',
#         "Applicant_CheckingAccount":'Y',
#         "Applicant_SavingAccount":'Y',
#
#         "DeclaredBankruptcy":'N'
#
#
#     }
#     for field,value in input_fields.items():
#         driver.find_element(By.ID,field).send_keys(value)
#         print('输入了：'+field)







