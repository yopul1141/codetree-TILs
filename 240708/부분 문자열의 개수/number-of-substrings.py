a = input()
b = input()
def count_patterns(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i:i + 2] == b:
            count += 1
            i += 1
        else:
            i += 1

    return count
cnt = count_patterns(a)
print(cnt)