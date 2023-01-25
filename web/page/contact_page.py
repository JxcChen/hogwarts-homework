import time

from selenium.webdriver.common.by import By

from web.page.base_page import BasePage

# 通讯录主页面
add_member_btn = (By.LINK_TEXT, '添加成员')
search_input = (By.CSS_SELECTOR, '#memberSearchInput')
# 右上角+号
add_btn = (By.XPATH, '//*[contains(@class,"member_colLeft_top_addBtnWrap")]')
add_department_btn = (By.LINK_TEXT, '添加部门')

# 添加部门
department_name_input = (By.NAME, 'name')
parent_department_select = (By.LINK_TEXT, '选择所属部门')
add_department_confirm_btn = (By.LINK_TEXT, '确定')

# 新增成员页面
username_input = (By.ID, 'username')
english_name_input = (By.CSS_SELECTOR, '#memberAdd_english_name')
account_input = (By.CSS_SELECTOR, '#memberAdd_acctid')
email_input = (By.CSS_SELECTOR, '#memberAdd_biz_mail')
phone_input = (By.CSS_SELECTOR, '#memberAdd_phone')
department_select = (By.LINK_TEXT, '修改')
department_search_input = (By.XPATH, '//*[@placeholder="搜索部门"]')
confirm_btn = (By.LINK_TEXT, '确认')
save_btn = (By.LINK_TEXT, '保存')

# 搜索后右侧详情页面
member_name_detail = (By.CSS_SELECTOR, '.member_display_cover_detail_name')
department_name_detail = (By.CSS_SELECTOR, '#party_name')


class ContactPage(BasePage):

    # 新增成员
    def add_member(self, name, english_name, account, email, phone, department):
        return self.find_and_click(add_member_btn) \
            .find_and_send(name, username_input) \
            .find_and_send(english_name, english_name_input) \
            .find_and_send(account, account_input) \
            .find_and_send(email, email_input) \
            .find_and_send(phone, phone_input) \
            .find_and_click(department_select) \
            .find_and_send(department, department_search_input) \
            .find_and_click(By.XPATH, f'//*[contains(text(),{department})]') \
            .find_and_click(confirm_btn) \
            .find_and_click(save_btn) \
            .sleep(2)

    # 搜索
    def search_member_or_department(self, key):
        return self.find_and_send(key, search_input).sleep(1)

    # 获取搜索后的详情页成员名称
    def get_member_search_detail(self):
        text = self.find_element(member_name_detail).get_element_text()
        return text

    # 获取搜索后的详情部门名称
    def get_department_search_detail(self):
        text = self.find_element(department_name_detail).get_element_text()
        return text

    # 新增部门
    def add_department(self, department_name, parent_department):
        parent_department_btn = (By.XPATH, f'//label[text()="所属部门"]//parent::div//a[text()="{parent_department}"]')
        return self.find_and_click(add_btn) \
            .find_and_click(add_department_btn) \
            .find_and_send(department_name, department_name_input) \
            .find_and_click(parent_department_select) \
            .scroll_to_target_element(parent_department_btn) \
            .find_and_click(parent_department_btn) \
            .find_and_click(add_department_confirm_btn).sleep(2)

