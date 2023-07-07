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


# 实例化一个option对象
# access_to_TLOS():
options = Options()
# 在笔记本上的option有add_experimental_option 这个属性，但是台式机上没有
 # 127.0.0.1是本地测试的地址
options.add_experimental_option("debuggerAddress","127.0.0.1:9233")
global driver #使用全局变量driver
# 导入webdriver浏览器的驱动，Chrome 类的实例化
driver = webdriver.Chrome(options=options)

# 单击图标，回到首页
def back_to_main_menu():
    # Logo = driver.find_element(By.CLASS_NAME,'logo')
    Logo = driver.find_element(By.XPATH,'/html/body/header/div/div[1]/a')
    Logo.click()
    print('回到首页啦!')

# 在首页中找到 Credit Application -> Application Interview 的链接并单击
def access_application_interview():
    Link_CreditApplication = driver.find_element(By.XPATH,'//*[@id="body"]/section/div[1]/a[1]')
    # Link_CreditApplication = driver1.find_element(By.LINK_TEXT,'Credit Application')
    Link_CreditApplication.click()
    print('Link: Credit Application clicked')

    # 单击链接1.Application Interview
    Link_ApplicationInterview = driver.find_element(By.XPATH,'/html/body/div/section/a[1]')
    Link_ApplicationInterview.click()
    print('Link: Application Interview clicked.')

# 生成新的SSN，并保存成global变量
def generate_new_ssn():
    global new_ssn
    fake = Faker()
    new_ssn = fake.ssn()
    print('New SSN:' + new_ssn)


# 在搜索框中输入ssn,查看是否已存在
def search_new_ssn():
    ssn_input = driver.find_element(By.XPATH,'//*[@id="SSN"]')
    ssn_input.clear()
    ssn_input.send_keys(new_ssn) #输入 SSN

    # 点击搜索按钮
    search_button = driver.find_element(By.XPATH,'//*[@id="body"]/section/form/fieldset/p/button[1]')
    search_button.click()
    time.sleep(2)

    #等待表格的出现
    wait = WebDriverWait(driver,10)
    no_data_message = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="AppplicationTable"]/tbody/tr/td')))

    # 如果是新SSN，结果应该是空 判断搜索结果是"No data available in table"
    if no_data_message.text == "No data available in table":
        print(f"SSN {new_ssn} 可以使用")
    else:
        print('继续产生新的SSN 吧')

# 在搜索页单击create button
def click_create_btn():
    # 单击Create button
    Button_Create = driver.find_element(By.XPATH,'//*[@id="btnLink"]')
    Button_Create.click()
    print('Button: Create clicked.')
    time.sleep(2)  #处理下弹窗前，需要等待，让弹窗加载2s

    # 在弹出的窗口上单击 Agree button
    Button_Agree = driver.find_element(By.XPATH,'/html/body/div[1]/section/form/div/div/div/div[3]/button')
    Button_Agree.click()




