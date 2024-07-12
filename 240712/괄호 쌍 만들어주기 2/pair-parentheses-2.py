a = input()
cnt = 0

for i in range(len(a)):
    if a[i] == '(' and a[i+1] == '(':
        for j in range(i+3, len(a)):
            if a[j-1] == ')' and a[j] == ')':
                cnt += 1
print(cnt)