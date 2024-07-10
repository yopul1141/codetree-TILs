a,b,c = map(int,input().split())
def cal_time(x,y,z):
    x *= 1440
    y *= 60
    return(x+y+z)
if cal_time(a,b,c) - cal_time(11,11,11) > 0:
    print(cal_time(a,b,c) - cal_time(11,11,11))
else:
    print(-1)