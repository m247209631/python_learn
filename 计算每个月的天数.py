import calendar
monthRange = calendar.monthrange(2016,9)
print(monthRange)
#输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数
# 以上实例输出（3,30)的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天

#若只想知道天数，只需要使用calendar.mdays即可
#输出为[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],第0个月0天
for i in range(13):
    print(calendar.mdays[i])