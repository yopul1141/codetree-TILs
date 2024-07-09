a = input()
b = input()
num_a = ""
num_b = ""
for i in a:
    if i.isdigit() == True:
        num_a += i
for i in b:
    if i.isdigit() == True:
        num_b += i
print(int(num_a)+int(num_b))