# -*- coding:utf-8 -*-
from random import randint
"""
class 文件 用于存储课程，学生的类
"""

major_in = ['z_' + str(i + 1) for i in range(24)]   # 不会改变的专业list, 24个专业, 动态生成不考虑效率



class Student(object):
    """
    学生基本信息, 包含学号, 姓名, 性别, 年纪, 专业,  注意:::我们简单实现一个选课系统, 不需要考虑学分是否会合理
    学生选课信息, 包含课程编号, 存储在 list 里
    其中学号为 唯一 标识
    """

    def __init__(self, num, name, agent, course, major):
        self.num = num
        self.name = name
        self.agent = agent    # 1 代表男 , 2 代表女
        # self.grade = grade
        self.grade = 6 - int(self.num[3])    # 取学号字符串的第四位数
        self.course = course  # list
        self.major = major


    def AppendCourse(self, ACourse):
        """
        为学生添加课程, 带判断学生是否选修过某门课
        :param ACourse:
        :return:
        """
        if int(ACourse) not in self.course:
            self.course.append(int(ACourse))
            return True
        else:
            return False  # 返回False 用于判断学生是否选修了这门课

    def DeleteCourse(self, ACourse):
        if int(ACourse) in self.course:
            self.course.remove(int(ACourse))
            return True
        else:
            return False


class Course(object):
    """
    课程基本信息,课程号y, 课程名, 教师, 类型, 时间y, 地点y, 限选年级y, 学分, 容量y
    唯一标识 课程号y
    """

    def __init__(self, num, name, teachername, type, time, classroom, gradelist, \
                 xuefen, num_of_class, student_list, now_num_of_student ):
        self.num = num
        self.name = name
        self.teachername = teachername
        self.type = type
        self.time = time
        self.classroom = classroom
        self.gradelist = gradelist  # list
        self.xuefen = xuefen
        self.num_of_class = num_of_class
        self.student_list = student_list  # 用于存储学生学号
        self.now_num_of_student = now_num_of_student  # 用于记录当前选课人数, 及与num_of_class 比较


    def AppendGrade(self, grade):
        """
        为课程添加限选年级, 2, 3, 4, 5 , 对应 1, 2, 3, 4 现在让它随机生成   TODO
        :param grade:
        :return:
        """
        for i in range(randint(0, 4)):
            j = randint(0, 4)
            if j not in self.gradelist:
                self.gradelist.append(j)
        return True

    def AppendStudent(self, student_num):
        """
        为课程添加学生, 包括学生学号, 且 课程已选人数 + 1 即 self.now_num_of_student + 1
        :param student_num: 传入学号就可以了
        :return:
        """
        if student_num not in self.student_list:
            self.student_list.append(student_num)
            return True
        else:
            return False

    def AppendTime(self, time):
        """
        为课程添加开课, 上课的时间
        """
        if time not in self.time:
            self.time.append(time)
            return True
        else:
            return False

    def AppendClassroom(self, classroom):
        """
        为课程添加教室
        """
        if classroom not in self.classroom:
            self.classroom.append(classroom)
            return True
        else:
            return False

    def judge_num(self):
        if self.now_num_of_student < self.num_of_class:
            return True
        else:
            return False

