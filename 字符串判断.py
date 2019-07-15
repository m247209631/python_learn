#字符串
strs = ['runoob.com','runoob','Aunoob']

for str in strs:
    print(str.isalnum(), # 判断所有字符都是数字或者字母
          str.isalpha(), # 判断所有字符都是字母
          str.isdigit(), #判断所有字符都是数字
          str.islower(), # 判断所有字符都是小写
          str.isupper(), # 判断所有字符都是大写
          str.istitle(), # 判断所有单词都是首字母大写，像标题
          str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r
    print()

