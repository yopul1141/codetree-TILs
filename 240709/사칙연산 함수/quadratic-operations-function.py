a,o,c = input().split()
def cal(a,o,c):
    if o in ['+', '-', '/', '*']:
        if o == '+':
            return int(a)+int(c)
        if o == '-':
            return int(a)-int(c)
        if o == '/':
            return "{int(a)/int(c):.1f}".format(int(a)/int(c))
        if o == '*':
            return int(a)*int(c)
    else:
        return False

if cal(a,o,c) == False:
    print(False)
else:
    print(f"{a} {o} {c} = {cal(a,o,c)}")