def find_first_non_repeating_char(s):
  if s == "":
    return None
  frequencies = {}
  for char in s:
    if char != " ":
      if char in frequencies:
        frequencies[char] += 1
      else:
        frequencies[char] = 1
  for c in s:
    if c != " " and frequencies[char] == 1:
      return c
  return None

    
print(find_first_non_repeating_char("aabbcc"))