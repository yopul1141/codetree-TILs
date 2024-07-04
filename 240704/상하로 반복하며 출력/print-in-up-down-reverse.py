n = int(input())

def generate_pattern(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row += str(i) if j % 2 == 1 else str(n + 1 - i)
        print(row)


generate_pattern(n)