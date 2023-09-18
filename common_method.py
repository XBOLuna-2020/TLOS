# import random
# from selenium import webdriver
# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from faker import Faker
# from selenium.webdriver.chrome.options import Options
#
#
# class LoanSystemTest:
#     def __init__(self):
#         self.driver = webdriver.Chrome()  #使用Chrome 浏览器
#
#     def login(self, username, password):
#         LoanSystemTest.driver.get('http://mgrtest:tower1@uft-svr-010110/Tower010110/')  #MRGTEST 登录系统
#
#     def create_application(self):
#         # 在搜索页面单击Create button
#         button_create = driver.find_element(By.ID, "btnLink")
#         button_create.click()
#         time.sleep(2)  # 处理下弹窗前，需要等待，让弹窗加载2s
#
#         # 在弹出的窗口上单击 Agree button
#         Button_Agree = driver.find_element(By.XPATH, '/html/body/div[1]/section/form/div/div/div/div[3]/button')
#         Button_Agree.click()
#
#         # 输入数据
#         driver.find_element(By.ID, 'AmountRequested').send_keys(1000)
#         applicant_ssn = driver.find_element(By.ID, 'Applicant_SSN')
#         applicant_ssn.click()  # 单击一下applicant ssn 的输入框，否则老是无效输入
#         applicant_ssn.send_keys(new_ssn)
#         # 自定义name列表，随机输入名字
#         first_name_group = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
#         last_name_group = ['Green', 'Baker', 'Noah']
#         first_name = random.choice(first_name_group)
#         last_name = random.choice(last_name_group)
#         # 定位并输入多个字段的数据
#         input_fields = {
#             # Basic loan information
#             # "AmountRequested": 1000, #不知道为啥使用循环无法有效输入
#             "LoanSourceId": 'CUSTOMER RECOMMENDED (5)',
#             "LoanPurposeId": 'CHRISTMAS (1)',
#             "Applicant_Birthdate": '8/8/1998',
#             "Applicant_FirstName": first_name,
#             "Applicant_LastName": last_name,
#             "Applicant_MaritalStatusId": 'Unmarried',
#             # Residence info
#             "ResidenceStatusId": 'Rent',
#             "DateOfResidence": '1/1/2010',
#             "Applicant_CurrentAddress_Address1": '2220 RIDGEVIEW ST',
#             "Applicant_CurrentAddress_Zip": 76119 - 3117,
#             # Emp info
#             "Applicant_EmploymentHistory_0__Employer": 'Marsk',
#             "Applicant_EmploymentHistory_0__Industry": 'EDUCATION',
#             # "Applicant_EmploymentHistory_0__Position":'TEACHER',
#             "Applicant_EmploymentHistory_0__DateEmployed": '8/8/2008',
#             "Applicant_EmploymentHistory_0__NetSalary": 10000,
#             # Bank info
#             "Applicant_BankName": 'Bank of US',
#             "Applicant_CheckingAccount": 'Y',
#             "Applicant_SavingAccount": 'Y',
#             # Hometown info
#             "HomeTown": 'Dallas',
#             "Friend": 'Jack Steve',
#             "FriendPhone_PhoneTypeId": 'Cell',
#             "Rent_LandlordName": 'Tom Green',
#             "DeclaredBankruptcy": 'N'
#         }
#         for field, value in input_fields.items():
#             driver.find_element(By.ID, field).send_keys(value)
#         # 输入电子邮件
#         driver.find_element(By.ID, 'Applicant_Emails_0__EmailAddress').send_keys('test@gmail.com')
#         # 输入friend phone number
#         driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').click()
#         driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').send_keys('8598379823')
#         # 输入职业
#         time.sleep(5)
#         driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__Position').send_keys('TEACHER'),
#         # 输入County Name
#         Select(driver.find_element(By.NAME, 'Applicant.CurrentAddress.County')).select_by_visible_text(
#             'OUT OF STATE (1000)')
#         # 选择 mail的radio
#         driver.find_element(By.ID, 'mail').click()
#         # 单击create button
#         driver.find_element(By.ID, 'btnCreate').click()
#         time.sleep(2)
#
#         # 下面代码适用于除了09之外的branch
#         # 等待App number 出现，就是application创建成功
#         application = EC.text_to_be_present_in_element((By.ID, 'additionalHeaderInfo'), 'Application')
#         # application字样出现代表app成功
#         WebDriverWait(driver, 10).until(application)
#         # 获取app_number
#         global app_number
#         app_number = driver.find_element(By.XPATH, '//*[@id="additionalHeaderInfo"]/b[1]/a').text
#         print('app number:' + app_number)
#
#     def checkout_application(self):
#
#     def enter_identification_information(self):
#
#     def select_payment_inquiry(self):
#
#     def setup_account(self):
#
#     def check_account_creation(self):
#
#     def run_test(self):
#         self.login()

