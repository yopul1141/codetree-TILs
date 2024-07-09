n,m = map(int,input().split())
arr = list(map(int,input().split()))
def res_sum(n,m):
    for i in range(m):
        val = 0
        a1,a2 = map(int,input().split())
        for j in arr[a1-1:a2]:
            val += j
        print(val)
res_sum(n,m)