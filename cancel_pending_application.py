from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# 设置浏览器选项
options = webdriver.ChromeOptions()
# 如果需要在后台运行，取消下一行的注释
# options.add_argument('--headless')

# 启动浏览器
driver = webdriver.Chrome(options=options)
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


# 打开网站
driver.get('http://mgrtest:tower1@uft-svr-090904/Tower090904/')
# 窗口最大化
driver.maximize_window()

try:
    # 定位表格行中的"pending application"或"Incomplete Application"链接，并点击进入详情页
    while True:
        link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Click Here")))
        link_element.click()

        # 选择purpose
        driver.find_element(By.ID,'LoanPurposeId').send_keys('CHRISTMAS (1)')

        # 在cancel的下拉列表中，选择‘Y'
        select_dropdown = Select(driver.find_element(By.ID,'Cancelled'))
        select_dropdown.select_by_value('Y')

        # 单击update按钮
        driver.find_element(By.ID,'btnUpdate').click()
        # 选择地址的radio
        driver.find_element(By.ID,'verifiedAddressOverridden').click()
        # 单击update按钮
        driver.find_element(By.ID,'btnUpdate').click()
        # # 在详情页中更新字段，例如假设有一个字段名为"field_name"，将其值更新为"updated_value"
        # field_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "field_name")))
        # field_name_input.clear()
        # field_name_input.send_keys("updated_value")

        # 返回到首页，继续处理下一个申请
        logo = driver.find_element(By.XPATH, '//*[@id="affixed-header"]/div[1]/a/img')
        logo.click()

except Exception as e:
    print("自动化过程中出现错误:", e)

# # 关闭浏览器
# driver.quit()
