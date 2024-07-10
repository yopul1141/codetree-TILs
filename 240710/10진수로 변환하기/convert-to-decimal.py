a = input()
arr = []
for i in a:
    arr.append(int(i))
num = 0

for i in range(len(arr)):
    num = num * 2 + arr[i]

print(num)