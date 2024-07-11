n,m = map(int,input().split())
a = []
b = []
dis = 0
cnt = 0
pre = None
for i in range(n):
    v,t = map(int,input().split())
    for j in range(t):
        dis += v
        a.append(dis)
dis = 0
for i in range(m):
    v,t = map(int,input().split())
    for j in range(t):
        dis += v
        b.append(dis)
for i in range(len(a)):
    if a[i] > b[i]:
        cur = '>'
    elif a[i] < b[i]:
        cur = '<'
    if pre is not None and pre != cur:
        cnt += 1
    pre = cur
print(cnt)