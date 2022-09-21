def commoncharacters( w1, w2 ):
  array = []
  if len(w1) >= len(w2):
    for x in w1:
      if x.isalpha()== True and x in w2:
        if x in array:
          break
        else:
          array.append(x)
  else:
    for z in w2:
      if z.isalpha()== True and z in w1:
        if z in array:
          break
        else:
          array.append(z)

    
  
  return len(array)

w1 = "bee"
w2 = "beae"
print(commoncharacters(w1, w2))