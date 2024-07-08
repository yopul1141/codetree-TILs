n = list(input())
a = n[0]
b = n[1]
for i in range(len(n)):
    if n[i] == a:
        n[i] = b
    elif n[i] == b:
        n[i] = a
print(''.join(n))