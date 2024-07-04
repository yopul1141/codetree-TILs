# 입력 받기
n = int(input())
a = list(map(int, input().split()))

# 빈도 저장할 리스트 초기화
counts = [0] * 10

# 각 숫자의 빈도 계산
for number in a:
    counts[number] += 1

# 1부터 9까지 각 숫자의 빈도 출력
for i in range(1, 10):
    print(counts[i])