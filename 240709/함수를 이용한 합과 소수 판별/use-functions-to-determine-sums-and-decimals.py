a,b = map(int,input().split())
cnt = 0
def sosu(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def odd(n):
    val = 0
    while n>0:
        val += n%10
        n //= 10
    if val%2 != 0:
        return False
    else:
        return True
for i in range(a,b+1):
    if sosu(i) == True and odd(i) == True:
        cnt += 1
print(cnt)