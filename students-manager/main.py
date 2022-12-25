# -*- coding:utf-8 -*-
# @Time     :2022/12/25 11:04 下午
# @Author   :CHNJX
# @File     :main.py
# @Desc     :学生管理系统
from manager import Manager

manager = Manager()
while True:
    res = input("1.根据学号查看学员信息     2.添加学员     3.查看所有学员信息     4.删除学员信息     5.退出")
    if res == '1':
        try:
            stu_num = int(input('请输入学生编号'))
            print(manager.get_student(stu_num))
        except Exception:
            print('输入的学生编号格式有误')
    elif res == '2':
        stu_num = int(input('请输入学生编号'))
        stu_name = input('请输入学生姓名')
        stu_sex = input('请输入学生性别')
        print(manager.add_student(stu_num, stu_name, stu_sex))
    elif res == '3':
        student_list = manager.get_student_list()
        for student in student_list:
            print(student)
    elif res == '4':
        try:
            stu_num = int(input('请输入要删除的学生编号'))
            print(manager.delete_student(stu_num))
        except Exception:
            print('输入的学生编号格式有误')
    elif res == '5':
        break
    else:
        print('输入有误请重新输入')
