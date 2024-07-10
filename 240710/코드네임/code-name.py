class info:
    def __init__(self,name,score):
        self.name = name
        self.score = score
min_val = 101
min_num = -1
people = []
for i in range(5):
    name,score = input().split()
    people.append(info(name,int(score)))
for i in range(5):
    person = people[i]
    val = person.score
    if min_val > val:
        min_val = val
        min_num = i
print(people[min_num].name, people[min_num].score)