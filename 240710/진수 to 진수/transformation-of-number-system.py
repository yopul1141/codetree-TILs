a,b = map(int,input().split())
n = input()
arr = []
digits = []
for i in n:
    arr.append(int(i))
num = 0
for i in range(len(arr)):
    num = num * a + arr[i]

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

for i in digits[::-1]:
    print(i, end="")