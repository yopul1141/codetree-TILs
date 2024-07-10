class info:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
students = []
for i in range(5):
    name,height,weight = input().split()
    students.append(info(name,int(height),float(weight)))
students.sort(key=lambda x: x.name)
print('name')
for i in range(5):
    a = students[i]
    print(a.name, a.height, a.weight)
print()
print('height')
students.sort(key=lambda x: -x.height)
for i in range(5):
    a = students[i]
    print(a.name, a.height, a.weight)