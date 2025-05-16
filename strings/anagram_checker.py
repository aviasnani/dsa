def anagram_checker(s1, s2):
  s1_list = list(s1.lower())
  s2_list = list(s2.lower())
  len_s1 = len(s1_list)
  len_s2 = len(s2_list)
  for i in range(len_s1):
    for j in range(len_s1-i-1):
      if s1_list[j] > s1_list[j+1]:
        s1_list[j], s1_list[j+1] = s1_list[j+1], s1_list[j]
  for i in range(len_s2):
    for j in range(len_s2-i-1):
      if s2_list[j] > s2_list[j+1]:
        s2_list[j], s2_list[j+1] = s2_list[j+1], s2_list[j]
  if s1_list == s2_list:
    return True 
  return False

print(anagram_checker("racecar", "carrace"))

# below is an efficient approach 

def anagram(str1, str2):
  str1_list = list(str1.lower())
  str2_list = list(str2.lower())
  str1_list.sort()
  str2_list.sort()
  if str1_list == str2_list:
    return True
  return False

print(anagram("racecar", "carrace"))
