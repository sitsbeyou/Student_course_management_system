# -*- coding:utf-8 -*-
# __author__ = 'kong90'
# from random import randint
#
# time_of_course = ['1,2', '3,4', '5,6', '7,8', '9,10']  # 将一天的课化为5节大课, 可以自由组合, 通过索引获取
# time_of_course_week = [str(i)+str(j) for i in time_of_course for j in range(5)]  # 生成一周的课
# # 生成20门课
# num_of_course = [str(i + 1) for i in range(20)]
# num_of_class = [30, 60, 100, 140, 170]  # 几种典型的上课人数, 规定了某课可以选课人数的上限
# names = ['课' + str(i) for i in range(20)]  # 二十门课的名字
#
# num_of_classroom = [str(i) for i in range(10)]
# # 1    '知味' '孔老师'  '通识课'  教室 [1,2,4]     4    100    [201211, 201212]  12
#
# fp = open('course', 'w')
# for i in range(20):
#     # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
#     fp.write(num_of_course[i] + ' ' + names[i] + ' ' + '老师' + ' ' + '通识课' + ' ' + '[]' + ' ' +
#              str(num_of_classroom[randint(0,4)]) + ' '
#            + '[]' + ' ' + '4' + ' ' + str(num_of_class[randint(0, 4)]) + ' ' + '[]'
#              + ' ' + '0' + '\n')
# fp.close()



# """
# 正式的排课系统, 规定上课时间, 教室, 老师假定足够且名字相同
# """
#
# __author__ = 'kong90'
# from random import randint
#
# time_of_course = ['1', '3', '5', '7', '9']  # 将一天的课化为5节大课, 可以自由组合, 通过索引获取
# time_of_course_week = [str(i)+str(j+1) for i in time_of_course for j in range(5)]  # 生成一周的课9514代表星期5第⑤节大课时间和星期4的第一节大课
# # 生成20门课
# num_of_course = [str(i + 1) for i in range(20)]
# print num_of_course
# num_of_class = [30, 60, 100, 140, 170]  # 几种典型的上课人数, 规定了某课可以选课人数的上限
# names = ['课' + str(i) for i in range(20)]  # 二十门课的名字
#
# # num_of_classroom = [str(i) for i in range(10)]
# # 1    '知味' '孔老师'  '通识课'  教室 [1,2,4]     4    100    [201211, 201212]  12
#
# # 先给20门课10个教室
# num_of_classroom = [str(randint(1, 10)) for i in range(20)]
#
# # 生成限选年级的list
# list_of_grade = ['12', '34']  # 12代表限选年级为1,2年级
#
# x = []  # 用于记录之前的安排的课, 以便比较有没有时间教室冲突的课
# def self_check(lists, news):
#     """
#     用于检查排课的时间教室安排
#     """
#     if news[1] in [i[1] for i in lists]:
#         if news[0][0:2] in [i[0][0:2] for i in lists] or news[2:] in [i[1][2:] for i in lists]:
#             return False
#         else:
#             return True
#     else:
#         return True
#
#
# fp = open('course', 'w')
# for i in range(20):
#     # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
#     time = [time_of_course_week[randint(0, 24)] for j in range(2)]
#     time = time[0]+time[1]
#     classroom = num_of_classroom[i]
#     z = (time, classroom)
#     # print num_of_course[i]
#     # print i
#     # if self_check(x, z):
#     x.append(z)
#
#         # print x
#     fp.write(num_of_course[i] + ' ' + names[i] + ' ' + '孔老师' + ' ' + '通识课' + ' ' + str(time) + ' ' +
#                  num_of_classroom[i] + ' '
#              + list_of_grade[randint(0, 1)] + ' ' + '4' + ' ' + str(num_of_class[randint(0, 4)]) + ' ' + '[]'
#                  + ' ' + '0' + '\n')
#     # else:
#         # print 'Wrong'
# fp.close()


