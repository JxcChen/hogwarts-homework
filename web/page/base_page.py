import datetime
import logging
import os
import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger_utils import LoggerUtils


class BasePage:
    _element: WebElement = None
    _elements: list[WebElement] = None
    current_time = 0
    caps = {}
    logger: logging = None

    def __init__(self, driver: WebDriver = None):
        self.logger = LoggerUtils.get_logger('page', 'web/web_log')
        if driver is None:
            self.init_web()
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    def init_web(self):
        from selenium import webdriver
        # web driver 初始化
        driver_type = os.getenv("browser")
        # 根据用户传入变量打开对应的浏览器
        if driver_type == "firefox":
            self.driver = webdriver.Firefox()
        elif driver_type == 'edge':
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # @handle_exception
    def find_element(self, by, locator: str = None):
        """
        查找元素
        :param by: 可以是元祖或者by对象
        :param locator: 定位符 默认为空  如果不传 by必须传元祖
        :return: 目标元素
        """
        self.logger.info(f'查找元素 by：{by},locator:{locator}')
        try:
            if locator is None:
                self._element = self.driver.find_element(*by)
            else:
                self._element = self.driver.find_element(by, locator)
        except Exception as e:
            self.logger.error('点击元素失败')
            self.logger.error(e.__str__())
            raise e
        return self

    def click(self):
        """
        点击元素  需要先查找
        """
        self.logger.info('点击元素')
        try:
            self._element.click()
        except Exception as e:
            self.logger.error('点击元素失败')
            self.logger.error(e.__str__())
            raise e
        return self

    def send(self, key):
        """
        点击元素  需要先查找
        """
        self.logger.info(f'输入 key： {key}')
        try:
            self._element.send_keys(key)
        except Exception as e:
            self.logger.error('点击元素失败')
            self.logger.error(e.__str__())
            raise e
        return self

    def find_and_click(self, by, locator: str = None):
        """
        点击元素
        return 当前页面
        """
        self.logger.info(f'查找并点击元素 by：{by} locator:{locator}')
        self.find_element(by, locator)
        return self.click()

    def find_and_send(self, key: str, by, locator: str = None):
        """
        点击元素
        return 当前页面
        """
        self.logger.info(f'查找并输入内容 by：{by} locator:{locator} key:{key}')
        self.find_element(by, locator)
        return self.send(key)

    # @handle_exception
    def find_elements(self, by, locator: str = None, index: int = None):
        """
        查找全部相关元素
        """
        self.logger.info(f'查找全部相关元素 by：{by} locator:{locator} 第{index}个')
        if index is None:
            if locator is None:
                self._elements = self.driver.find_elements(*by)
            else:
                self._elements = self.driver.find_elements(by, locator)
        else:
            if locator is None:
                self._element = self.driver.find_elements(*by)[index]
            else:
                self._element = self.driver.find_elements(by, locator)[index]
        return self

    def get_elements_text(self) -> list:
        """
        获取元素的文本属性列表
        """
        self.logger.info(f'获取元素的文本属性列表')
        if self._elements is not None:
            return [ele.text for ele in self._elements]
        else:
            return []

    def get_element_text(self) -> str:
        """
        获取元素的文本属性
        """
        self.logger.info(f'获取元素的文本属性: {self._element.text}')
        return self._element.text

    def get_element_attribute(self, attribute) -> str:
        """
        :param attribute: 属性名称
        获取元素的文本属性
        """
        self.logger.info(f'获取元素的{attribute}属性: {self._element.get_attribute(attribute)}')
        return self._element.get_attribute(attribute)

    def wait_for_click(self, locator, timeout=15):
        """
        等待元素可被点击
        :param locator: 定位符
        :param timeout: 超时时间 默认10秒
        :return: self
        """
        self.logger.info(f'等待元素可被点击 locator：{locator} timeout：{timeout}')
        self._element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        return self

    def wait_for_visible(self, locator, timeout=10):
        """
        等待元素可见
        :param locator: 定位符
        :param timeout: 超时时间 默认10秒
        :return: self
        """
        self.logger.info(f'等待元素可见 locator：{locator} timeout：{timeout}')
        self._element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        return self

    def save_screenshot(self, name: str = None, png_dir: str = None) -> str:
        """
        保存截图
        :param name:截图名称  默认为当前时间
        :param png_dir: 截图存放路径默认存在res/image下
        return 返回完整名称
        """
        if name is None:
            name = f"{datetime.datetime.now().strftime('%H.%M.%S')}"
        if png_dir is None:
            today = f"{datetime.datetime.now().strftime('%Y-%m-%d')}"
            png_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), f'image/{today}')
        if not os.path.exists(png_dir):
            os.makedirs(png_dir)
        png_path = png_dir + '/' + name + '.png'
        self.logger.info(f'进行截图 name：{name} png_dir：{png_dir}')
        self.driver.save_screenshot(png_path)
        # 将截图放到allure中
        with open(png_path, 'rb') as f:
            allure.attach(f.read(), attachment_type=allure.attachment_type.PNG)
        return png_path

    # ******************* web *************************
    def scroll_to_bottom(self):
        """
        滑动到页面底部
        """
        self.logger.info("滑动到页面底部")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_target_element(self, locator: tuple = None):
        """
        :param locator: 定位 若为空则需要先调用find_element
        滑动到元素位置
        """
        if locator:
            self.find_element(locator)
        self.logger.info(f'滑动到元素位置 locator：{locator}')
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true)", self._element)
        return self

    def sleep(self, sleep_time):
        self.logger.warning(f"进行强制等待，强制等待时间：{sleep_time}")
        time.sleep(sleep_time)
        return self
