#约瑟夫生者死者小游戏
people=list(range(30))
while len(people)>15:
    i=1
    while i<9:
        people.append(people.pop(0))#把没有下船的放到列的末尾
        i+=1
    print('{:2d}号下船了'.format(people.pop(0)))

