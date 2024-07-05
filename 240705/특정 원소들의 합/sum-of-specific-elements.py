lst =[list(map(int, input().split())) for i in range(4)]
ssum=0
for j, i in enumerate(lst, start=1):
    ssum += sum(i[ :j])
    
    
print(ssum)