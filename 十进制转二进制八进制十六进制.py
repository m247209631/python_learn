# 获取用户输入十进制数
# dec = int(input("输入数字："))
#
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))

#十进制转2进制
# def dec2bin(n):
#     l=[]
#     if n < 0:
#         return '-'+dec2bin(abs(n))
#     else:
#         while n>=0 :
#             n,b=divmod(n,2)#返回n除以2的商和余数
#             l.append(str(b))#由于join的对象必须是字符串序列,所以这里必须有str函数
#             if n == 0:
#                 return ''.join(l[::-1])

#十进制转8进制
# def dec2oct(n):
#     l=[]
#     if n < 0:
#         return '-'+dec2bin(abs(n))
#     else:
#         while n>=0 :
#             n,b=divmod(n,8)#divmod函数返回n除以2的商和余数
#             l.append(str(b))#由于join的对象必须是字符串序列,所以这里必须有str函数
#             if n == 0:
#                 return ''.join(l[::-1])

#十进制转十六进制
# base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
# def dec2hex(num):
#     l = []
#     if num < 0:
#         return '-' + dec2hex(abs(num))
#     while True:#这里与上面的有些不一样，但效果没有感觉出差别
#         num,rem = divmod(num, 16)
#         l.append(base[rem])
#         if num == 0:
#             return ''.join(l[::-1])

#浮点数转2进制
while True:
    number=input("请输入一个正数:(输入q退出程序）")
    if number in ['q','Q']:
        break
    elif not float(number)>0:
        print("请输入一个正数（输入q退出程序）：")
    else:
        number=float(number)
        array1=[]
        array2=[]
        integer=int(number)
        floa=number-integer
        while integer!=0:
            array1.append(integer%2)
            integer=integer//2
        else:
            array1.append(0)
        array1.reverse()
        while floa>0.00001:#精度为0.00001
            array2.append(int(2*floa))
            floa=floa*2-int(floa*2)
        else:
            array2.append(0)
        array1.append(".")
        array=array1+array2
        for x in array:
            print(x,end="")
        print("\n")

