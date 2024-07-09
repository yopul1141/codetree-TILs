while True:
    a = input()
    if a == 'END':
        break
    for i in a[::-1]:
        print(i,end="")
    print()