a = list(map(int,input().split()))
sum = 0
cnt = 0
for i in a:
    if i < 250:
        sum += i
        cnt += 1
    else:
        break
print(f"{sum} {sum/cnt:.1f}")