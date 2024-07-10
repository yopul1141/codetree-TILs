class info:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
n = int(input())
students = []
for i in range(n):
    name,kor,eng,math = input().split()
    students.append(info(name,int(kor),int(eng),int(math)))
students.sort(key=lambda x: (-x.kor,-x.eng,-x.math))
for i in range(n):
    a = students[i]
    print(a.name,a.kor,a.eng,a.math)