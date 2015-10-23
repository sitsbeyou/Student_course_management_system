# -*- coding:utf-8 -*-
__author__ = 'kong90'

from xuanke import Student, Course
from random import randint
from fire import write_course, update_course, read_course, make_str_list, make_course, read_student, \
                 make_str_list_of_student, make_student, update_student, write_student, check_course_time

num_of_student = []  # 生成2000个学号, 2012 - 2015
for i in range(4):
    for j in range(500):
        num_of_student.append('201' + str(i+2) + str(j))

time_of_course = ['1,2', '3,4', '5,6', '7,8', '9,10']  # 将一天的课化为5节大课, 可以自由组合, 通过索引获取
time_of_course_week = [str(i)+str(j) for i in time_of_course for j in range(5)]  # 生成一周的课
# 生成20门课
num_of_course = [str(i) for i in range(20)]


stnum = ''


def login():
    global stnum
    stnum = raw_input("请输入学号:")
    password = raw_input("请输入密码:")
    if password == '123456' and stnum in num_of_student:
        return True
    else:
        return False


# def choose_course(student, course):
#     str_all_course = ''
#     for i in course:
#         str_all_course = str_all_course + ' ' + i.num
#     course_num = raw_input("%s\n请输入相应课程序号:"%str_all_course)
#     if course_num in num_of_course:
#         # if check_course_time(student, course_num, course):
#         if student.AppendCourse(course_num):
#             if course[int(course_num)].judge_num():
#                 print "选课成功"
#                 print student.num, student.name, student.course, student.grade
#                 # print course[int(student.course[0])].name
#                 return course_num
#             else:
#                 print "该课人数已满"
#         else:
#             print "您已经选修过该门课"
#             return False
#         # else:
#             # return '选课时间冲突'
#     else:
#         print "没有该课"
#         return False

def choose_course(student, course):
    str_all_course = ''
    for i in course:
        str_all_course = str_all_course + ' ' + i.num
    course_num = raw_input("%s\n请输入相应课程序号:"%str_all_course)
    if course_num in num_of_course:
        if check_course_time(student, course_num, course):
            if student.AppendCourse(course_num):
                if course[int(course_num)].judge_num():
                    print "选课成功"
                    print student.num, student.name, student.course, student.grade
                    # print course[int(student.course[0])].name
                    return course_num
                else:
                    print "该课人数已满"
            else:
                print "您已经选修过该门课"
                return False
        else:
            print '选课时间冲突'
            return False
    else:
        print "没有该课"
        return False

def delete_course(student, course):
    str_all_course = ''
    for i in student.course:
        str_all_course = str_all_course + ' ' + str(i)
    course_num = raw_input("%s\n请输入您想退的课程序号:"%str_all_course)

    if course_num in num_of_course:
        if student.DeleteCourse(course_num):
            print "退课成功"
            print student.num, student.name, student.course
            return course_num
        else:
            print "您未选过该门课"
            return False
    else:
        print "没有这门课"
        return False


def main():
    c = raw_input("0:退出\n1:选课\n2:退课\n3:查询已选课程\n4:根据课程名查看选课学生等")
    course = make_str_list()
    # print course
    course = make_course(course)
    students = make_student(make_str_list_of_student(read_student('student')))
    if c == '1':
        x = choose_course(student1, course)
        if x:
            x = str(int(x) - 1)
            update_course(course, student1, x, c)  # 更新课程的文件
            update_student(course[int(x)], students, student_weizhi, c)
        main()
    elif c == '2':
        x = delete_course(student1, course)
        if x:
            x = str(int(x) - 1)
            update_course(course, student1, x, c)
            update_student(course[int(x)], students, student_weizhi, c)
        main()
    elif c == '3':
        print "您已经选了如下课程:"
        for i in student1.course:
            print '课'+str(i)
        main()
    elif c == '4':
        course_name = raw_input("请输入课程名: 如'课1'")
        print course_name
        for i in course:
            # print i.name
            if i.name == course_name:
                course1 = i
                # print i
        print '人数上限:' + course1.num_of_class
        print '现在已选人数:' + course1.now_num_of_student
        print '学生:' + str(course1.student_list)
        print '教室:' + course1.classroom
        print '上课时间:' + str(course1.time)
        print '上课时间:' + time(str(course1.time))
        # print '老师:' + course1.teachername
        main()
    elif c == '0':
        pass

def time(str_of_time):
    return "星期"+str_of_time[1]+' '+str_of_time[0]+str(int(str_of_time[0])+1)+"节课"\
           "星期"+str_of_time[3]+' '+str_of_time[2]+str(int(str_of_time[2])+1)+"节课"

if __name__ == '__main__':
    while not login():
        if login():
            break
    students = make_student(make_str_list_of_student(read_student('student')))  # 读出格式合理的student, 这里生成了全部的学生
    student_weizhi = 0                                                                            # 其实没必要. 但为了方便
    for i in students:
        if i.num == stnum:
            student1 = i
            break
        student_weizhi += 1
    # print student_weizhi
    main()
    # print student1.name
    # student1 = Student(stnum, '孔令星', '1', '火星科技与技术', [])






