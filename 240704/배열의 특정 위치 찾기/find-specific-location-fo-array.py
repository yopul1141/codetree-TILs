a = list(map(int,input().split()))
val_2 = 0
val_3 = 0
cnt = 0
for i in range(1,len(a),2):
    val_2 += a[i]
for i in range(2,len(a),3):
    val_3 += a[i]
    cnt += 1
print(f"{val_2} {val_3/cnt:.1f}")