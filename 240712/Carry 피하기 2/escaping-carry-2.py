n = int(input())
arr = []
for i in range(n):
    a = input()
    if len(a) < 4:
        a = '0'*(4-len(a)) + a
    arr.append(a)

def possible(i, j, k):
    for l in range(4):
        if int(arr[i][l]) + int(arr[j][l]) + int(arr[k][l]) >= 10:
            return False
    return True

true_case = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i != j != k:
                if possible(i,j,k):
                    true_case.append([i,j,k])

max_val = 0
for i, j, k in true_case:
    max_val = max(max_val, int(arr[i]) + int(arr[j]) + int(arr[k]))

if max_val == 0:
    print(-1)
else:
    print(max_val)