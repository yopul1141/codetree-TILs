a,b = map(int,input().split())
val = 0
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(a,b+1):
    res = is_prime(i)
    if res == True:
        val += i
if a == b:
    val = 0
print(val)