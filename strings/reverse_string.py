def reverse_string(s):
  right = len(s) - 1
  reverse = ""
  while right >= 0:
    reverse += s[right]
    right -= 1
  return reverse

print(reverse_string("barryallen"))