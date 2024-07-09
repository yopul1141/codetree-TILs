arr = []
cnt = 0
while True:
    a = input()
    if a == '0':
        break
    arr.append(a)
    cnt += 1
print(cnt)
for i in range(cnt+1):
    if i%2 == 1:
        print(arr[i-1])