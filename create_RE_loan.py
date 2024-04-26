from common_method import ApplyProcess

loan = ApplyProcess()

# 创建RE loan
# loan.cancel_pending_app()
loan.access_application_interview()
loan.generate_new_ssn()
loan.search_new_ssn()
loan.create_new_application()
loan.RE_checkout_loan()
loan.RE_enter_identification_info()
loan.RE_payment_schedule()
loan.RE_print_closing_documents()



