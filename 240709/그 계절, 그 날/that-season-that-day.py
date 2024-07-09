Y,M,D = map(int,input().split())
def yoon(Y,M,D):
    if Y%4 != 0:
        return False
    if Y%100 == 0 and Y%400 != 0:
        return False
    return True
def exist(Y,M,D):
    if yoon(Y,M,D) == True:
        if M == 2:
            if D>29:
                return False
    else:
        if M == 2:
            if D>28:
                return False
    if M > 12:
        return False
    if M < 8:
        if M%2 == 0:
            if D > 30:
                return False
        else:
            if D > 31:
                return False
    if M > 7:
        if M%2 == 0:
            if D > 31:
                return False
        else:
            if D > 30:
                return False
    return True

def season(Y,M,D):
    if 3<= M <=5:
        print('Spring')
    elif 6<= M <=8:
        print('Summer')
    elif 9<= M <= 11:
        print('Fall')
    else:
        print('Winter')

if exist(Y,M,D) == False:
    print(-1)
else:
    season(Y,M,D)