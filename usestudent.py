# -*- coding:utf-8 -*-
__author__ = 'kong90'

# fp = open('student', 'r')
# # for i in range(2000):
#     # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
#     # fp.write(num_of_student[i] + ' ' +names[i] + ' ' + str(6 - int(num_of_
#            student[i][3])) + ' ' + '火星科学与技术' + '[]' + '\n')
# x = [line for line in fp.readlines()]
# print x[0]
# fp.close()

def read_student(student):
    fp = open(student, 'r')
    x = [line for line in fp.readlines()]
    y = [i.split(' ') for i in x]
    fp.close()
    return y


def make_str_list_of_student(y):
    for j in y:
        if len(j[-1][:-1]) == 2:
            j[-1] = []
        else:
            j[-1] = j[-1][1:-2].split(',')
    return y
if __name__ == '__main__':
    # print read_course('course')
    print make_str_list_of_student(read_student('student'))

