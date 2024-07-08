def count_patterns(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i:i + 2] == find:
            count += 1
            i += 1
        i += 1
    if count == 0:
        count = -1
    return count

n = input()
find = input()
cnt = count_patterns(n)
print(cnt)