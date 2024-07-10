class info:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
n = int(input())
student = []
for i in range(n):
    name,height,weight = input().split()
    student.append(info(name,height,weight))
student.sort(key=lambda x:x.height)
for i in range(n):
    a = student[i]
    print(a.name, a.height, a.weight)