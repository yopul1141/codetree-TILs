a = input().split()
arr = ''
for i in a:
    if i != '0':
        arr = i +' '+arr
    else:
        break
print(arr)