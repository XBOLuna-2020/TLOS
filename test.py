from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options() #实例化option
options.add_experimental_option('detach',True)
driver= webdriver.Chrome(options=options)

driver.get('https://www.baidu.com')
sleep(2)

