n = int(input())
val = 0
for i in range(n):
    a = int(input())
    val += a
val = str(val)
val = val[1:]+val[0]
print(val)