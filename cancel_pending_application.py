# # 导入浏览器驱动
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import WebDriverException
# import pandas as pd
#
# #先等待一段时间，需要手动点击Chrome浏览器一下
# print('先单击一下浏览器，切换窗口！')
# time.sleep(2)
#
# # 实例化一个option对象
# options = Options()
# # 在笔记本上的option有add_experimental_option 这个属性，但是台式机上没有
# # 127.0.0.1是本地测试的地址
# options.add_experimental_option("debuggerAddress","127.0.0.1:9233")
# # 导入webdriver浏览器的驱动，Chrome 类的实例化
# driver = webdriver.Chrome(options=options)
#
# # 单击图标，返回到首页
# def BacktoMainMenu():
#     Logo = driver.find_element(By.CLASS_NAME,'logo')
#     Logo.click()
#     print('回到首页啦!')
#
# # 如果页面还有Pending Application 就继续循环
# def CancelPendingApplication():
#     if there is a