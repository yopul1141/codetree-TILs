n,m = map(int,input().split())
a = []
b = []
dis_a = 0
dis_b = 0
cnt = 0
pre = None
for i in range(n):
    t,d = input().split()
    for j in range(int(t)):
        if d == 'L':
            dis_a -= 1
            a.append(dis_a)
        if d == 'R':
            dis_a += 1
            a.append(dis_a)
for i in range(m):
    t,d = input().split()
    for j in range(int(t)):
        if d == 'L':
            dis_b -= 1
            b.append(dis_b)
        if d == 'R':
            dis_b += 1
            b.append(dis_b)
if len(a) > len(b):
    for i in range(len(a)-len(b)):
        b.append(dis_b)
else:
    for i in range(len(b)-len(a)):
        a.append(dis_a)
for i in range(len(a)):
    if a[i] > b[i]:
        cur = '>'
    elif a[i] < b[i]:
        cur = '<'
    else:
        cur = '='
    if pre is not None and pre != cur and cur == '=':
        cnt += 1
    pre = cur
print(cnt)