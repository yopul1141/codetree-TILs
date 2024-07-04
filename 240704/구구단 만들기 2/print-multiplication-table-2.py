a,b = map(int, input().split())
for i in range(4):
    c = b
    for j in range(3):
        while a <= c <= b:
            print(f"{c} * {(i+1)*2} = {c*(i+1)*2}",end=" ")
            if c != a:
                print('/',end=" ")
            c -= 1
    print()