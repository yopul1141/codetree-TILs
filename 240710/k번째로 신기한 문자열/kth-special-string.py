n,k,t = input().split()
arr = []
cnt = 0
for i in range(int(n)):
    a = input()
    arr.append(a)
arr.sort()
for i in range(int(n)):
    if t in arr[i]:
        cnt += 1
        if cnt == int(k):
            print(arr[i])
            break