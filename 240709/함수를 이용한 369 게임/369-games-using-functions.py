a,b = map(int,input().split())
def is_369(n):
    return (n//10)%3 == 0 or (n%10)%3 == 0
def is_3(n):
    return n%3 == 0
cnt = 0
for i in range(a,b+1):
    if is_369(i):
        cnt += 1
    elif is_3(i):
        cnt += 1
print(cnt)