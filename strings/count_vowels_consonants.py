def vowel_consonant_count(s):
  vowel_count=0
  consonant_count = 0
  vowels = ['a', 'e', 'i', 'o', 'u']
  for c in s:
    if c in vowels:
      vowel_count += 1
    else:
      consonant_count += 1
    

  res = f'vowels: {vowel_count}, consonants: {consonant_count}'
  return res

print(vowel_consonant_count("heello"))
