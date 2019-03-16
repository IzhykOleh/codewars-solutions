def duplicate_count(text): 
  txt = {}
  for i in text:
      if i.isupper():
          i = i.lower()
      if i in txt:
          txt[i]=txt.get(i)+1
      else:
          txt[i]=1
  count=0
  for i,j in txt.items():
      if j>1:
          count+=1
  return count
