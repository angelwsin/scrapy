#编码
#以 UTF-8 编码，所有字符串都是 unicode 字符串


#标识符
#第一个字符必须是字母表中字母或下划线'_'。
#标识符的其他的部分有字母、数字和下划线组成。
#标识符对大小写敏感。

#python保留字
import keyword

for key in keyword.kwlist:print(key)


#行与缩进
#python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
#缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数

if True:
    print("true")
else:
    print("false")
    

#多行语句
#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item_one  = "item_one"
item_two  = "item_two"
item_three = "item_three"
total = item_one + \
        item_two + \
        item_three

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']


#数据类型
#python中数有四种类型：整数、长整数、浮点数和复数。
#整数， 如 1
#长整数 是比较大的整数
#浮点数 如 1.23、3E-2
#复数 如 1 + 2j、 1.1 + 2.2j



#字符串
#python中单引号和双引号使用完全相同。
#使用三引号('''或""")可以指定一个多行字符串。
#转义符 '\'
#自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
#python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
#字符串是不可变的。
#按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。

#空行
#函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
#空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
#记住：空行也是程序代码的一部分。

#同一行显示多条语句
#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例

  

#import 与 from...import
#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *









