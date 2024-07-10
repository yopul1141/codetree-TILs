m1,d1,m2,d2 = map(int,input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def cal_day(m,d):
    days = 0
    for i in num_of_days[:m]:
        days += i
    days += d
    return days
print(cal_day(m2,d2)-cal_day(m1,d1)+1)