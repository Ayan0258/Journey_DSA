"""
Running sum of 1d arry
dsa question.
"""
arr =[1,2,3,4,5,6,77,88,9,9]
sum1 = []
n = len(arr)
current_sum = 0

for i in range (0,n):
    current_sum = current_sum + arr[i]
    sum1.append(current_sum)
print (sum1)