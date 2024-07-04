a,b = map(int,input().split())

for i in range(9):
    c = b
    for j in range(3):
        while a <= c <= b:
            print(f"{c} * {i+1} = {c*(i+1)}",end=" ")
            if a != c:
                print('/', end=" ")
            c -= 2
    print()