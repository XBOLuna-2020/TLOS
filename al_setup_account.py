import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import common_method
from common_method import driver

app_number_link = ''


# 在AL branch首页中找到 Credit Application -> Application Interview 的链接并单击
def al_search_pn_app():
    driver.get('http://mgrtest:tower1@uft-svr-090904/Tower090904/')
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Credit Application').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Application Interview').click()
    # 注意： 如果此处想要输入数字，需要加引号，因为这里应该是字符串
    # driver.find_element(By.ID, 'SSN').send_keys(new_ssn)
    # 筛选PN 状态的app并单击搜索按钮
    driver.find_element(By.ID, 'ApplicationStatus').send_keys('PN')
    driver.find_element(By.CLASS_NAME, 'btn-warning').click()
    # 等待ssn 的搜索结果显示出来
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'odd'), 'Credit'))
    # 获取app_number
    global app_number_link
    app_number_link = driver.find_element(By.XPATH, '//*[@id="AppplicationTable"]/tbody/tr[1]/td[1]/a')
    print('AL pending APP:' + app_number_link.text)
    app_number_link.click()


def al_enter_identification_info():
    # 在Credit Application页面，则选择Enter_identification_info link
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Enter/Edit Identification Information').click()
    driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number_link.text)
    driver.find_element(By.ID, 'btnSearch').click()
    # 选择Photo Compare
    driver.find_element(By.ID, 'ApplicantIdentification_PhotosCompare').send_keys('Y')
    # 输入Applicant Employment History 信息
    driver.find_element(By.ID, 'ApplicantEmployment_VerifiedNetIncome').clear()
    driver.find_element(By.ID, 'ApplicantEmployment_VerifiedNetIncome').send_keys(1000)
    driver.find_element(By.ID, 'ApplicantEmployment_NetIncomeVerified').send_keys('Yes')
    # 输入References信息
    driver.find_element(By.ID, 'References_0__ReferenceFor').send_keys('Applicant')
    driver.find_element(By.ID, 'References_0__ReferenceRelationship').send_keys('Friends')
    driver.find_element(By.ID, 'References_0__FirstName').send_keys('Lucus')
    driver.find_element(By.ID, 'References_0__LastName').send_keys('Boke')
    driver.find_element(By.ID, 'References_0__HomePhone_PhoneNumber').send_keys('6662647218')
    # 单击create按钮
    driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div/p[2]/input[3]').click()
    time.sleep(2)


al_search_pn_app()
common_method.checkout_application()
al_enter_identification_info()
common_method.back_to_main_menu()
common_method.payment_schedule()




