class info:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
n = int(input())
students = []
for i in range(n):
    name,height,weight = input().split()
    students.append(info(name,int(height),int(weight)))
students.sort(key=lambda x: (x.height,-x.weight))
for i in range(n):
    a = students[i]
    print(a.name, a.height, a.weight)