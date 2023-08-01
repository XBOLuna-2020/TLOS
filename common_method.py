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
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)  # 实例化
driver.maximize_window()  # 窗口最大化

# 声明 app_number 为全局变量
app_number = ''


# 在首页中找到 Credit Application -> Application Interview 的链接并单击
def access_application_interview():
    # 打开url 并且在用户名和密码放在里面
    driver.get('http://mgrtest:tower1@uft-svr-010110/Tower010110/')
    link_credit_application = driver.find_element(By.XPATH,'//*[@id="body"]/section/div[1]/a[1]')
    # Link_CreditApplication = driver1.find_element(By.LINK_TEXT,'Credit Application')
    link_credit_application.click()


    # 单击链接1.Application Interview
    link_credit_application = driver.find_element(By.XPATH,'/html/body/div/section/a[1]')
    link_credit_application.click()


# 生成新的SSN，并保存成global变量
def generate_new_ssn():
    global new_ssn
    fake = Faker()
    new_ssn = fake.ssn()
    print('New SSN:' + new_ssn)


# 在搜索框中输入ssn,查看是否已存在
def search_new_ssn():
    wait = WebDriverWait(driver,10)  # 等待ssn visible
    ssn_input = wait.until(EC.element_to_be_clickable((By.ID,'SSN')))
    # ssn_input = driver.find_element(By.ID,"SSN")
    ssn_input.click()
    # ssn_input.clear()
    ssn_input.send_keys(new_ssn) #输入 SSN
    # 点击搜索按钮
    search_button = driver.find_element(By.XPATH,'//*[@id="body"]/section/form/fieldset/p/button[1]')
    search_button.click()
    # 等待表格的出现
    # wait = WebDriverWait(driver,10)
    table_prompt = EC.text_to_be_present_in_element((By.ID,'AppplicationTable'),'No data available in table')
    WebDriverWait(driver,10).until(table_prompt)


# 新建application, 单击create button, 然后进入新建application interview的页面，输入数据
def create_new_application():
    # 在搜索页面单击Create button
    button_create = driver.find_element(By.ID,"btnLink")
    button_create.click()
    time.sleep(2)  # 处理下弹窗前，需要等待，让弹窗加载2s

    # 在弹出的窗口上单击 Agree button
    Button_Agree = driver.find_element(By.XPATH,'/html/body/div[1]/section/form/div/div/div/div[3]/button')
    Button_Agree.click()

    # 输入数据
    driver.find_element(By.ID,'AmountRequested').send_keys(1000)
    applicant_ssn = driver.find_element(By.ID, 'Applicant_SSN')
    applicant_ssn.click()  # 单击一下applicant ssn 的输入框，否则老是无效输入
    applicant_ssn.send_keys(new_ssn)
    # 自定义name列表，随机输入名字
    first_name_group = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
    last_name_group = ['Green','Baker','Noah']
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
        # Residence info
        "ResidenceStatusId": 'Rent',
        "DateOfResidence": '1/1/2010',
        "Applicant_CurrentAddress_Address1": '2220 RIDGEVIEW ST',
        "Applicant_CurrentAddress_Zip": 76119-3117,
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
        "HomeTown":'Dallas',
        "Friend":'Jack Steve',
        "FriendPhone_PhoneTypeId":'Cell',
        "Applicant_EmploymentHistory_0__Position": 'TEACHER',
        "Rent_LandlordName":'Tom Green',
        "DeclaredBankruptcy": 'N'
    }
    for field, value in input_fields.items():
        driver.find_element(By.ID, field).send_keys(value)
    # 输入电子邮件
    driver.find_element(By.ID,'Applicant_Emails_0__EmailAddress').send_keys('test@gmail.com')
    # 输入friend phone number
    driver.find_element(By.XPATH,'//*[@id="FriendPhone_PhoneNumber"]').click()
    driver.find_element(By.XPATH,'//*[@id="FriendPhone_PhoneNumber"]').send_keys(8598379823)
    # 输入County Name
    Select(driver.find_element(By.NAME,'Applicant.CurrentAddress.County')).select_by_visible_text('OUT OF STATE (1000)')
    # 选择 mail的radio
    driver.find_element(By.ID,'mail').click()
    # 单击create button
    driver.find_element(By.ID,'btnCreate').click()
    # 等待App number 出现，就是application创建成功
    application = EC.text_to_be_present_in_element((By.ID,'additionalHeaderInfo'),'Application')
    # application字样出现代表app成功
    WebDriverWait(driver,10).until(application)
    # 获取app_number
    global app_number
    app_number = driver.find_element(By.XPATH,'//*[@id="additionalHeaderInfo"]/b[1]/a').text
    print('app number:' + app_number)

    # 将app_number保存到文件中
    with open('app_number.txt','w') as file:
        file.write(app_number)



# app创建成功后，进入checkout页面
def checkout_application():
    # 单击下拉列表目录
    driver.find_element(By.ID,'dropdownMenu1').click()
    # 选择checkout
    driver.find_element(By.XPATH,'//*[@id="pageTitle"]/div/ul/li[3]/a').click()

    # 输入Applicant Gross Monthly Salary
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
    driver.find_element(By.ID, ' entText1').send_keys(plan_a)

    # 输入security info
    driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys('Endorser')
    driver.find_element(By.ID, 'ApplicantSignature').send_keys('Y')
    driver.find_element(By.XPATH, '//*[@id="body"]/section/form[2]/p/input[3]').click()

    print('checkout 成功')
    driver.minimize_window()


