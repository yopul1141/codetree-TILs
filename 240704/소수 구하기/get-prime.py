n = int(input())

# 1부터 n까지의 숫자 중 소수를 출력하는 코드
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i, end=" ")