def is_369(n):
    while n > 0:
        digit = n % 10
        if digit in [3, 6, 9]:
            return True
        n //= 10
    return False

def is_3(n):
    return n % 3 == 0

a, b = map(int, input().split())

cnt = 0
for i in range(a,b+1):
    if is_369(i):
        cnt += 1
    elif is_3(i):
        cnt += 1

print(cnt)