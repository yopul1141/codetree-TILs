n = int(input())
a = input()
a = a.replace(" ","") 
for i in range(0, len(a), 5):
    print(a[i:i + 5])