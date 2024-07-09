a = input()
def same(n):
    for i in range(len(n)):
        if n[i]!=n[i+1]:
            return 'Yes'
    return 'No'
print(same(a))