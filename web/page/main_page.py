import os
import time

import yaml
from selenium.webdriver.common.by import By

from web.page.base_page import BasePage
from web.page.contact_page import ContactPage

contact_btn = (By.ID, 'menu_contacts')


class MainPage(BasePage):
    cookies_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cookies.yaml')

    def __init__(self):
        super().__init__()
        self._into_main_page()

    def into_contact_page(self):
        self.find_and_click(contact_btn)
        return ContactPage(self.driver)

    def _into_main_page(self):
        # 判断本地当前是否存在cookies
        if not os.path.exists(self.cookies_file):
            self._save_cookies()
            self._into_main_page()
        else:
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
            cookies = yaml.safe_load(open(self.cookies_file, 'r'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

    def _save_cookies(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        time.sleep(10)
        cookies = self.driver.get_cookies()
        file = open(self.cookies_file, 'w')
        yaml.safe_dump(data=cookies, stream=file)
        file.close()
