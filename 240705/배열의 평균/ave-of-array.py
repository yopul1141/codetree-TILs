det = []
every = 0
for i in range(2):
    line = list(map(int,input().split()))
    det.append(line)
    every += sum(line)
    print(f"{sum(line)/4}",end = " ")
print()
for i in range(4):
    row = 0
    for j in range(2):
        row += det[j][i]
    print(f"{row/2:.1f}",end = " ")
print()
print(f"{every/8:.1f}")