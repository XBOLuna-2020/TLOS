#
# import common_method_original
#
# # 单击credit application -> create application
# common_method_original.access_application_interview()
#
# # 生成新的SSN，并保存成global变量
# common_method_original.generate_new_ssn()
#
# # 在搜索框中输入ssn,查看是否已存在
# common_method_original.search_new_ssn()
#
# # 创建新的application，依次输入数据
# common_method_original.create_new_application()
#
# # app 创建成功后，进入checkout页面
# common_method_original.checkout_application()
#
# # check out application 后，进入 enter/edit 页面
# common_method_original.enter_identification_info()
#
# # Payment Inquiry 页面输入
# common_method_original.payment_schedule()


from common_method import LoanSystemTester

tester = LoanSystemTester()

try:
    tester.access_application_interview()
    tester.generate_new_ssn()
    tester.search_new_ssn()
    tester.create_new_application()
    tester.checkout_application()
    tester.enter_identification_info()
    tester.payment_schedule()
except Exception as e:
    print(f"An error occurred: {str(e)}")
# finally:
#     tester.close_driver()
