num = int(input("输入一个整数："))
a=0
b=1
if num <=0:
    print("请输入一个正整数！")
elif num==1:
    print("斐波拉契数列：%d" % a)
else:
    print("斐波拉契数列：",end="")
    print(a,b,end=" ")
    for n in range(1,num-1):
        f=a+b
        a,b=b,f
        print(f,end=" ")