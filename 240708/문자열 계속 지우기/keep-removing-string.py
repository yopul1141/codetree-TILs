a = input()
b = input()
while b in a:
    ind = a.index(b)
    a = a[:ind]+a[ind+len(b):]
print(a)