n = input()
m = input()
n = sorted(n)
m = sorted(m)
def same(n):
    for i in range(max(len(n),len(m))):
        if n[i] != m[i]:
            return 'No'
        else:
            return 'Yes'
print(same(n))