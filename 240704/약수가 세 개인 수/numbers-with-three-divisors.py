a,b = map(int,input().split())
cnnt = 0
cnnnt = 0
for i in range(a,b+1):  # 약수가 3개인지 체크하려는 수 i (a ~ b)
    cnnt = 0
    for j in range(1,i+1): # i의 약수가 될 j를 찾기위한 for문
        if i % j == 0:  # j가 i의 약수인지 체크
            cnnt += 1
    if cnnt == 3:
        cnnnt += 1
print(cnnnt)