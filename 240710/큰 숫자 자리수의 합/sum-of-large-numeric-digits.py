arr = list(map(int,input().split()))
val = 1
for i in arr:
    val *= i
def sum_num(n):
    if n < 10:
        return n
    return sum_num(n//10) + n%10
print(sum_num(val))