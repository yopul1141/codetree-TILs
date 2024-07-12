a = input()
cnt = 0

for i in range(1,len(a)):
    if a[i-1] == '(' and a[i] == '(':
        for j in range(i+2, len(a)):
            if a[j-1] == ')' and a[j] == ')':
                cnt += 1
print(cnt)