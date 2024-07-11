n,m = map(int,input().split())
a = []
b = []
dis = 0
for i in range(n):
    d,t = input().split()
    for j in range(int(t)):
        if d == 'L':
            dis -= 1
            a.append(dis)
        if d == 'R':
            dis += 1
            a.append(dis)
dis = 0
for i in range(m):
    d,t = input().split()
    for j in range(int(t)):
        if d == 'L':
            dis -= 1
            b.append(dis)
        if d == 'R':
            dis += 1
            b.append(dis)
for i in range(len(a)):
    if a[i] == b[i]:
        print(i+1)
        break
    else:
        if i == len(a)-1:
            print(-1)