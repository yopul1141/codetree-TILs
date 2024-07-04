a = list(map(int, input().split()))
odd = 0
even = 0
for i in a[::2]:
    odd += i
for i in a[1::2]:
    even += i
if odd > even:
    print(odd - even)
else:
    print(even - odd)