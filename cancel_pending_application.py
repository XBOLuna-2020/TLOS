# # 导入浏览器驱动
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import WebDriverException
# import pandas as pd

driver = webdriver.Chrome()
message = 'Former Borrower info found, please choose appropriate source of Former Borrower.'

def cancel_pending_app(self):
    self.driver.get('http://mgrtest:tower1@uft-svr-010110/Tower010110/')
    # 判断页面是否有pending application的表格出现
    table = self.driver.find_element(By.CLASS_NAME, 'table')
    # 获取所有待处理申请的行
    rows = self.driver.find_elements(By.TAG_NAME, 'tr')
    # 跳过首行标题行
    for row in rows[1:]:
    # 获取每行的App Number和URL
        app_number = row.find_element(By.XPATH, 'td[2]').text
        url_element = row.find_element(By.XPATH, 'td[3]/a')
        url = url_element.get_attribute('href')
        # 单击链接，进入app页
        self.driver.get(url)
        # 进入app页后，下拉到页面底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Select 'Yes' from the Cancel 下拉列表
        cancel_dropdown = self.driver.find_element(By.ID, 'Cancelled')
        cancel_dropdown.send_keys('Yes')
        # 单击Update 按钮
        updated_button = self.driver.find_element(By.ID, 'btnUpdate')
        updated_button.click()
        print('App:' + app_number + '已处理')
        # 返回到首页
        self.driver.back_to_main_menu

def update_app_source_onlinelending(self):
    source = driver.find_element(By.ID, 'LoanSourceId')
    source.clear()
    source.send_keys('CUSTOMER RECOMMENDED (5)')

