n = int(input())
cnt = 0
def sum_num(n):
    global cnt
    if n == 1:
        return cnt
    if n%2 == 0:
        cnt += 1
        return sum_num(n//2)
    else:
        cnt += 1
        return sum_num(n//3)
print(sum_num(n))