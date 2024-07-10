m1,d1,m2,d2 = map(int,input().split())
a = input()
date = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def find_day(m,d):
    days = 0
    for i in num_of_days[:m]:
        days += i
    days += d
    return days
day = find_day(m2,d2) - find_day(m1,d1)
def find_date(a):
    global day
    cnt = 0
    while day > 0:
        if date[day%7] == a:
            cnt += 1
        day -= 1
    return cnt
print(find_date(a))