a = input()
b = input()
for i in range(len(a)):
    a = a[-1]+a[:-1]
    if a == b:
        print(i+1)
        break
    if i+1 == len(a):
        print(-1)