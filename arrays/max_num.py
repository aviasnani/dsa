def find_max(nums):
  max_num = float('-inf')
  if len(nums) < 2:
    return None
  for num in nums:
    if num > max_num:
      max_num = num 
  return max_num

print(find_max([1, 2, 3, 4, 5]))