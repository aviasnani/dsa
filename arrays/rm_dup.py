def remove_duplicates(nums):
  if not nums:
    return 0
  final = []
  nums.sort()
  for num in nums:
    if num not in final:
      final.append(num)
  return final


print(remove_duplicates([3,1,4,1,2,6,3,4,4,1]))


