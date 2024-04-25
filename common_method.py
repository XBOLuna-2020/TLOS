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
# import cancel_pending_application


class ApplyProcess:
    def __init__(self):
        self.driver = self.setup_driver()

    def setup_driver(self):
        # 停止脚本后，不会关闭浏览器
        # options = Options()
        # options.add_experimental_option('detach', True)
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver  #千万不要忘记返回值 driver


    def enter_amount(self, locator_value, amount):
        # 定位并输入金额
        try:
            element = self.driver.find_element(By.ID, locator_value)
            ActionChains(self.driver).double_click(element).perform()
            element.send_keys(amount)
            return element
        except Exception as e:
            print(f"Element with '{locator_value}' not found ")
            return None

    def back_to_main_menu(self):
        logo = self.driver.find_element(By.CLASS_NAME, 'logo')
        logo.click()

    def cancel_pending_app(self):
        self.driver.get('http://mgrtest:tower1@uft-svr-090904/Tower090904/')
        # 获取所有行（包括标题行）
        from selenium.webdriver.common.by import By
        rows = self.driver.find_elements(By.TAG_NAME, 'tr')
        # 跳过标题行，从第二行开始迭代
        for _ in range(1, len(rows)):
            # 每次循环重新获取所有行（因为页面已经刷新）
            rows = self.driver.find_elements(By.TAG_NAME, 'tr')
            row = rows[_]
            # 获取每行的App Number和URL
            app_number = row.find_element(By.XPATH, '//*[@id="body"]/section/table/tbody/tr[2]/td[2]').text
            url_element = row.find_element(By.XPATH, '//*[@id="body"]/section/table/tbody/tr[2]/td[3]/a')
            url = url_element.get_attribute('href')
            # 单击链接，进入app页
            self.driver.get(url)
            # 进入app页后，导航至相应的checkout页面
            # 单击下拉列表目录
            self.driver.find_element(By.ID, 'dropdownMenu1').click()
            # 选择checkout
            self.driver.find_element(By.XPATH, '//*[@id="pageTitle"]/div/ul/li[3]/a').click()

            # 输入Applicant Gross Monthly Salary
            from selenium.webdriver.common.by import By
            applicant_salary_monthly_salary = self.driver.find_element(By.ID,
                                                                  'ApplicantSalaryGarnishments_VerifiedMonthlySalary')
            ActionChains(self.driver).double_click(applicant_salary_monthly_salary).perform()
            applicant_salary_monthly_salary.send_keys(15000)
            # spouse_salary_monthly_salary = self.driver.find_element(By.ID,
            #                                                            'SpouseSalaryGarnishments_VerifiedMonthlySalary')
            # ActionChains(self.driver).double_click(spouse_salary_monthly_salary).perform()
            # spouse_salary_monthly_salary.send_keys(15000)

            # Manager Approve info
            self.driver.find_element(By.ID, 'LoanApprovals_0__Approved').send_keys('Y')
            # 输入 Credit Limit
            credit_limit = self.driver.find_element(By.ID, 'CreditLimit')
            credit_limit.clear()  # 因为有默认值，需要先清除默认值，否则会在后面追加
            credit_limit.send_keys(1000)
            # 规定Amount Approved
            amount_approved = self.driver.find_element(By.ID, 'LoanApprovals_0__ApprovedAmount')
            amount_approved.clear()
            amount_approved.send_keys(1000)

            # 输入Plan A 的数据
            plan_A_input_box = self.driver.find_element(By.ID, 'planA')
            ActionChains(self.driver).double_click(plan_A_input_box).perform()  # Plan A 需要双击后才可以输入数字清除默认数值
            plan_A_input_box.send_keys('1000')
            plan_a = 'RN CUST, WANTS$1000, SELF EMPLOYED 3 YRS, BUYING HER HOME 2 YR RES, HAS C/S C 28% DTI, IM OK TO ADV $1000' \
                     ' WILL BE A $4000 NL, DHPZ, 26 X 258 WILL NEED ID/POI/PP TO CLOSE VOIDED CHK AND 0 FORMER CL BC. '
            self.driver.find_element(By.ID, 'commentText1').send_keys(plan_a)

            # 输入security info
            self.driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys('Endorser')
            self.driver.find_element(By.ID, 'ApplicantSignature').send_keys('Y')
            # 在cancel 下拉列表中选择Y
            cancel_dropdown = self.driver.find_element(By.ID, 'Cancelled')
            cancel_dropdown.send_keys('Y')
            #单击 create/update button
            self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form[2]/p/input[3]').click()

            # 如果页面报错，更新报错的section
            # max_attempts = 3  # 设置最大尝试次数，防止无限循环
            # for attempt in range(max_attempts):
            #     try:
            #         # 在这里应该检查是否有错误消息，如果有，则抛出异常，触发except分支
            #         error_message_element = self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/fieldset/div[1]')
            #         error_messages = error_message_element.text.split('\n')
            #
            #         # 根据不同的错误消息执行不同的操作
            #         for error_message in error_messages:
            #             if 'Online Lending is not a valid Loan Source' in error_message:
            #                 self.handle_source_error()
            #             elif 'Choose address or update original entry (AI)' in error_message:
            #                 self.handle_address_error()
            #             elif 'County is required for the physical address' in error_message:
            #                 self.hanle_county_error()
            #             elif 'The Industry field is required' in error_message:
            #                 self.handle_industry_error()
            #             elif 'The Job Title field is required' in error_message:
            #                 self.handle_job_title_error()
            #             elif 'Previous employment is required if duration of current employment is less than 3 years.' in error_message:
            #                 self.handle_previous_employment_error()
            #             elif 'Previous employment duration is required if duration of current employment is less than 3 years' in error_message:
            #                 continue
            #                 # self.handle_previous_employment_duration_error()
            #             elif 'Bank Name is required' in error_message:
            #                 self.handle_bank_name_error()
            #             elif 'Please choose Y or N for Saving Account' in error_messages or 'Please choose Y or N for Checking Account' in error_messages:
            #                 continue
            #             elif 'Friend Phone Number is required' in error_message:
            #                 self.handle_friend_phone_number_error()
            #             elif 'The Property Description field is required' in error_message:
            #                 self.handle_own_residence_info_error()
            #             elif 'Landlord\'s Name is required.' in error_message:
            #                 self.handle_landlord_name_error()
            #         # 进入app页后，下拉到页面底部
            #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #         # 更新完页面后，应该单击按钮，但是此处单击按钮后没生效，于是单击了两遍
            #         self.driver.find_element(By.XPATH, '//*[@id="btnUpdate"]').click()
            #         self.driver.find_element(By.XPATH, '//*[@id="btnUpdate"]').click()
            #         print('单击了更新按钮')
            #         time.sleep(5)
            #         # 每次更新后，都单击update button
            #
            #
            #        # 如果没有错误消息，说明更新成功，跳出循环
            #         break
            #     except Exception as e:
            #         print(f'An error occurred while updateing: {str(e)}')

            # 如果单击update按钮后，页面报错，则需要进一步更新页面
            # self.update_app_according_error()
            # 如果是Source 选择的是‘Online Lending’,则先把source 改为别的
            # 如果单击更新按钮后，页面没有报错，则成功更新
            print('App:' + app_number + '已处理')
            # 返回到首页
            self.driver.find_element(By.CLASS_NAME, 'logo').click()


    def update_app_according_error(self):
        # 如果页面报错，更新报错的section
        max_attempts = 3  # 设置最大尝试次数，防止无限循环
        for attempt in range(max_attempts):
            try:
                # 在这里应该检查是否有错误消息，如果有，则抛出异常，触发except分支
                error_message_element = self.driver.find_element(By.CLASS_NAME,'validation-summary-errors')
                error_message = error_message_element.text
                # 根据不同的错误消息执行不同的操作
                if 'Choose address or update original entry (AI)' in error_message:
                    self.handle_address_error()
                elif 'Online Lending is not a valid Loan Source' in error_message:
                    self.handle_source_error()
                elif 'County is required for the physical address' in error_message:
                    self.hanle_county_error()
                elif 'The Industry field is required' in error_message:
                    self.handle_industry_error()
                elif 'The Job Title field is required' in error_message:
                    self.handle_job_title_error()
                elif 'Previous employment is required if duration of current employment is less than 3 years.' in error_message:
                    self.handle_previous_employment_error()
                elif 'Bank Name is required.' in error_message:
                    self.handle_bank_name_error()
                elif 'Friend Phone Number is required' in error_message:
                    self.handle_friend_phone_number_error()
                elif 'The Property Description field is required' in error_message or 'Approximate Value is required' in error_message:
                    self.handle_own_residence_info_error()
                elif 'Landlord Name is required' in error_message:
                    self.handle_landlord_name_error()

                # 如果没有错误消息，说明更新成功，跳出循环
                break

            except Exception as e:
                print(f'An error occurred while updateing: {str(e)}')
        if attempt < max_attempts -1:
            # 在下一次的尝试前，等待一段时间
            time.sleep(2)
        else:
            # 达到最大尝试次数， 可以选择抛出异常或者采取其他措施
            print('Maximum attempts reached. Updated unsuccessful.')

    # 定义处理不同错误的方法
    def handle_address_error(self):
        # 选中地址的单选项，总是报错
        # 修改原来的地址
        Applicant_CurrentAddress_Address = self.driver.find_element(By.ID, 'Applicant_CurrentAddress_Address1')
        Applicant_CurrentAddress_Address.clear()
        Applicant_CurrentAddress_Address.send_keys('1311 ROOSEVELT ST')
        Applicant_CurrentAddress_Zip = self.driver.find_element(By.ID, 'Applicant_CurrentAddress_Zip')
        Applicant_CurrentAddress_Zip.clear()
        Applicant_CurrentAddress_Zip.send_keys('39567-6455')
        print()

    def handle_source_error(self):
        self.driver.find_element(By.ID, 'LoanSourceId').send_keys('CUSTOMER RECOMMENDED (5)')
        print('Handling Source Error')

    def hanle_county_error(self):
        # County 选择30
        Select(self.driver.find_element(By.NAME, 'Applicant.CurrentAddress.County')).select_by_value(
            'Jackson (30)')
        print('Handling County Error')

    def handle_industry_error(self):
        # Employment History Applicant_Industry
        self.driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__Industry').send_keys('EDUCATION')
        time.sleep(2)
        print('Handling Industry Error')

    def handle_job_title_error(self):
        # Employment History Applicant_Job Title
        self.driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__Position').send_keys('TEACHER')
        print('Handling Job Title Error')

    def handle_previous_employment_error(self):
        self.driver.find_element(By.ID,'Applicant_EmploymentHistory_0__PreviousEmployment').send_keys('Microsoft')
        self.driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__PreviousDurationYears').send_keys(4)
        print('Handling Previous Employment Error')

    def handle_previous_employment_duration_error(self):
        self.driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__PreviousDurationYears').send_keys(4)
        print('Handling Previous Employment Error')

    def handle_bank_name_error(self):
        # If the bank info is empty, fill the field
        self.driver.find_element(By.ID, 'Applicant_BankName').send_keys('Bank US')
        self.driver.find_element(By.ID, 'Applicant_CheckingAccount').send_keys('Y')
        self.driver.find_element(By.ID, 'Applicant_SavingAccount').send_keys('Y')
        print('Handing Bank Info Error')

    def handle_friend_phone_number_error(self):
        # 输入朋友的电话
        # 输入friend phone number
        self.driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').send_keys('8598379823')
        # friend_phone = self.driver.find_element(By.ID, 'FriendPhone_PhoneNumber')
        # ActionChains(self.driver).double_click(friend_phone).perform()
        print('Handling Friend Phone Error')

    def handle_own_residence_info_error(self):
        # 如果自己购买房产，需要填写下列信息
        # Date Purchased
        self.driver.find_element(By.ID, 'Owned_DatePurchased').send_keys('1/1/2024')
        # Purchase Price
        purchase_price = self.driver.find_element(By.ID, 'Owned_PurchasePrice')
        ActionChains(self.driver).double_click(purchase_price).perform()
        purchase_price.send_keys(3000000)
        # Approximate Value
        approximate_value = self.driver.find_element(By.ID, 'Owned_ApproximateValue')
        ActionChains(self.driver).double_click(approximate_value).perform()
        approximate_value.send_keys(3000000)
        # Property Description
        self.driver.find_element(By.ID, 'Owned_ResidenceCategoryId').send_keys('ONE STORY BRICK, 3 BEDROOMS')
        print('Handling Own Residence Info Error')

    def handle_landlord_name_error(self):
        self.driver.find_element(By.ID, 'Rent_LandlordName').send_keys('William')
        self.driver.find_element(By.ID, 'Rent_RentAmount').send_keys(500)
        print('Handling Rent Residence Info Error')

    def access_application_interview(self):
        # 打开url 并且在用户名和密码放在里面
        self.driver.get('http://mgrtest:tower1@uft-svr-070377/tower070377/')
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
        self.driver.find_element(By.ID, 'AmountRequested').send_keys(3500)
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
            "Applicant_CurrentAddress_Address1": '136 W LOUISIANA AVE',
            "Applicant_CurrentAddress_Address2":'APRTMENT NO 5, UNIT 4, LEVEL 14, ROOM NUMBER 1405',
            "Applicant_CurrentAddress_Zip":71082-2836,
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
            "DeclaredBankruptcy": 'N',
            # Auto Info
            "Cars_0__Year": '2020',
            "Cars_0__Make": 'AUDI',
            "Cars_0__Model":'CL',
            "Cars_0__Condition":'Excellent',
            "Cars_0__LienHolder":'PingAn'

        }
        for field, value in input_fields.items():
            self.driver.find_element(By.ID, field).send_keys(value)
        # 输入电子邮件
        self.driver.find_element(By.ID, 'Applicant_Emails_0__EmailAddress').send_keys('test@gmail.com')
        # 输入friend phone number
        self.driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="FriendPhone_PhoneNumber"]').send_keys('8598379823')
        # 输入职业
        time.sleep(10)
        job_title = self.driver.find_element(By.ID, 'Applicant_EmploymentHistory_0__Position')
        job_title_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'Applicant_EmploymentHistory_0__Position'))
        )
        Select(job_title_dropdown).select_by_index(2)
        # time.sleep(5)
        # 输入County Name
        Select(self.driver.find_element(By.NAME, 'Applicant.CurrentAddress.County')).select_by_visible_text(
            'Caddo Parish (09)')
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
        credit_limit.send_keys(3500)
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
        # self.driver.find_element(By.ID, 'SecurityOnLoan2_SecurityOnLoan').send_keys('Auto')
        self.driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys('Endorser')
        # 选择签名
        self.driver.find_element(By.ID, 'ApplicantSignature').send_keys('Y')
        # self.driver.find_element(By.ID, 'SpouseSignature').send_keys('Y')
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form[2]/p/input[3]').click()
        time.sleep(2)
        print('checkout 成功')

    def RE_checkout_loan(self):
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
        self.enter_amount('CreditLimit', 10000)
        # 规定Amount Approved
        self.enter_amount('LoanApprovals_0__ApprovedAmount', 10000)
        # 输入Plan A 的数据
        plan_A_input_box = self.driver.find_element(By.ID, 'planA')
        ActionChains(self.driver).double_click(plan_A_input_box).perform()  # Plan A 需要双击后才可以输入数字清除默认数值
        plan_A_input_box.send_keys('1000')
        plan_a = 'RN CUST, WANTS$1000, SELF EMPLOYED 3 YRS, BUYING HER HOME 2 YR RES, HAS C/S C 28% DTI, IM OK TO ADV $1000' \
                 ' WILL BE A $4000 NL, DHPZ, 26 X 258 WILL NEED ID/POI/PP TO CLOSE VOIDED CHK AND 0 FORMER CL BC. '
        self.driver.find_element(By.ID, 'commentText1').send_keys(plan_a)
        # security info 选择为 Real Estate
        self.driver.find_element(By.ID, 'SecurityOnLoan1_SecurityOnLoan').send_keys('Real Estate')
        # 弹窗单击OK
        self.driver.switch_to.alert.accept()
        # Property Address
        self.driver.find_element(By.ID, 'SecurityOnLoan1_RealEstateSecurity').send_keys('100 Mercantile St')
        # Is Real Estate Insured (Y/N)
        self.driver.find_element(By.ID, 'SecurityOnLoan1_RealEstateInsured').send_keys('Y')
        # Ins Expiration Date
        self.driver.find_element(By.ID, 'SecurityOnLoan1_RealEstateInsuranceExpiry').send_keys('1/1/2025')
        # Index
        self.driver.find_element(By.ID, 'SecurityOnLoan1_Index').send_keys('39046')
        # County/Parish
        self.driver.find_element(By.ID, 'SecurityOnLoan1_County').send_keys('Parish')
        # 选择签名下拉框
        self.driver.find_element(By.ID, 'ApplicantSignature').send_keys('Y')
        # 选择Will this loan pay off or refinance ANY existing mortgages? (Y/N)
        self.driver.find_element(By.ID, 'PayoffRefiAnyMortgage').send_keys('Y')
        # 选择Is loan a Homestead loan? (Y/N)
        self.driver.find_element(By.ID, 'HomesteadLoan').send_keys('N')
        # 单击底部create 按钮
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

    def RE_enter_identification_info(self):
        # real estate loan 输入 Identification information
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

        # Description
        self.driver.find_element(By.ID, 'RealEstateCollateral_0__Description').send_keys('test for real estate')
        # 调用enter_amount 方法在Home Appraisal Value， Home Quick Sale Value等输入数据
        self.enter_amount('RealEstateCollateral_0__AppraisalValue', 500000)
        self.enter_amount('RealEstateCollateral_0__QuickSaleValue', 400000)
        self.enter_amount('RealEstateCollateral_0__FirstMortgageValue', 300000)
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div/p[2]/input[3]').click()
        print('enter RE id infor 成功')

    def payment_schedule(self):
        # 从首页进入payment inquiry页面
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry Search').click()
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()

        # 输入loan_amount
        ActionChains(self.driver).double_click(self.driver.find_element(By.ID, 'Input_RequestedAmount')).perform()
        self.driver.find_element(By.ID, 'Input_RequestedAmount').send_keys(1500)
        # 输入保险
        # 单击计算按钮
        self.driver.find_element(By.ID, 'calcInquiryBtn').click()
        time.sleep(2)

        # 选择terms
        self.driver.find_element(By.ID, 'selectedLoanTerm').send_keys(21)
        # 单击Confirm button
        self.driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a').click()
        # 在pop-up上选择ok
        self.driver.switch_to.alert.accept()
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

    def RE_payment_schedule(self):
        # 从首页进入payment inquiry页面
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry Search').click()
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        # 选择Loan Type为F
        Select(self.driver.find_element(By.ID, 'loanType')).select_by_value("F")
        # 输入loan_amount
        self.enter_amount('Input_RequestedAmount', 5000)
        # 输入RE Title Serv
        self.enter_amount('reTitleServ', 100)
        # 单击计算按钮
        self.driver.find_element(By.ID, 'calcInquiryBtn').click()
        time.sleep(2)
        # 选择terms
        Select(self.driver.find_element(By.ID, 'selectedLoanTerm')).select_by_index(1)
        # 单击Confirm button
        self.driver.find_element(By.XPATH, '//*[@id="confirmTerm"]/div[2]/a').click()
        # 在pop-up上单击OK
        self.driver.switch_to.alert.accept()
        # 单击HUD-1按钮，进入HUD-1页面
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[2]').click()
        time.sleep(2)
        self.HUD()
        # 从HUD 1 页面返回后，单击Print按钮
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[3]').click()
        time.sleep(2)
        # 切换到payment Inquiry页面
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        time.sleep(2)
        # 单击eSign button
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/div[13]/div[2]/div/input[4]').click()
        # error:An error occurred: Alert Text: There was an error printing a document.
        time.sleep(3)
        self.driver.switch_to.window(handles[0])
        print('RE payment 设置成功')

    def RE_print_closing_documents(self):
        # 打印相关的文档
        self.back_to_main_menu()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Print Real Estate Closing Document').click()
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        # 在Proof 下拉列表选择Y
        self.driver.find_element(By.ID, 'PreCounseled').send_keys('Y')
        # 单击 Disbursements of Proceeds 中的的下拉列表
        self.driver.find_element(By.ID, 'Disbursements_Checks_0__IsPayableToCustomerYesNo').send_keys('Y')
        # 找到，清除默认值，并输入Disbursements of Proceeds 的 Amount
        disbursements_balance = self.driver.find_element(By.ID, 'TotalToAccountFor').get_attribute('value')
        self.enter_amount('Disbursements_Checks_0__LoanCheckAmount', disbursements_balance)
        # 单击print Closing Document button,等待Print字段出现
        self.driver.find_element(By.ID, 'printLoanCheckBtn').click()
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'pageAlerts'), 'Printed'))
        print('RE Closing Documents打印完成')

    def HUD(self):
        # 1101 - RE Title Search
        # self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Amount').clear()
        # self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Amount').send_keys('100')
        self.enter_amount('Hud1_1101_RE_Title_Search_Amount', 100)
        self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Name').send_keys('1101 - RE Title Search')
        self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Phone_PhoneNumber').send_keys(6061573515)
        self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Address_Address1').send_keys('BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1101_RE_Title_Search_Address_Zip').send_keys('70112')
        # 1102 - RE Closing Fee
        self.driver.find_element(By.ID, 'Hud1_1102_RE_Closing_Fee_Name').send_keys('1102 - RE Closing Fee')
        self.driver.find_element(By.ID, 'Hud1_1102_RE_Closing_Fee_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1102_RE_Closing_Fee_Phone_PhoneNumber').send_keys(606573515)
        self.driver.find_element(By.ID, 'Hud1_1102_RE_Closing_Fee_Address_Address1').send_keys('BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1102_RE_Closing_Fee_Address_Zip').send_keys('70112')
        # 1104 - RE Title Insurance
        self.driver.find_element(By.ID, 'Hud1_1104_RE_Title_Insurance_Name').send_keys('1104 - RE Title Insurance')
        self.driver.find_element(By.ID, 'Hud1_1104_RE_Title_Insurance_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1104_RE_Title_Insurance_Phone_PhoneNumber').send_keys('6061573515')
        self.driver.find_element(By.ID, 'Hud1_1104_RE_Title_Insurance_Address_Address1').send_keys('BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1104_RE_Title_Insurance_Address_Zip').send_keys('70112')
        # 1107 - Attorney Portion
        self.driver.find_element(By.ID, 'Hud1_1107_Attorney_Portion_Name').send_keys('1107 - Attorney Portion')
        self.driver.find_element(By.ID, 'Hud1_1107_Attorney_Portion_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1107_Attorney_Portion_Phone_PhoneNumber').send_keys('4621573515')
        self.driver.find_element(By.ID, 'Hud1_1107_Attorney_Portion_Address_Address1').send_keys('BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1107_Attorney_Portion_Address_Zip').send_keys('70112')
        # 1108 - Underwriter Portion
        self.driver.find_element(By.ID, 'Hud1_1108_Underwriter_Portion_Name').send_keys('1108 - Underwriter Portion')
        self.driver.find_element(By.ID, 'Hud1_1108_Underwriter_Portion_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1108_Underwriter_Portion_Phone_PhoneNumber').send_keys('6019573515')
        self.driver.find_element(By.ID, 'Hud1_1108_Underwriter_Portion_Address_Address1').send_keys(
            'BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1108_Underwriter_Portion_Address_Zip').send_keys('70112')
        # 1201 - Recording Fee
        self.driver.find_element(By.ID, 'Hud1_1201_Recording_Fee_Name').send_keys('1201 - Recording Fee')
        self.driver.find_element(By.ID, 'Hud1_1201_Recording_Fee_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1201_Recording_Fee_Phone_PhoneNumber').send_keys('6051573515')
        self.driver.find_element(By.ID, 'Hud1_1201_Recording_Fee_Address_Address1').send_keys(
            'BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1201_Recording_Fee_Address_Zip').send_keys('70112')
        # 1300 - Additional Charges
        self.driver.find_element(By.ID, 'Hud1_1300_Additional_Charges_Name').send_keys('1300 - Additional Charges')
        self.driver.find_element(By.ID, 'Hud1_1300_Additional_Charges_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1300_Additional_Charges_Phone_PhoneNumber').send_keys('6071573515')
        self.driver.find_element(By.ID, 'Hud1_1300_Additional_Charges_Address_Address1').send_keys(
            'BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1300_Additional_Charges_Address_Zip').send_keys('39032')
        # 1301 - Survey
        self.driver.find_element(By.ID, 'Hud1_1301_Survey_Name').send_keys('1301 - Survey')
        self.driver.find_element(By.ID, 'Hud1_1301_Survey_Phone_PhoneNumber').click()
        self.driver.find_element(By.ID, 'Hud1_1301_Survey_Phone_PhoneNumber').send_keys(
            '9781579515')
        self.driver.find_element(By.ID, 'Hud1_1301_Survey_Address_Address1').send_keys(
            'BOKE Str, NEW YORK')
        self.driver.find_element(By.ID, 'Hud1_1301_Survey_Address_Zip').send_keys('70112')
        # 单击Save button
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/input[34]').click()
        self.driver.find_element(By.XPATH, '//*[@id="body"]/section/form/a').click()
        time.sleep(2)

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

    def RE_setup_account(self):
        # 从首页进入payment inquiry页面
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Payment Inquiry Search').click()
        self.driver.find_element(By.ID, 'ApplicationNumber').send_keys(app_number)
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        # 单击 Account Setup 按钮 从payment 页面开始和personal一样了
        self.setup_account()









