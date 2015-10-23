# -*- coding:utf-8 -*-
__author__ = 'kong90'
from random import randint

num_of_student = []  # 生成2000个学号, 2012 - 2015
for i in range(4):
    for j in range(500):
        num_of_student.append('201' + str(i+2) + str(j))

# 生成2000个名字
names = ['孔' + str(i) for i in range(2000)]


fp = open('student', 'w')
for i in range(2000):
    # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
    fp.write(num_of_student[i] + ' ' + names[i] + ' ' + str(randint(0, 1)) + ' ' + str(6 - int(num_of_student[i][3])) + ' ' + '[]'
             + ' ' + '火星科学与技术' + '\n')
fp.close()




