a = input()
a_list = [int(c) for c in a]

if 0 not in a_list:
    a_list[-1] = 0
else:
    for index, value in enumerate(a_list): 
        if value == 0:
            a_list[index] = 1
            break

num = 0
for i in a_list:
    num = num * 2 + i

print(num)