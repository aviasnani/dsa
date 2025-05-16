def find_min(nums):
  min_num = float('inf')
  if len(nums) < 2:
    return None
  for num in nums:
    if num < min_num:
      min_num = num 
  return min_num

print(find_min([1, 2, 3, 4, 5]))