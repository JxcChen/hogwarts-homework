from utils.logger_utils import LoggerUtils

logger = LoggerUtils.get_logger('testcase', 'web_log')


def fail_screenshot(func):
    def testcase(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            args[0].logger.error('进行错误截图')
            args[0].main.save_screenshot()
            raise e

    return testcase
