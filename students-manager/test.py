# -*- coding:utf-8 -*-
# @Time     :2022/12/25 6:55 下午
# @Author   :CHNJX
# @File     :test.py
# @Desc     :
from student import Student
from manager import Manager


class TestStudent:
    manager = Manager()

    def test_add_student(self):
        res = self.manager.add_student(3, 'jjj', '男')
        assert '新增成功' == res

    def test_delete_student(self):
        res = self.manager.delete_student(3)
        assert '删除成功' == res


