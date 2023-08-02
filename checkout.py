from selenium.webdriver.common.by import By
from common_method import driver
from selenium.webdriver import ActionChains


# app创建成功后，进入checkout页面
def checkout_application():
    # 单击下拉列表目录
    driver.find_element(By.ID,'dropdownMenu1').click()
    # 选择checkout
    driver.find_element(By.XPATH,'//*[@id="pageTitle"]/div/ul/li[3]/a').click()

    # 输入Applicant Gross Monthly Salary
    from selenium.webdriver.common.by import By
    applicant_salary_monthly_salary = driver.find_element(By.ID,'ApplicantSalaryGarnishments_VerifiedMonthlySalary')
    ActionChains(driver).double_click(applicant_salary_monthly_salary).perform()
    applicant_salary_monthly_salary.send_keys(15000)

    # Manager Approve info
    driver.find_element(By.ID,'LoanApprovals_0__Approved').send_keys('Y')
    # 输入 Credit Limit
    credit_limit = driver.find_element(By.ID, 'CreditLimit')
    credit_limit.clear()  # 因为有默认值，需要先清除默认值，否则会在后面追加
    credit_limit.send_keys(1000)
    # 规定Amount Approved
    amount_approved = driver.find_element(By.ID, 'LoanApprovals_0__ApprovedAmount')
    amount_approved.clear()
    amount_approved.send_keys(1000)

    # 输入Plan A 的数据
    plan_A_input_box = driver.find_element(By.ID, 'planA')
    ActionChains(driver).double_click(plan_A_input_box).perform()  # Plan A 需要双击后才可以输入数字清除默认数值
    plan_A_input_box.send_keys('1000')
    plan_a = 'RN CUST, WANTS$1000, SELF EMPLOYED 3 YRS, BUYING HER HOME 2 YR RES, HAS C/S C 28% DTI, IM OK TO ADV $1000' \
             ' WILL BE A $4000 NL, DHPZ, 26 X 258 WILL NEED ID/POI/PP TO CLOSE VOIDED CHK AND 0 FORMER CL BC. '
    driver.find_element(By.ID, 'commentText1').send_keys(plan_a)

    # 输入security info
    driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys('Endorser')
    driver.find_element(By.ID, 'ApplicantSignature').send_keys('Y')
    driver.find_element(By.XPATH, '//*[@id="body"]/section/form[2]/p/input[3]').click()

    print('checkout 成功')
    driver.minimize_window()