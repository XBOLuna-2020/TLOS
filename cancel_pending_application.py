# # 导入浏览器驱动
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import WebDriverException
# import pandas as pd

driver = webdriver.Chrome()
message = 'Former Borrower info found, please choose appropriate source of Former Borrower.'

# def check_pending_app():
#      # //*[@id="body"]/section/table/tbody/tr[2]/td[3]/a
#     if there is a table in the page:
#         driver.find_element(By.XPATH,'# //*[@id="body"]/section/table/tbody/tr[2]/td[3]/a').click()
#         cancel_application_interview()
# def cancel_application_interview():
#     if there is :
#         change the Source to former borrower
#         driver.find_element(By.ID,'countyName').send_keys('Adams (01)')
#         driver.find_element(By.ID,'verifiedUsed').click()
#     else
#     driver.find_element(By.ID,'btnUpdate').click()