import math
n = int(input())
arr = list(map(int,input().split()))

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result
print(lcm_multiple(arr))