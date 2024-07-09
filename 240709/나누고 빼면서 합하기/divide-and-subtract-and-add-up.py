n,m = map(int,input().split())
arr = list(map(int,input().split()))
a = []
def find_m(m):
    while m>0:
        if m%2==0:
            a.append(m)
            m //= 2
        else:
            a.append(m)
            m -= 1
def sum_val(a):
    val = 0
    for i in a:
        val += arr[i-1]
    return val
find_m(m)
print(sum_val(a))