# """
# 正式的排课系统, 规定上课时间, 教室, 老师假定足够且名字相同
# """
#
# __author__ = 'kong90'
# from random import randint
#
# time_of_course = ['1', '3', '5', '7', '9']  # 将一天的课化为5节大课, 可以自由组合, 通过索引获取
# time_of_course_week = [str(i)+str(j+1) for i in time_of_course for j in range(5)]  # 生成一周的课9514代表星期5第⑤节大课时间和星期4的第一节大课
# # 生成20门课
# num_of_course = [str(i + 1) for i in range(20)]
# # print num_of_course
# num_of_class = [30, 60, 100, 140, 170]  # 几种典型的上课人数, 规定了某课可以选课人数的上限
# names = ['课' + str(i) for i in range(20)]  # 二十门课的名字
#
# # num_of_classroom = [str(i) for i in range(10)]
# # 1    '知味' '孔老师'  '通识课'  教室 [1,2,4]     4    100    [201211, 201212]  12
#
# # 先给20门课10个教室
# num_of_classroom = [str(randint(1, 10)) for i in range(20)]
#
# # 生成限选年级的list
# list_of_grade = ['12', '34']  # 12代表限选年级为1,2年级
#
# x = []  # 用于记录之前的安排的课, 以便比较有没有时间教室冲突的课
# def self_check(lists, news):
#     """
#     用于检查排课的时间教室安排
#     """
#     if news[1] in [i[1] for i in lists]:
#         o = []
#         for j in lists:
#             if news[1] == j[1]:
#                 o.append(j)
#         if (news[0][0:2] in [i[0][0:2] for i in o]) or (news[2:] in [i[1][2:] for i in o]):
#             return False
#         else:
#             return True
#     else:
#         return True
#
#
# fp = open('course', 'w')
# for i in range(20):
#     # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
#     time = [time_of_course_week[randint(0, 24)] for j in range(2)]
#     time = time[0]+time[1]
#     classroom = num_of_classroom[i]
#     z = (time, classroom)
#     # print num_of_course[i]
#     # print i
#     if self_check(x, z):
#
#         x.append(z)
#
#         # print x
#         fp.write(num_of_course[i] + ' ' + names[i] + ' ' + '孔老师' + ' ' + '通识课' + ' ' + str(time) + ' ' +
#                  num_of_classroom[i] + ' '
#              + list_of_grade[randint(0, 1)] + ' ' + '4' + ' ' + str(num_of_class[randint(0, 4)]) + ' ' + '[]'
#                  + ' ' + '0' + '\n')
#     else:
#         print 'Wrong'
#         print '重新生成中...'
# fp.close()

"""
正式的排课系统, 规定上课时间, 教室, 老师假定足够且名字相同
"""

__author__ = 'kong90'
from random import randint

time_of_course = ['1', '3', '5', '7', '9']  # 将一天的课化为5节大课, 可以自由组合, 通过索引获取
time_of_course_week = [str(i)+str(j+1) for i in time_of_course for j in range(5)]  # 生成一周的课9514代表星期5第⑤节大课时间和星期4的第一节大课
# 生成20门课
num_of_course = [str(i + 1) for i in range(20)]
# print num_of_course
num_of_class = [30, 60, 100, 140, 170]  # 几种典型的上课人数, 规定了某课可以选课人数的上限
names = ['课' + str(i) for i in range(20)]  # 二十门课的名字

# num_of_classroom = [str(i) for i in range(10)]
# 1    '知味' '孔老师'  '通识课'  教室 [1,2,4]     4    100    [201211, 201212]  12

# 先给20门课10个教室
num_of_classroom = [str(randint(1, 10)) for i in range(20)]

# 生成限选年级的list
list_of_grade = ['12', '34']  # 12代表限选年级为1,2年级

# x = []  # 用于记录之前的安排的课, 以便比较有没有时间教室冲突的课
def self_check(lists, news):
    """
    用于检查排课的时间教室安排
    """
    if news[1] in [i[1] for i in lists]:
        o = []
        for j in lists:
            if news[1] == j[1]:
                o.append(j)
        if (news[0][0:2] in [i[0][0:2] for i in o]) or (news[2:] in [i[1][2:] for i in o]):
            return False
        else:
            return True
    else:
        return True


def build_course():
    """
    重新生成还有点问题
    """
    x = []  # 用于记录之前的安排的课, 以便比较有没有时间教室冲突的课
    fp = open('course', 'w')
    for i in range(20):
        # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
        time = [time_of_course_week[randint(0, 24)] for j in range(2)]
        time = time[0]+time[1]
        classroom = num_of_classroom[i]
        z = (time, classroom)
        # print num_of_course[i]
        # print i
        if self_check(x, z):

            x.append(z)

            # print x
            fp.write(num_of_course[i] + ' ' + names[i] + ' ' + '孔老师' + ' ' + '通识课' + ' ' + str(time) + ' ' +
                     num_of_classroom[i] + ' '
                 + list_of_grade[randint(0, 1)] + ' ' + '4' + ' ' + str(num_of_class[randint(0, 4)]) + ' ' + '[]'
                     + ' ' + '0' + '\n')
        else:
            print 'Wrong'
            print '重新生成中...'
            build_course()
            print 'OK'
    fp.close()

if __name__ == '__main__':
    build_course()