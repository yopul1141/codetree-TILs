cnt = 0
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    if sum(a)/len(a) >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
print(cnt)