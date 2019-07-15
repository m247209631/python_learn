def  recur_fibo(n):
    """使用递归函数
    生成斐波那契数列"""
    if n <= 1 :
        return n  #这里当n=0,输出0；当n=1，输出1；
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)


num = int(input('您需要输出几项： '))

if num <= 0:
    print('请输入正数')
else:
    for i in range(1,num+1):#如果0算第一项，则用range(num),如果不算用(1,num+1)
        print(recur_fibo(i))