from utils.logger_utils import LoggerUtils


class TestBase:
    logger = LoggerUtils.get_logger('testcase', 'web/web_log')
