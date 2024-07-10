class info:
    def __init__(self,height,weight,number):
        self.height = height
        self.weight = weight
        self.number = number
n = int(input())
students = []
for i in range(n):
    height,weight = input().split()
    students.append(info(int(height),int(weight),i+1))
students.sort(key=lambda x: (-x.height,-x.weight,x.number))
for i in range(n):
    a = students[i]
    print(a.height, a.weight, a.number)