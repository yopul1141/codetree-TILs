n = int(input())
def sum_num(n):
    if n < 10:
        return n**2
    return sum_num(n//10) + (n%10)**2
print(sum_num(n))