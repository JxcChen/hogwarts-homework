# -*- coding:utf-8 -*-
# @Time     :2022/12/25 6:49 下午
# @Author   :CHNJX
# @File     :student.py
# @Desc     :学员实体类

class Student:

    def __init__(self, num: int, name: str, sex: str):
        self.__num = num
        self.__name = name
        self.__sex = sex

    def __str__(self):
        return f"学生编号：{self.__num} 学成姓名：{self.__name} 学生性别：{self.__sex}"
