n1,n2 = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def is_subsequence(A,B):
    for i in range(n1 - n2 + 1):
        if A[i:i+n2] == B:
            return True
    return False

if is_subsequence(a,b):
    print("Yes")
else:
    print("No")