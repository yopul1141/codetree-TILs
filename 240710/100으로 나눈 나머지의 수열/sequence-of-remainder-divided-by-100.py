n = int(input())
def dup_val(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return dup_val(n-1) * dup_val(n-2) % 100
print(dup_val(n))