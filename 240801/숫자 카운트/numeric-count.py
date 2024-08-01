def count_possible_numbers(n, queries):
    from itertools import permutations

    all_possible_numbers = list(permutations(range(1, 10), 3))
    valid_count = 0

    for number_tuple in all_possible_numbers:
        number = ''.join(map(str, number_tuple))
        is_valid = True

        for query in queries:
            query_number, count1, count2 = query
            c1, c2 = 0, 0

            for i in range(3):
                if number[i] == query_number[i]:
                    c1 += 1
                elif number[i] in query_number:
                    c2 += 1
            
            if c1 != count1 or c2 != count2:
                is_valid = False
                break

        if is_valid:
            valid_count += 1

    return valid_count

n = int(input())
queries = []

for _ in range(n):
    guess, c1, c2 = input().split()
    queries.append((guess, int(c1), int(c2)))

print(count_possible_numbers(n, queries))