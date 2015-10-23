# -*- coding:utf-8 -*-
from random import randint
from xuanke import Student, Course

num_of_student = []  # 生成2000个学号, 2012 - 2015
for i in range(4):
    for j in range(500):
        num_of_student.append('201' + str(i+2) + str(j))

time_of_course = ['1,2', '3,4', '5,6', '7,8', '9,10']  # 将一天的课化为5节大课, 可以自由组合, 通过索引获取
time_of_course_week = [str(i)+str(j) for i in time_of_course for j in range(5)]  # 生成一周的课
# 生成20门课
num_of_course = [str(i + 1) for i in range(20)]

# 生成10间教室
num_of_classroom = [str(i) for i in range(10)]

# 生成20门课的具体信息, 假设老师足够, 教室和课程时间不能同时一样


def write_course(course, list_of_course):
    fp = open(course, 'w')
    # print list_of_course
    # print len(list_of_course)
    for i in list_of_course:
        """
        先去掉列表里的空格
        """
        i.student_list = [int(j) for j in i.student_list]
        i.student_list = str(i.student_list).split(' ')
        student_list_b = ''
        for j in i.student_list:
            student_list_b += j
        i.student_list = student_list_b
        fp.write(i.num + ' ' + i.name + ' ' + '孔老师' + ' ' + '通识课' + ' '
                 + str(i.time) + ' ' + i.classroom + ' '
           + str(i.gradelist) + ' ' + '4' + ' ' + i.num_of_class + ' ' + i.student_list + ' '
         + i.now_num_of_student )
    fp.close()


def update_course(course, student, num_of_course, judge): # 用于判断是选课还是删课
    # print num_of_course
    # print course
    if judge == '1':
        if int(course[int(num_of_course)].now_num_of_student) < int(course[int(num_of_course)].num_of_class):
            # print course[int(num_of_course)].student_list
            course[int(num_of_course)].student_list.append(int(student.num))
            # print course[int(num_of_course)].student_list
            x = int(course[int(num_of_course)].now_num_of_student)
            x += 1
            course[int(num_of_course)].now_num_of_student = str(x) + '\n'
            # print 12
            write_course('course', course)
    if judge == '2':
        if int(course[int(num_of_course)].now_num_of_student) < int(course[int(num_of_course)].num_of_class):
            # print course[int(num_of_course)].student_list
            course[int(num_of_course)].student_list.remove(int(student.num))
            # print course[int(num_of_course)].student_list
            x = int(course[int(num_of_course)].now_num_of_student)
            x -= 1
            course[int(num_of_course)].now_num_of_student = str(x) + '\n'
            # print 12
            write_course('course', course)

def read_course(course):
    fp = open(course, 'r')
    x = [line for line in fp.readlines()]
    y = [i.split(' ') for i in x]
    fp.close()
    return y

def make_str_list():
    y = read_course('course')
    # print y
    for j in y:
        # print j
        # if len(j[6]) == 2:
        #     j[6] = []
        # else:
        #     j[6] = j[6][1:-1].split(',')
        #     j[6] = [int(x) for x in j[6]]
        # if len(j[4]) == 2:
        #     j[4] = []
        # else:
        #     j[4] = j[4][1:-1].split(',')
        #     j[4] = [int(x) for x in j[4]]
        if len(j[-2]) == 2:
            j[-2] = []
        else:
            j[-2] = j[-2][1:-1].split(',')
            j[-2] = [int(x) for x in j[-2]]
    return y

def make_course(course):
    list_of_n = []
    for i in course:
        # n = Course(i, '第一门课', '孔老师', '专业选修课', time_of_course_week[randint(0,24)],
        #            num_of_classroom[randint(0, 9)], [1, 2], 5, 50, 20, [1, 2])
        n = Course(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
        # n = Course(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], 12, i[9], 0)
        list_of_n.append(n)
    # print list_of_n[0]
    return list_of_n


def read_student(student):
    fp = open(student, 'r')
    x = [line for line in fp.readlines()]
    y = [i.split(' ') for i in x]
    fp.close()
    return y


def make_str_list_of_student(y):
    for j in y:
        if len(j[-2]) == 2:
            j[-2] = []
        else:
            j[-2] = j[-2][1:-1].split(',')
            j[-2] = [int(x) for x in j[-2]]
    return y


def make_student(student):
    list_of_n = []
    for i in student:
        # print type(i[4])
        # n = Course(i, '第一门课', '孔老师', '专业选修课', time_of_course_week[randint(0,24)],
        #            num_of_classroom[randint(0, 9)], [1, 2], 5, 50, 20, [1, 2])
        n = Student(i[0], i[1], i[2], i[4], i[5])
        list_of_n.append(n)
    # print list_of_n[0].name
    return list_of_n


def write_student(student, list_of_student):
    fp = open(student, 'w')
    # print list_of_course
    # print len(list_of_course)
    for i in list_of_student:
        """
        先去掉列表里的空格
        """
        i.course = [int(j) for j in i.course]
        i.course = str(i.course).split(' ')
        course_b = ''
        for j in i.course:
            course_b += j
        i.course = course_b
        fp.write(i.num + ' ' + i.name + ' ' + i.agent + ' ' + str(i.grade) + ' '
                 + i.course + ' ' + '火星科学与技术\n' )
    fp.close()


def update_student(course, student, num_of_student, judge): # 用于判断是选课还是删课
    # print num_of_course
    # print course
    if judge == '1':
        student[int(num_of_student)].course.append(int(course.num))
        # print student[int(num_of_student)].course
        write_student('student', student)
    if judge == '2':
        student[int(num_of_student)].course.remove(int(course.num))
        write_student('student', student)
    # if judge == '2':
    #     if int(course[int(num_of_course)].now_num_of_student) < int(course[int(num_of_course)].num_of_class):
    #         # print course[int(num_of_course)].student_list
    #         course[int(num_of_course)].student_list.remove(int(student.num))
    #         # print course[int(num_of_course)].student_list
    #         x = int(course[int(num_of_course)].now_num_of_student)
    #         x -= 1
    #         course[int(num_of_course)].now_num_of_student = str(x) + '\n'
    #         print 12
    #         write_course('course', course)


def check_course_time(student, course_num, course):  # student 为1个, course 是全部的课对象
    student_course = student.course    # 学生已选课的num的list
    # course_all = [i.num for i in course]  # 全部的课num的list
    # in_two = [j for j in course_all if j in student_course]
    # print student_course
    # for s in course:
    #     if s.num in student_course:pass
    course_duixiang = [j for j in course if int(j.num) in student_course]
    time_of_course_duixiang = [i.time for i in course_duixiang]
    # print 't', course_duixiang
    k_course = ''
    for k in course:
        if k.num == course_num:
            k_course = k
    # print k_course.time
    # print [l[0:2] for l in time_of_course_duixiang]
    if k_course.time[0:2] in [l[0:2] for l in time_of_course_duixiang] or \
        k_course.time[2:] in [z[0:2] for z in time_of_course_duixiang]:
        return False
    else:
        return True

