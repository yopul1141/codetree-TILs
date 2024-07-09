n = int(input())
def print_low(n):
    if n == 0:
        return
    print_low(n-1)
    print(n,end=" ")
def print_high(n):
    if n == 0:
        return
    print(n,end=" ")
    print_high(n-1)
print_low(n)
print()
print_high(n)