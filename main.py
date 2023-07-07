# 导入浏览器驱动
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import pandas as pd
from selenium.webdriver.support.select import Select
from faker import Faker
import common_method

#先等待一段时间，需要手动点击Chrome浏览器一下
print('先单击一下浏览器，切换窗口！')
time.sleep(2)

# 回到首页
common_method.back_to_main_menu()

# 单击credit application -> create application
common_method.access_application_interview()

# 生成新的SSN，并保存成global变量
common_method.generate_new_ssn()

# 在搜索框中输入ssn,查看是否已存在
common_method.search_new_ssn()

