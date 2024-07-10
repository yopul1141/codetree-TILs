a,b,c,d = map(int,input().split())
def cal_time(x,y):
    x *= 60
    return(x+y)
print(cal_time(c,d)-cal_time(a,b))