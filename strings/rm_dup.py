def rm_dup(str):
  final = []
  for s in str:
    if s not in final:
      final.append(s)
  return ''.join(final)
  
print(rm_dup("hello"))
