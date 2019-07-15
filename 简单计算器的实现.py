#定义函数：加减乘除
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
#
# print('选择运算：1,相加；2，相减；3，相乘；4，相除 ')
# choice = input('请输入你的选择(1/2/3/4)')
# num1 = int(input('请输入第一个数字： '))
# num2 = int(input('请输入第二个数字： '))
#
# if choice == '1':
#     print(num1,'+',num2,'=',add(num1,num2))
# elif choice == '2':
#     print(num1,'-','num2',subtract(num1,num2))
# elif choice == '3':
#     print(num1,'*',num2,'=',multiply(num1,num2))
# elif choice == '4':
#     print(num1,'/',num2,'=',divide(num1,num2))
# else:
#     print('非法输入')

class Calculator(object):
    def __init__(self,x,op,y):
        self.x = float(x)
        self.y = float(y)
        self.op = op
    def oper(self):
        if self.op == '+':
            return add(self.x,self.y)
        elif self.op == '-':
            return subtract(self.x,self.y)
        elif self.op == '*':
            return multiply(self.x,self.y)
        elif self.op == '/':
            return divide(self.x,self.y)
        else:
            return '运算符出错'
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return '分母不能为0, 计算无效'
    else:
        return x/y

import re
exp = input('请输入计算式： ')
expression = re.search(r'(\d+)(.*?)(\d+)',exp,re.M)
if exp:
    a = expression.group(1)
    operator = expression.group(2)
    b = expression.group(3)
    #print('运算结果为：{}'.format(Calculator(a,operator,b).oper()))
    print('运算结果为：%s' % Calculator(a, operator, b).oper())#这里当y为0的时候，会返回'分母不能为0, 计算无效'，这里采用%f，不对，如果改为%s，就可以啦
# print(Calculator(2,'/',0).oper())



