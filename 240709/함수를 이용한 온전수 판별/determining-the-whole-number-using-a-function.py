a,b = map(int,input().split())
cnt = 0
def onjeon(n):
    if n%2 == 0:
        return False
    if n%10 == 5:
        return False
    if n%3 == 0 and n%9 != 0:
        return False
    return True
for i in range(a,b+1):
    if onjeon(i) == True:
        cnt += 1
print(cnt)