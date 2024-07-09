a = input()
for i in a:
    if i.isalpha() == True:
        print(i.lower(),end = "")
    elif i.isdigit() == True:
        print(i,end = "")