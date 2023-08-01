import common_method
from common_method import driver
from selenium.webdriver.common.by import By

# 从文件中读取app_number的值
with open('app_number.txt','r') as file:
    app_number = file.read()

driver.get('http://mgrtest:tower1@uft-svr-080801/Tower080801/Home/CreditApplication')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Enter/Edit Identification Information').click()
driver.find_element(By.ID, 'ApplicationNumber').send_keys()