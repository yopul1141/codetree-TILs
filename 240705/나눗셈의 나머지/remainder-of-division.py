a,b = map(int,input().split())
arr = [0]*b
val = 0
while a > 1:
    arr[a%b] += 1
    a = a//b
for i in arr:
    val += i**2
print(val)