import random
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from faker import Faker
from selenium.webdriver.chrome.options import Options

# 调浏览器
options = Options()  # 实例化
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)  # 实例化
driver.maximize_window()  # 窗口最大化
# 在module外定义global元素
app_number = ''
new_ssn = ''


# 单击图标，回到首页
def back_to_main_menu():
    # Logo = driver.find_element(By.CLASS_NAME,'logo')
    logo = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/a')
    logo.click()
    print('回到首页啦!')


# 在首页中找到 Credit Application -> Application Interview 的链接并单击
def access_application_interview():
    # 打开url 并且在用户名和密码放在里面
    driver.get('http://mgrtest:tower1@uft-svr-090904/Tower090904/')
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Credit Application').click()

    # 单击链接Application Interview
    link_credit_application = driver.find_element(By.XPATH, '/html/body/div/section/a[1]')
    link_credit_application.click()


# 生成新的SSN，并保存成global变量
def generate_new_ssn():
    global new_ssn
    fake = Faker()
    new_ssn = fake.ssn()
    print('New SSN:' + new_ssn)


# 在搜索框中输入ssn,查看是否已存在
def search_new_ssn():
    wait = WebDriverWait(driver, 2)  # 等待ssn visible
    ssn_input = wait.until(EC.element_to_be_clickable((By.ID, 'SSN')))
    ssn_input.click()
    ssn_input.send_keys(new_ssn)  # 输入 SSN
    # 点击搜索按钮
    search_button = driver.find_element(By.XPATH, '//*[@id="body"]/section/form/fieldset/p/button[1]')
    search_button.click()
    # 等待表格的出现
    # wait = WebDriverWait(driver,10)
    table_prompt = EC.text_to_be_present_in_element((By.ID, 'AppplicationTable'), 'No data available in table')
    WebDriverWait(driver, 10).until(table_prompt)


# 新建application, 单击create button, 然后进入新建application interview的页面，输入数据
def create_new_application():
    # 在搜索页面单击Create button
    button_create = driver.find_element(By.ID, "btnLink")
    button_create.click()
    time.sleep(2)  # 处理下弹窗前，需要等待，让弹窗加载2s

    # 在弹出的窗口上单击 Agree button
    Button_Agree = driver.find_element(By.XPATH, '/html/body/div[1]/section/form/div/div/div/div[3]/button')
    Button_Agree.click()

    # 输入数据
    driver.find_element(By.ID, 'AmountRequested').send_keys(1000)
    applicant_ssn = driver.find_element(By.ID, 'Applicant_SSN')
    applicant_ssn.click()  # 单击一下applicant ssn 的输入框，否则老是无效输入
    applicant_ssn.send_keys(new_ssn)
    # 自定义name列表，随机输入名字
    first_name_group = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
    last_name_group = ['Green', 'Baker', 'Noah']
    first_name = random.choice(first_name_group)
    last_name = random.choice(last_name_group)
    # 定位并输入多个字段的数据
    input_fields = {
        # Basic loan information
        # "AmountRequested": 1000, #不知道为啥使用循环无法有效输入
        "LoanSourceId": 'CUSTOMER RECOMMENDED (5)',
        "LoanPurposeId": 'CHRISTMAS (1)',
        "Applicant_Birthdate": '8/8/1998',
        "Applicant_FirstName": first_name,
        "Applicant_LastName": last_name,
        "Applicant_MaritalStatusId": 'Unmarried',
        # Residence info
        "ResidenceStatusId": 'Rent',
        "DateOfResidence": '1/1/2010',
        "Applicant_CurrentAddress_Address1": '2220 RIDGEVIEW ST',
        "Applicant_CurrentAddress_Zip": 76119 - 3117,
        # Emp info
        "Applicant_EmploymentHistory_0__Employer": 'Marsk',
        "Applicant_EmploymentHistory_0__Industry": 'EDUCATION',
        # "Applicant_EmploymentHistory_0__Position":'TEACHER',
        "Applicant_EmploymentHistory_0__DateEmployed": '8/8/2008',
        "Applicant_EmploymentHistory_0__NetSalary": 10000,
        # Bank info
        "Applicant_BankName": 'Bank of US',
        "Applicant_CheckingAccount": 'Y',
        "Applicant_SavingAccount": 'Y',
        # Hometown info
        "HomeTown": 'Dallas',
        "Friend": 'Jack Steve',
        "FriendPhone_PhoneTypeId": 'Cell',
        "Applicant_EmploymentHistory_0__Position": 'TEACHER',
        "Rent_LandlordName": 'Tom Green',
        "DeclaredBankruptcy": 'N'
    }
    for field, value in input_fields.items():
        driver.find_element(By.ID, field).send_keys(value)
    # 输入电子邮件
    driver.find_element(By.ID, 'Applicant_Emails_0__EmailAddress').send_keys('test@gmail.com')
    # 输入friend phone number
    driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').click()
    driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').send_keys('8598379823')
    # 输入County Name
    Select(driver.find_element(By.NAME, 'Applicant.CurrentAddress.County')).select_by_visible_text(
        'OUT OF STATE (1000)')
    # 选择 mail的radio
    driver.find_element(By.ID, 'mail').click()
    # 单击create button
    driver.find_element(By.ID, 'btnCreate').click()
    time.sleep(2)
    # 如果是AL的branch,则执行下面的方法
    al_state_create_new_application()
    """
    下面代码适用于除了09之外的branch
    # 等待App number 出现，就是application创建成功
    application = EC.text_to_be_present_in_element((By.ID,'additionalHeaderInfo'),'Application')
    # application字样出现代表app成功
    WebDriverWait(driver,10).until(application)
    # 获取app_number
    global app_number
    app_number = driver.find_element(By.XPATH,'//*[@id="additionalHeaderInfo"]/b[1]/a').text
    print('app number:' + app_number)
    """
