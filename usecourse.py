# -*- coding:utf-8 -*-
__author__ = 'kong90'

# fp = open('course', 'r')
# # for i in range(2000):
#     # fp.write('201211  孔令星  1         4         火星科学与技术  [1,2,6,9]\n')
#     # fp.write(num_of_student[i] + ' ' +names[i] + ' ' + str(6 - int(num_of_student[i][3])) + ' ' + '火星科学与技术' + '[]' + '\n')
# x = [line for line in fp.readlines()]
# print x[0]
# fp.close()

def read_course(course):
    fp = open(course, 'r')
    x = [line for line in fp.readlines()]
    y = [i.split(' ') for i in x]
    fp.close()
    return y

def make_str_list(y):
    for j in y:
        if len(j[3]) == 2:
            j[3] = []
        else:
            j[3] = j[3][1:-1].split(',')
        if len(j[4]) == 2:
            j[4] = []
        else:
            j[4] = j[4][1:-1].split(',')
        if len(j[5]) == 2:
            j[5] = []
        else:
            j[5] = j[5][1:-1].split(',')
        if len(j[9]) == 2:
            j[9] = []
        else:
            j[9] = j[9][1:-1].split(',')
        if len(j[-1][:-1]) == 2:
            j[-1] = []
        else:
            j[-1] = j[-1][1:-2].split(',')
    return y
if __name__ == '__main__':
    # print read_course('course')
    print make_str_list(read_course('course'))
