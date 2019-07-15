#如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
num = int(input("请输入一个正整数： "))
#num = int(input(""))
sum = 0
n = len(str(num))#先将其转换成字符串
temp = num
while temp > 0:
    digital = temp % 10
    sum += digital ** n
    temp //= 10
if sum == num:
    print('您输入的是一个阿姆斯特朗数')
else:
    print("您输入的不是一个阿姆斯特朗数")
