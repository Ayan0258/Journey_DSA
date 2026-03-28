"""
we have a arry we have to count the frequesncy of that arry

"""

arr = [1, 2, 2, 3, 1, 4, 2]

d = {}

for num in arr:
    if num in d:
        d[num] += 1

    else:
        d[num] = 1

print(d)