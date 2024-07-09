a = input()
val = 0
for i in a:
    if i.isdigit() == True:
        val += int(i)
print(val)