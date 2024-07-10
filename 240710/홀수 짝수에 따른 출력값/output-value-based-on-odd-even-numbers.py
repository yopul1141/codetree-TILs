n = int(input())
def sum_val(n):
    if n%2 == 1:
        if n == 1:
            return 1
        return sum_val(n-2) + n
    else:
        if n == 2:
            return 2
        return sum_val(n-2) + n
print(sum_val(n))