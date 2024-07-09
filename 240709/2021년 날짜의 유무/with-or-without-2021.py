M,D = map(int,input().split())
def find_date(M,D):
    if M == 2:
        if D>28:
            return False
    if M > 12:
        return False
    if M%2 == 0:
        if D > 30:
            return False
    else:
        if D > 31:
            return False
    return True
if find_date(M,D) == True:
    print("Yes")
else:
    print("No")