n = int(input())
a = list(map(int, input().split()))
cnt_1 = cnt_2 = cnt_3 = cnt_4 = cnt_5 = cnt_6 = cnt_7 = cnt_8 = cnt_9 = 0
for i in a:
    if i == 1:
        cnt_1 += 1
    elif i == 2:
        cnt_2 += 1
    elif i == 3:
        cnt_3 += 1
    elif i == 4:
        cnt_4 += 1
    elif i == 5:
        cnt_5 += 1
    elif i == 6:
        cnt_6 += 1
    elif i == 7:
        cnt_7 += 1
    elif i == 8:
        cnt_8 += 1
    else:
        cnt_9 += 1
print(cnt_1)
print(cnt_2)
print(cnt_3)
print(cnt_4)
print(cnt_5)
print(cnt_6)
print(cnt_7)
print(cnt_8)
print(cnt_9)