n = input()
encoded_str = ""
cnt = 1
current_char = n[0]

for i in range(1, len(n)):
    if n[i] == current_char:
        cnt += 1
    else:
        encoded_str += current_char + str(cnt)
        current_char = n[i]
        cnt = 1

encoded_str += current_char + str(cnt)

print(len(encoded_str))
print(encoded_str)