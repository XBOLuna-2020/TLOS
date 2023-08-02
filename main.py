
import common_method

# 单击credit application -> create application
common_method.access_application_interview()

# 生成新的SSN，并保存成global变量
common_method.generate_new_ssn()

# 在搜索框中输入ssn,查看是否已存在
common_method.search_new_ssn()

# 创建新的application，依次输入数据
common_method.create_new_application()

# app 创建成功后，进入checkout页面
common_method.checkout_application()

# check out application 后，进入 enter/edit 页面
common_method.enter_identification_info()


