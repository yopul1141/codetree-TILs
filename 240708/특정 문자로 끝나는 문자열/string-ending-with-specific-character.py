arr = []
cnt = 0
for i in range(10):
    a = input()
    arr.append(a)
find = input()
for i in arr:
    if i[-1] == find:
        print(i)
        cnt += 1
if cnt == 0:
    print("None")