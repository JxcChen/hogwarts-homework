import os

import pytest
import yaml

from utils.logger_utils import LoggerUtils
from calculator.calculator import Calculator


class TestCalculator:
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_data')
    logger = LoggerUtils.get_logger('testcase', 'calculator/calculator_log')
    calculator = Calculator()
    """
        def add(self, a, b):

        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a + b

    def div(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a / b
    """

    @pytest.mark.parametrize('add_data',
                             yaml.safe_load(open(os.path.join(DATA_DIR, 'test_add_data.yaml'), encoding='utf - 8')))
    @pytest.mark.add
    def test_add(self, add_data: dict):
        self.logger.info(add_data['desc'])
        res = self.calculator.add(add_data['a'], add_data['b'])
        assert res == add_data['expect']

    @pytest.mark.parametrize('div_data',
                             yaml.safe_load(open(os.path.join(DATA_DIR, 'test_div_data.yaml'), encoding='utf - 8')))
    @pytest.mark.div
    def test_div(self, div_data):
        self.logger.info(div_data['desc'])
        try:
            res = self.calculator.div(div_data['a'], div_data['b'])
            assert res == div_data['expect']
        except Exception as e:
            assert type(e) is ZeroDivisionError
