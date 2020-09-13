#Author:Y
#2020.09.13

def move(n,a,b,c):
    if n==1:
        print(a,'---->',c)
    else:
        move(n-1,a,c,b)
        print(a,'---->',c)
        move(n-1,b,a,c)

n = int(input("请输入n的值："))
move(n,"A","B","C")
