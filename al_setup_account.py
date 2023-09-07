from selenium.webdriver.support.wait import WebDriverWait
from common_method_original import driver, new_ssn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def al_state_create_new_application():
    # 如果有error 发生（090904），则返回到首页再去查看最新生成的app number
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Credit Application').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Application Interview').click()
    # 注意： 如果此处想要输入数字，需要加引号，因为这里应该是字符串
    driver.find_element(By.ID, 'SSN').send_keys(new_ssn)
    # 点击搜索按钮
    driver.find_element(By.CLASS_NAME, 'btn-warning').click()
    # search_button = driver.find_element(By.XPATH, '//*[@id="body"]/section/form/fieldset/p/button[1]')
    # search_button.click()
    # 等待ssn 的搜索结果显示出来
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'odd'), 'Credit'))

    # 获取app_number
    app_number = driver.find_element(By.XPATH, '//*[@id="AppplicationTable"]/tbody/tr[1]/td[1]/a').text
    print('AL: NEW APP:' + app_number)