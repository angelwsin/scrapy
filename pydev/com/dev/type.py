#Python3 基本数据类型

#Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
#等号（=）用来给变量赋值。
#等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值

#多个变量赋值
a= b =c = 1

#标准数据类型
#Python3 中有六个标准的数据类型：
#Number（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Sets（集合）
#Dictionary（字典）


#Number（数字）
'''
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long
内置的 type() 函数可以用来查询变量所指的对象类型。
'''
a = 1
print(type(a))

class A:
    pass
class B(A):
    pass
#此外还可以用 isinstance 来判断
print(type(A())==A)
print(type(B())==A)
print(isinstance(B(), A))



#注释
#1、单引号（'''）
#2、双引号（"""）

x = set()
