# ITACPC 2023
# I - Sum of Digits
# (digits)
# Made by Pegorari Lorenzo

# 1 <= n <= 100000
n = int(input())

list_of_tuples = []
for _ in range(n):
    # x either 1 or -1 and 0 <= y <= 1000000
    x, y = input().split(' ')
    list_of_tuples.append((int(x), int(y)))


sorted_list_of_tuples = sorted(list_of_tuples, key=lambda tup: tup[1])

max_val = 0
current = 0
i = 0
while i < n:
    current += sorted_list_of_tuples[i][0]
    for j in range(i + 1, n):
        if sorted_list_of_tuples[i][1] == sorted_list_of_tuples[j][1]:
            current += sorted_list_of_tuples[j][0]
            i += 1
        else:
            break
    if current > max_val:
        max_val = current
    i += 1

print(max_val)
