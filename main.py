from common_method import ApplyProcess

# 将字符串'data/data_application_interview.json'（文件的路径） 赋值给变量json_input_fields_application_interview
json_input_fields_application_interview = 'data/data_application_interview.json'
loan = ApplyProcess(json_input_fields_application_interview)
print(f"The JSON file path is: {json_input_fields_application_interview}")

# loan.cancel_pending_app()
# 创建普通的personal loan
loan.access_application_interview()
loan.generate_new_ssn()
loan.search_new_ssn()
loan.create_new_application()
# loan.checkout_application()
# loan.enter_identification_info()
# loan.payment_schedule()
# loan.setup_account()