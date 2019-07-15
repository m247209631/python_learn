#质数的判断
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# 用户输入数字
num = int(input("请输入一个数字: "))
if is_prime(num):
    print(num,"是质数")
else:
    print(num,"不是质数")