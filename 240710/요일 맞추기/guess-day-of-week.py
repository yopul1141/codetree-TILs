m1,d1,m2,d2 = map(int,input().split())
date = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def find_day(m,d):
    days = 0
    for i in num_of_days[:m]:
        days += i
    days += d
    return days
days = find_day(m2,d2) - find_day(m1,d1)
print(date[days%7])