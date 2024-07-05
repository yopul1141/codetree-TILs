room = [0]*4
for i in range(3):
    info = input().split()
    if info[0] == 'Y' and int(info[1]) >= 37:
        room[0] += 1
    elif info[0] == 'N' and int(info[1]) >= 37:
        room[1] += 1
    elif info[0] == 'Y':
        room[2] += 1
    else:
        room[3] += 1
for i in room:
    print(i,end = " ")
if room[0] >= 2:
    print('E')