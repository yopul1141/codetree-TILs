def count_str(s):
    ee_count = s.count('ee')
    eb_count = s.count('eb')
    return ee_count, eb_count

n = input()

ee_count, eb_count = count_str(n)
print(ee_count, eb_count)