def al_state_create_new_application():
    # 如果有error 发生（090904），则返回到首页再去查看最新生成的app number
    back_to_main_menu()
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

# app创建成功后，进入checkout页面
def checkout_application():
    # 从首页进入check out页面
    back_to_main_menu()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Credit Application').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Checkout Application').click()
    # 输入app number 进入页面
    driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
    driver.find_element(By.ID, 'btnSearch').click()

    # 输入Applicant Gross Monthly Salary
    applicant_salary_monthly_salary = driver.find_element(By.ID, 'ApplicantSalaryGarnishments_VerifiedMonthlySalary')
    ActionChains(driver).double_click(applicant_salary_monthly_salary).perform()
    applicant_salary_monthly_salary.send_keys(15000)

    # Manager Approve info
    driver.find_element(By.ID, 'LoanApprovals_0__Approved').send_keys('Y')
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
    time.sleep(2)
    print('checkout 成功')


def enter_identification_info():
    # 如果是check out 后，进入了Credit Application页面，则选择Enter_identification_info link
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Enter/Edit Identification Information').click()

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


def payment_schedule():
    # 从首页进入payment inquiry页面
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry Search').click()
    driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
    driver.find_element(By.CLASS_NAME, 'btn').click()
    # 输入loan_amount
    ActionChains(driver).double_click(driver.find_element(By.ID, 'Input_RequestedAmount')).perform()
    driver.find_element(By.ID, 'Input_RequestedAmount').send_keys(1000)
    # 单击计算按钮
    driver.find_element(By.ID, 'calcInquiryBtn').click()
    time.sleep(2)
    # 选择terms为12期
    driver.find_element(By.ID, 'selectedLoanTerm').send_keys(12)
    driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a').click()

    # 在pop-up上选择ok
    prompt_object = driver.switch_to.alert
    print(prompt_object.text)
    prompt_object.accept()
    time.sleep(2)



