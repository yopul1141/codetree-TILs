n = input()
if len(n)%2 == 0:
    for i in n[::-2]:
        print(i, end = "")
else:
    for i in n[-2::-2]:
        print(i, end = "")