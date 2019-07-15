#定义函数

# def lcm(x,y):
#     if x>y:
#         greater = x
#     else:
#         greater = y
#     for i in range(greater,x*y,1):
#         if i%x == 0 and i%y == 0:
#             return i

# 求两个数之间的最小公倍数相对简单，用两个数的乘积对两个之间的最大公约数求商即可
def lcm(x, y): # very fast
    s = x*y
    while y: x, y = y, x%y
    return s//x