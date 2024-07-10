n = input()
m = input()
n = sorted(n)
m = sorted(m)
def same(n):
    for i in range(len(n)):
        if len(n) != len(m):
            return 'No'
        if n[i] != m[i]:
            return 'No'
    return 'Yes'
print(same(n))