n1,n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(n1 - n2 + 1):
    if A[i:i+n2] == B:
        print("Yes")
        break
    else:
        if i == n1-n2:
            print("No")
        else:
            continue