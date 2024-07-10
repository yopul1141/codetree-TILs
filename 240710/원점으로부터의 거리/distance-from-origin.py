class info:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num
n = int(input())
dots = []
for i in range(n):
    x,y = map(int,input().split())
    dots.append(info(x,y,i+1))
dots.sort(key=lambda x: abs(x.x)+abs(x.y))
for i in range(n):
    a = dots[i]
    print(a.num)