n = int(input())
arr = list(map(int, input().split()))
count_dict = {}
for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
max_val = -1
for num, count in count_dict.items():
    if count == 1:
        if num > max_val:
            max_val = num

print(max_val)