# coding:utf-8
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# 用列表生成式，生成新的列表
b = [i for i in a if i > 0]
print("大于 0 的个数：%s" % len(b))
c = [i for i in a if i < 0]
print("小于 0 的个数：%s" % len(c))