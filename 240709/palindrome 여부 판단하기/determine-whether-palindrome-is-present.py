a = input()
def palin(n):
    op = ""
    for i in n[::-1]:
        op += i
    if op == n:
        return 'Yes'
    else:
        return 'No'
print(palin(a))