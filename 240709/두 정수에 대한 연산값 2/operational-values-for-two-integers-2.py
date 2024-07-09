a,b = map(int,input().split())
def edit_val(a,b):
    if a>b:
        b += 10
        a *= 2
    else:
        a += 10
        b *= 2
    return a,b
a,b = edit_val(a,b)
print(a,b)