def second_largest(nums):
  max_num = float('-inf')
  second_largest = float('-inf')
  if len(nums) < 2:
    return None
  for num in nums:
    if num > max_num:
      max_num = num 
  for num in nums: 
    if num > second_largest and num != max_num:
      second_largest = num
  return second_largest

print(second_largest([1, 2, 3, 4, 5]))