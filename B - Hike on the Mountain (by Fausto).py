# ITACPC 2023
# B - Hike on the Mountain
# (hike)
# Made by Fausto Allegrini

# 2 <= n <= 1000
n = int(input()) 

# -3 <= d <= 3
d = input()

sum = 0
alt = d.split()
for i in alt:
    sum += int(i)

print(3000 + sum)
