n,b = map(int,input().split())
arr = []
while True:
    if n < b:
        arr.append(n)
        break

    arr.append(n % b)
    n //= b

for i in arr[::-1]:
    print(i, end="")