n = int(input())
def sum_val(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return sum_val(n//3) + sum_val(n-1)
print(sum_val(n))