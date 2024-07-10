n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
def same(n):
    for i in range(n):
        if a[i] != b[i]:
            return 'No'
    return 'Yes'
print(same(n))