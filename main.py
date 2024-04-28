from common_method import ApplyProcess


data_interview_application = 'data/data_application_interview.json'
loan = ApplyProcess(data_interview_application)

# loan.cancel_pending_app()
# 创建普通的personal loan
loan.access_application_interview()
loan.generate_new_ssn()
loan.search_new_ssn()
loan.create_new_application()
loan.checkout_application()
loan.enter_identification_info()
loan.payment_schedule()
loan.setup_account()