class info:
    def __init__(self,height,weight,num):
        self.height = height
        self.weight = weight
        self.num = num
n = int(input())
students = []
for i in range(n):
    height,weight = map(int,input().split())
    students.append(info(height,weight,i+1))
students.sort(key=lambda x: (x.height,-x.weight))
for i in range(n):
    a = students[i]
    print(a.height, a.weight, a.num)