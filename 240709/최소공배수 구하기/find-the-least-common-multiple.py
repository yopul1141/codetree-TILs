import math
n,m = map(int,input().split())
gcd = math.gcd(n,m)
result = n*m//gcd
print(result)