# ITACPC 2023
# I - Sum of Digits
# (digits)
# Made by Pegorari Lorenzo

# 0 <= d <= 9 and 1 <= n <= 60
d, n = input().split(' ')
n = int(n)

if n < 2:
    print(d)
else:
    start = ''.join([d, '2', d])
    tot = 0
    for digit in start:
        tot += int(digit)
    
    for i in range(3, n + 1):
        tot_digits = 0
        for digit in str(i):
            tot_digits += int(digit)
        tot = tot * 2 + tot_digits
    print(tot)