class info:
    def __init__(self,name,num,place):
        self.name = name
        self.num = num
        self.place = place
people = []
n = int(input())
for i in range(n):
    name,num,place = input().split()
    people.append(info(name,num,place))
person = people[-1]
print(f"name {person.name}")
print(f"addr {person.num}")
print(f"city {person.place}")