class info:
    def __init__(self,name,num,place):
        self.name = name
        self.num = num
        self.place = place
people = []
people_name = []
n = int(input())
for i in range(n):
    name,num,place = input().split()
    people.append(info(name,num,place))
for i in range(n):
    people_name.append(people[i].name)
people_name = sorted(people_name)
person = people[-1]
print(f"name {person.name}")
print(f"addr {person.num}")
print(f"city {person.place}")