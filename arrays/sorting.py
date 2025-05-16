def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(n-1-i):  
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

print(bubble_sort([3, 1, 4, 1, 2, 6, 3, 4, 4, 1]))

def check_sorted(arr):
  n = len(arr)
  is_sorted = True
  for i in range(n-1):
      if arr[i] > arr[i+1]:
        is_sorted = False
  return is_sorted

print(check_sorted([1,2,3,4,5,1]))