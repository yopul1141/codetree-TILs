n = int(input())
arr = []
cnt_a = 0
cnt_len = 0
for i in range(n):
    a = input()
    arr.append(a)
for i in arr:
    cnt_len += len(i)
    if i[0] == 'a':
        cnt_a += 1
print(cnt_len, cnt_a)