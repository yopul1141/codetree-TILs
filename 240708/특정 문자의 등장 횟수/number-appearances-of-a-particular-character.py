def count_patterns(s):
    ee_count = 0
    eb_count = 0
    
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] == 'ee':
            ee_count += 1
            i += 1
        elif s[i:i+2] == 'eb':
            eb_count += 1
            i += 1
        i += 1
    
    return ee_count, eb_count

n = input()

ee_count, eb_count = count_patterns(n)
print(ee_count, eb_count)