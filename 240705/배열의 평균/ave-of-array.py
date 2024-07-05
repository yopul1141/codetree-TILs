det = []
every = 0
for i in range(2):
    line = list(map(int,input().split()))
    det.append(line)
    every += sum(line)
    print(sum(line)/4,end = " ")
print()
for i in range(4):
    row = 0
    for j in range(2):
        row += det[j][i]
    print(row/2,end = " ")
print()
print(every/8)