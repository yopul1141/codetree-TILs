n = int(input())
cnt = 0
def sum_val(n):
    global cnt
    if n == 1:
        return cnt
    if n%2 == 0:
        cnt += 1
        return sum_val(n//2)
    else:
        cnt += 1
        return sum_val(n*3+1)
print(sum_val(n))