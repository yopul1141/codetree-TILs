arr = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()
cnt = 0
for i in range(5):
    if n == arr[i][2] or n == arr[i][3]:
        print(arr[i])
        cnt += 1
print(cnt)