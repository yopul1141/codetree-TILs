n,m,k = map(int,input().split())
arr = [0] * n
def find_student(n,m,k):
    for i in range(m):
        t = int(input())
        arr[t-1] += 1
        for j in range(n):
            if arr[j] == k:
                return j+1        
    if max(arr) != k:
        return -1
print(find_student(n,m,k))