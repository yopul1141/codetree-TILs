class info:
    def __init__(self,date,days,weather):
        self.date = date
        self.days = days
        self.weather = weather
users = []
n = int(input())
for i in range(n):
    date,days,weather = input().split()
    users.append(info(date,days,weather))
users.sort(key=lambda x: x.date)
for i in range(n):
    a = users[i]
    if a.weather == "Rain":
        print(a.date,a.days,a.weather)
        break