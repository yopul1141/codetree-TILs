a,b = input().split()
num_a = ""
num_b = ""
for i in a:
    if i.isdigit() == True:
        num_a += i
    else:
        break
for i in b:
    if i.isdigit() == True:
        num_b += i
    else:
        break
print(int(num_a)+int(num_b))