import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from faker import Faker
from selenium.webdriver.chrome.options import Options


class ApplyProcess:
    def __init__(self):
        self.driver = self.setup_driver()

    def setup_driver(self):
        # 停止脚本后，不会关闭浏览器
        options = Options()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
        # 清除浏览器缓存
        # driver.execute_script('window.sessionStorage.clear();')
        # driver.execute_script('window.localStorage.clear();')
        driver.maximize_window()
        return driver

    def back_to_main_menu(self):
        # driver.get('http://mgrtest:tower1@uft-svr-010110/Tower010110/')
        # time.sleep(1)
        logo = self.driver.find_element(By.CLASS_NAME, 'logo')
        logo.click()

    def access_application_interview(self):
        # 打开url 并且在用户名和密码放在里面
        self.driver.get('http://mgrtest:tower1@uft-svr-020539/Tower020539/')
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Credit Application').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Application Interview').click()

    def generate_new_ssn(self):
        # 生成新的SSN，并保存成global变量
        global new_ssn
        fake = Faker()
        new_ssn = fake.ssn()
        print('New SSN:' + new_ssn)

    def search_new_ssn(self):
        # 在搜索框中输入ssn,查看是否已存在
        wait = WebDriverWait(self.driver, 2)  # 等待ssn visible
        ssn_input = wait.until(EC.element_to_be_clickable((By.ID, 'SSN')))
        ssn_input.click()
        ssn_input.send_keys(new_ssn)  # 输入 SSN
        # 点击搜索按钮
        search_button = self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/fieldset/p/button[1]')
        search_button.click()
        # 等待表格的出现
        # wait = WebDriverWait(driver,10)
        table_prompt = EC.text_to_be_present_in_element((By.ID, 'AppplicationTable'), 'No data available in table')
        WebDriverWait(self.driver, 10).until(table_prompt)

    def create_new_application(self):
        # 在搜索页面单击Create button
        button_create = self.driver.find_element(By.ID, "btnLink")
        button_create.click()
        time.sleep(2)  # 处理下弹窗前，需要等待，让弹窗加载2s

        # 在弹出的窗口上单击 Agree button
        Button_Agree = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/form/div/div/div/div[3]/button')
        Button_Agree.click()

        # 输入数据
        self.driver.find_element(By.ID, 'AmountRequested').send_keys(1000)
        applicant_ssn = self.driver.find_element(By.ID, 'Applicant_SSN')
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
            "Rent_LandlordName": 'Tom Green',
            "DeclaredBankruptcy": 'N'
        }
        for field, value in input_fields.items():
            self.driver.find_element(By.ID, field).send_keys(value)
        # 输入电子邮件
        self.driver.find_element(By.ID, 'Applicant_Emails_0__EmailAddress').send_keys('test@gmail.com')
        # 输入friend phone number
        self.driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').send_keys('8598379823')
        # 输入职业
        time.sleep(5)
        self.driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__Position').send_keys('TEACHER'),
        # 输入County Name
        Select(self.driver.find_element(By.NAME, 'Applicant.CurrentAddress.County')).select_by_visible_text(
            'OUT OF STATE (1000)')
        # 选择 mail的radio
        self.driver.find_element(By.ID, 'mail').click()
        # 单击create button
        self.driver.find_element(By.ID, 'btnCreate').click()
        time.sleep(2)

        # 下面代码适用于除了09之外的branch
        # 等待App number 出现，就是application创建成功
        application = EC.text_to_be_present_in_element((By.ID, 'additionalHeaderInfo'), 'Application')
        # application字样出现代表app成功
        WebDriverWait(self.driver, 10).until(application)
        # 获取app_number
        global app_number
        app_number = self.driver.find_element(By.XPATH, '//*[@id="additionalHeaderInfo"]/b[1]/a').text
        print('app number:' + app_number)

    def checkout_application(self):
        # app创建成功后，进入checkout页面
        # driver.get('http://mgrtest:tower1@uft-svr-080801/Tower080801/ApplicationCheckout/EditApplicationCheckout/36e8ce31-eb9c-48c3-ab14-b06d000d9a2e')
        # 从首页进入check out页面
        self.back_to_main_menu()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Credit Application').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Checkout Application').click()
        # 输入app number 进入页面
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.ID, 'btnSearch').click()

        # 输入Applicant Gross Monthly Salary
        applicant_salary_monthly_salary = self.driver.find_element(By.ID,
                                                              'ApplicantSalaryGarnishments_VerifiedMonthlySalary')
        ActionChains(self.driver).double_click(applicant_salary_monthly_salary).perform()
        applicant_salary_monthly_salary.send_keys(15000)

        # Manager Approve info
        self.driver.find_element(By.ID, 'LoanApprovals_0__Approved').send_keys('Y')
        # 输入 Credit Limit
        credit_limit = self.driver.find_element(By.ID, 'CreditLimit')
        credit_limit.clear()  # 因为有默认值，需要先清除默认值，否则会在后面追加
        credit_limit.send_keys(1000)
        # 规定Amount Approved
        amount_approved = self.driver.find_element(By.ID, 'LoanApprovals_0__ApprovedAmount')
        amount_approved.clear()
        amount_approved.send_keys(10000)

        # 输入Plan A 的数据
        plan_A_input_box = self.driver.find_element(By.ID, 'planA')
        ActionChains(self.driver).double_click(plan_A_input_box).perform()  # Plan A 需要双击后才可以输入数字清除默认数值
        plan_A_input_box.send_keys('1000')
        plan_a = 'RN CUST, WANTS$1000, SELF EMPLOYED 3 YRS, BUYING HER HOME 2 YR RES, HAS C/S C 28% DTI, IM OK TO ADV $1000' \
                 ' WILL BE A $4000 NL, DHPZ, 26 X 258 WILL NEED ID/POI/PP TO CLOSE VOIDED CHK AND 0 FORMER CL BC. '
        self.driver.find_element(By.ID, 'commentText1').send_keys(plan_a)

        # 输入security info
        # self.driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys('Personal Property - Household Goods - One Signatures')
        self.driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys(
            'Endorser')
        self.driver.find_element(By.ID, 'ApplicantSignature').send_keys('Y')
        # self.driver.find_element(By.ID, 'SpouseSignature').send_keys('Y')
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form[2]/p/input[3]').click()
        time.sleep(2)
        print('checkout 成功')

    def enter_identification_info(self):
        # 如果是check out 后，进入了Credit Application页面，则选择Enter_identification_info link
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Enter/Edit Identification Information').click()
        # 输入app number 进入页面
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.ID, 'btnSearch').click()

        # 选择Photo Compare
        self.driver.find_element(By.ID, 'ApplicantIdentification_PhotosCompare').send_keys('Y')
        # 输入Applicant Employment History 信息
        '''driver.find_element(By.ID, 'ApplicantEmployment_VerifiedNetIncome').clear()
        self.driver.find_element(By.ID, 'ApplicantEmployment_VerifiedNetIncome').send_keys(1000)
        self.driver.find_element(By.ID, 'ApplicantEmployment_NetIncomeVerified').send_keys('Yes')
        '''
        # 输入References信息
        self.driver.find_element(By.ID, 'References_0__ReferenceFor').send_keys('Applicant')
        self.driver.find_element(By.ID, 'References_0__ReferenceRelationship').send_keys('Friends')
        self.driver.find_element(By.ID, 'References_0__FirstName').send_keys('Lucus')
        self.driver.find_element(By.ID, 'References_0__LastName').send_keys('Boke')
        self.driver.find_element(By.ID, 'References_0__HomePhone_PhoneNumber').send_keys('6662647218')
        # 单击create按钮
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div/p[2]/input[3]').click()
        print('enter id infor 成功')
        time.sleep(2)

    def payment_schedule(self):
        # 从首页进入payment inquiry页面
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry Search').click()
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # 输入loan_amount
        ActionChains(self.driver).double_click(self.driver.find_element(By.ID, 'Input_RequestedAmount')).perform()
        self.driver.find_element(By.ID, 'Input_RequestedAmount').send_keys(1000)
        # 单击计算按钮
        self.driver.find_element(By.ID, 'calcInquiryBtn').click()
        time.sleep(2)

        # 选择terms
        self.driver.find_element(By.ID, 'selectedLoanTerm').send_keys(21)
        # 单击Confirm button
        self.driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a').click()

        # 在pop-up上选择ok
        prompt_object = self.driver.switch_to.alert
        prompt_object.accept()
        time.sleep(2)

        # 单击print preview 按钮
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[2]').click()
        time.sleep(2)  # 切换到payment Inquiry页面
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        # 单击eSign button
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[3]').click()
        time.sleep(3)
        self.driver.switch_to.window(handles[0])
        print('payment 设置成功')

    def setup_account(self):
        # 从Payment Inquiry页面开始创建Account
        # 单击 Account Setup 按钮
        self.driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a[2]').click()
        time.sleep(2)
        # 单击 Disbursements of Proceeds 中的的下拉列表
        self.driver.find_element(By.ID, 'Disbursements_Checks_0__IsPayableToCustomerYesNo').send_keys('Y')
        # 找到，清除默认值，并输入Disbursements of Proceeds 的 Amount
        disbursements_balance = self.driver.find_element(By.ID, 'TotalToAccountFor').get_attribute('value')
        disbursements_checks_amount = self.driver.find_element(By.ID, 'Disbursements_Checks_0__LoanCheckAmount')
        ActionChains(self.driver).double_click(disbursements_checks_amount).perform()
        disbursements_checks_amount.send_keys(disbursements_balance)
        # 单击eSign button,等待account号出现
        self.driver.find_element(By.ID, 'openESig').click()
        # 设置等待account出现后才打印出来
        account = EC.text_to_be_present_in_element((By.ID, 'additionalHeaderInfo'), 'Account')
        WebDriverWait(self.driver, 10).until(account)
        account_number = self.driver.find_element(By.XPATH, '//*[@id="additionalHeaderInfo"]/b[1]/a').text
        print('account number:' + account_number)

    def close_driver(self):
        self.driver.quit()

    def test(self):
        self.driver.get('http://mgrtest:tower1@uft-svr-020539/Tower020539/PaymentInquiry/FromApplication/19d5cab6-41ad-4812-99b5-b07c01738134')

        # 输入loan_amount
        ActionChains(self.driver).double_click(self.driver.find_element(By.ID, 'Input_RequestedAmount')).perform()
        self.driver.find_element(By.ID, 'Input_RequestedAmount').send_keys(1000)
        # 单击计算按钮
        self.driver.find_element(By.ID, 'calcInquiryBtn').click()
        time.sleep(2)

        # 选择terms为18期
        self.driver.find_element(By.ID, 'selectedLoanTerm').send_keys(21)
        # 单击Confirm button
        self.driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a').click()

        # 在pop-up上选择ok
        prompt_object = self.driver.switch_to.alert
        prompt_object.accept()
        time.sleep(2)

        # 单击print preview 按钮
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[2]').click()
        time.sleep(2)  # 切换到payment Inquiry页面
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        # 单击eSign button
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[3]').click()
        time.sleep(3)
        self.driver.switch_to.window(handles[0])

        # 单击 Account Setup 按钮
        self.driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a[2]').click()
        time.sleep(2)
        # 单击 Disbursements of Proceeds 中的的下拉列表
        self.driver.find_element(By.ID, 'Disbursements_Checks_0__IsPayableToCustomerYesNo').send_keys('Y')
        # 找到，清除默认值，并输入Disbursements of Proceeds 的 Amount
        disbursements_balance = self.driver.find_element(By.ID, 'TotalToAccountFor').get_attribute('value')
        disbursements_checks_amount = self.driver.find_element(By.ID, 'Disbursements_Checks_0__LoanCheckAmount')
        ActionChains(self.driver).double_click(disbursements_checks_amount).perform()
        disbursements_checks_amount.send_keys(disbursements_balance)
        # 单击eSign button,等待account号出现
        self.driver.find_element(By.ID, 'openESig').click()
        # 设置等待account出现后才打印出来
        account = EC.text_to_be_present_in_element((By.ID, 'additionalHeaderInfo'), 'Account')
        WebDriverWait(self.driver,10).until(account)
        account_number = self.driver.find_element(By.XPATH, '//*[@id="additionalHeaderInfo"]/b[1]/a').text
        print('account number:' + account_number)

