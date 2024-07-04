val = 0
cnt = 0
a = list(map(int, input().split()))
for i in a:
    if i != 0:
        val += i
        cnt += 1
    else:
        break
print(f"{val} {val/cnt:.1f}")