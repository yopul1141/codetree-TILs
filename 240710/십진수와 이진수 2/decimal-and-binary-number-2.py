n = input()
arr = []
digits = []
for i in n:
    arr.append(int(i))
num = 0
for i in range(len(arr)):
    num = num * 2 + arr[i]
num *= 17

while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

for i in digits[::-1]:
    print(i, end="")