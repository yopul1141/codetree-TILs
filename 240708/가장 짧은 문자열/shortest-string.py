a = input()
b = input()
c = input()
if len(a) > len(b):
    if len(a) > len(c):
        if len(b) > len(c):
            print(len(a)-len(c))
        else:
            print(len(a)-len(b))
    else:
        print(len(c)-len(b))
else:
    if len(b) > len(c):
        if len(a) > len(c):
            print(len(b)-len(a))
        else:
            print(len(b)-len(c))
    else:
        print(len(c)-len(a))