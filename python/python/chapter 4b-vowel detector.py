word = str(input())
v_count = 0
if 'a' in word:
  v_count += 1
if 'e' in word:
  v_count +=1
if 'i' in word:
  v_count +=1
if 'o' in word:
  v_count +=1
if 'u' in word:
  v_count +=1

if v_count == 1:
  print("There is only one different vowel in the string.")
else:
  print(f"There are {v_count} different vowels in the string.")
    
