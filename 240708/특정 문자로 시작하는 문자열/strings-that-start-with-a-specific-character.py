n = int(input())
arr = []
cnt = 0
cnt_len = 0
for i in range(n):
    a = input()
    arr.append(a)
find = input()
for i in arr:
    if i[0] == find:
        cnt += 1
        cnt_len += len(i)
print(f"{cnt} {cnt_len/cnt:.2f}")