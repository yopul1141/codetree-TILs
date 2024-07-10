n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if a.sort() == b.sort():
    print('Yes')
else:
    print('No')