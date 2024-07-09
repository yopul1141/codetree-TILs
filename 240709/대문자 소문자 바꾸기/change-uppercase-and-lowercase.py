a = input()
for i in a:
    if i.isupper() == True:
        print(i.lower(),end="")
    elif i.islower() == True:
        print(i.upper(),end="")