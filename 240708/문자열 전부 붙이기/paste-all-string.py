n = int(input())
arr = []
res = ""
for i in range(n):
    a = input()
    arr.append(a)
for i in arr:
    res += i
print(res)