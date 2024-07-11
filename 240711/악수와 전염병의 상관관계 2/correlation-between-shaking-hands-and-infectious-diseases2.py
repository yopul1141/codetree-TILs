n,k,p,s = map(int,input().split())
infect = [0]*(n+1)
count = [0]*(n+1)
infos = []
for i in range(s):
    t,x,y = map(int,input().split())
    infos.append((t,x,y))
infos.sort()
infect[p] = 1
for i in range(s):
    info = infos[i]
    if infect[info[1]] == 1 or infect[info[2]] == 1:
        if infect[info[1]] == 1 and infect[info[2]] == 1:
            if count[info[1]] < k:
                count[info[1]] += 1
            if count[info[2]] < k:
                count[info[2]] += 1
        elif infect[info[1]] == 1 and count[info[1]] < k:
            count[info[1]] += 1
            infect[info[2]] = 1
        elif infect[info[2]] == 1 and count[info[2]] < k:
            count[info[2]] += 1
            infect[info[1]] = 1
for i in range(1,n+1):
    print(infect[i],end = "")