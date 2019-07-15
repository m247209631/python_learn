# 定义一个函数
# def hcf(x, y):
#     """该函数返回两个数的最大公约数"""
#
#     # 获取最小值
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1, smaller + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#
#     return hcf

# 可按以下思路减少循环次数：
# 1. 当最小值为最大公约数时，直接返回；
# 2. 当最小值不为最大公约数时，最大公约数不会大于最小值的1/2；
# 3. 求最大公约数理应从大到小循环递减求最大
# def gcd(x,y):
#     if x>y:
#         x,y=y,x
#     if y%x == 0:
#         return x
#     else:
#         for i in range(x,0,-1):
#             if y%i == 0 and x%i == 0:
#                 return i
#             # else:
#             #     return 0  #这样写存在错误，return语句应该是在循环进行完以后进行的，
#         return 0 #应该放在这里

# 两个数的最大公约数可以使用 欧几里得算法实现。即两个数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。
def f1(a,b):
    while b!=0:
        a,b=b,a%b
    return a
