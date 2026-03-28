"""
Running sum of 1d arry
dsa question.
"""
# arr =[1,2,3,4,5,6,77,88,9,9]
# sum1 = []
# n = len(arr)
# current_sum = 0

# for i in range (0,n):
#     current_sum = current_sum + arr[i]
#     sum1.append(current_sum)
# print (sum1)

"""

remove dublicates from shorted arry
"""
nums = [1,2,4,56,2,1,1,2,3,4,5,56,6,7,34,4,4]

nums.sort()   

n = len(nums)

start = 0

for i in range(1, n):
    if nums[i] != nums[start]:
        start += 1
        nums[start] = nums[i]

print("Unique count:", start + 1)
print("Unique elements:", nums[:start + 1])