n = int(input())
def all_sum(n):
    result = 0
    for i in range(n+1):
        result += i
        result = result//10
    return result
print(all_sum(n))