from common_method import ApplyProcess

loan = ApplyProcess()
print('Which loan do you want to setup? (P or RE)')
loan_type = input()

# loan.cancel_pending_app()
loan.access_application_interview()
loan.generate_new_ssn()
loan.search_new_ssn()
loan.create_new_application()
if loan_type == 'P':
    try:
        loan.checkout_application()
        loan.enter_identification_info()
        loan.payment_schedule()
        loan.setup_account()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
elif loan_type == 'RE':
    try:
        loan.RE_checkout_loan()
        loan.RE_enter_identification_info()
        loan.RE_payment_schedule()
        loan.RE_print_closing_documents()
    except Exception as e:
        print('RE 还没跑完')
else:
     print('输入错误！请重新输入。')
loan.close_browser()

