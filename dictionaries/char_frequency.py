# this approach uses count() which counts how many times a character appears in a string. This approach has a time complexity of O(n^2) which is inefficient for long strings
def char_frequency(s):
  frequencies = {}
  for char in s:
    if char != " ":
      frequencies[char]=s.count(char)
  return frequencies

print(char_frequency("my name is barry allen and i am the fastest man alive"))

#Following is a better approach with time complexity O(n) because of single pass:

def frequency(s):
  frequencies = {}
  for char in s:
    if char != " ":
      if char in frequencies:
        frequencies[char] += 1
      else:
        frequencies[char] = 1
  return frequencies


print(frequency("hello"))




