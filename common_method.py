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
driver.get('http://mgrtest:tower1@uft-svr-080801/Tower080801/')
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
    ssn_input = driver.find_element(By.ID,"SSN")
    ssn_input.clear()
    ssn_input.send_keys(new_ssn) #输入 SSN

    # 点击搜索按钮
    search_button = driver.find_element(By.XPATH,'//*[@id="body"]/section/form/fieldset/p/button[1]')
    search_button.click()
    # time.sleep(5)

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
    create_new_application()

def create_new_application():
    driver.find_element(By.ID,'Applicant_SSN').send_keys(new_ssn)
    '''Generate fake name'''
    fake = Faker()
    full_name = fake.name() #注意后面要加（）调用方法并返回姓名字符串数据,此处返回的是first + last name，否则就是返回方法本身
    first_name, last_name = full_name.split()  # 拆分姓名为名字和姓氏
    driver.find_element(By.ID, "Applicant_FirstName").send_keys(first_name)  # 填入名字
    driver.find_element(By.ID, "Applicant_LastName").send_keys(last_name)  # 填入形式

    #定位并输入多个字段的数据
    input_fields = {
    # '''basic_info'''
        "AmountRequested": '1000',
        "LoanSourceId": 'CUSTOMER RECOMMENDED (5)',
        "LoanPurposeId": 'CHRISTMAS (1)',

    # '''applicant_basic_info'''
        "Applicant_Birthdate": '1/1/1990',

    # '''Applicant_CurrentAddress'''
        "DateOfResidence":'1/1/2010',
        "Applicant_CurrentAddress_Address1":'2220 RIDGEVIEW ST',
        "Applicant_CurrentAddress_Zip":'76119-3117',
        # "Applicant_CurrentAddress_City":'FORT WORTH',
        # "stateId":'',
        # "countyName":'ANDERSON (1)'

        #
    }
    for filed,value in input_fields.items():
        driver.find_element(By.ID,filed).send_keys(value)






