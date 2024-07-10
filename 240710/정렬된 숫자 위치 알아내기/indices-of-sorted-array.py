class info:
    def __init__(self,value,cur):
        self.value = value
        self.cur = cur
n = int(input())
arr = list(map(int,input().split()))
elements = [info(value, index) for index, value in enumerate(arr)]
elements.sort(key=lambda x: (x.value, x.cur))
new = [0] * n

for new_index, element in enumerate(elements):
    new[element.cur] = new_index + 1
print(" ".join(map(str, new)))